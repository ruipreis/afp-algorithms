# find_medical_profile.py
# Description: This script is used to find the most relevant medical profile for a given user profile.

import json
import os
from pathlib import Path

import requests
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.vectorstores.utils import DistanceStrategy


def download_faiss_vectorstore(folder_name: str = "afp.faiss"):
    # URLs of the files to be downloaded
    urls = [
        "https://storage.googleapis.com/ruipreis_public_datasets/afp.faiss/index.faiss",
        "https://storage.googleapis.com/ruipreis_public_datasets/afp.faiss/index.pkl",
    ]

    # Create the directory if it doesn't already exist
    os.makedirs(folder_name, exist_ok=True)

    # Loop through the URLs
    for url in urls:
        # Extract the file name from the URL
        file_name = url.split("/")[-1]

        # Full path to where the file will be saved
        path = os.path.join(folder_name, file_name)

        if os.path.isfile(path):
            print(f"{file_name} already exists in {folder_name}/")
            continue

        # Make the request to download the file
        response = requests.get(url, stream=True)

        # Check if the request was successful
        if response.status_code == 200:
            # Open the file path for writing in binary mode
            with open(path, "wb") as f:
                # Write the contents of the response to the file
                f.write(response.content)
            print(f"Downloaded {file_name} to {folder_name}/")
        else:
            print(
                f"Failed to download {file_name}. Status code: {response.status_code}"
            )


def _get_available_algorithms():
    return list((Path(__file__).parent / "algorithms").glob("*.json"))


def _build_faiss_index(out_path: str = "afp.faiss"):
    from tqdm import tqdm

    available_algorithms = _get_available_algorithms()
    embeddings = OpenAIEmbeddings()

    documents = []

    for algorithm_path in tqdm(available_algorithms):
        with open(algorithm_path, "r") as f:
            algorithm = json.load(f)

        # For each document it is very important that we store the algorithm metadata
        core_metadata = {
            "title": algorithm["title"],
            "url": algorithm["url"],
            "author": algorithm["author"],
            "doi": algorithm["doi"],
            "locked": algorithm["locked"],
        }

        if algorithm["abstract"] is not None:
            abstract_document = Document(
                page_content=algorithm["abstract"],
                metadata={
                    **core_metadata,
                    "type": "abstract",
                },
            )
            documents.append(abstract_document)

        # Then parse all of the contents
        headers = {k["id"]: k for k in algorithm["headers"]}

        for content in algorithm["content"]:
            matching_header = (
                None if content["parent"] == -1 else headers[content["parent"]]
            )

            content_metadata = {
                **core_metadata,
                "type": "content",
            }

            if matching_header is not None:
                content_metadata["header"] = matching_header

            content_document = Document(
                page_content=content["text"],
                metadata=content_metadata,
            )

            documents.append(content_document)

    # Instantiate a text splitter, which may be useful for splitting up the text
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_documents = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(
        split_documents,
        embeddings,
        distance_strategy=DistanceStrategy.MAX_INNER_PRODUCT,
    )
    db.save_local(out_path)

    return db


def load_afp_faiss(path: str = "afp.faiss") -> FAISS:
    if not os.path.exists(path):
        return _build_faiss_index(path)

    return FAISS.load_local(
        path,
        OpenAIEmbeddings(),
        distance_strategy=DistanceStrategy.MAX_INNER_PRODUCT,
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", help="The medical profile to search for", type=str)
    parser.add_argument(
        "--k", help="The number of results to return", type=int, default=5
    )
    args = parser.parse_args()

    # Download the FAISS index if it doesn't already exist
    download_faiss_vectorstore()

    # Load a FAISS index with the AFP dataset
    afp_faiss = load_afp_faiss()

    # Search for the meidcal profile
    results = afp_faiss.similarity_search_with_score(
        args.profile, k=args.k, filter=dict(locked=False)
    )

    # Present the corresponding results to the user
    for result, score in results:
        print(f'> "{result.page_content}"')
        print(f"\tTitle: {result.metadata['title']}")
        print(f"\tAuthor: {result.metadata['author']}")
        print(f"\tURL: {result.metadata['url']}")
        print(f"\tDOI: {result.metadata['doi']}")
        print(f"\tScore: {score}")
        print()
        print()
