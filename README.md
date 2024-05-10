# American Family Physician Algorithms

## Description

This repository houses a comprehensive JSON collection of 1,020 diagnostic and treatment algorithms from American Family Physician. Each algorithm is equipped with a vector search mechanism designed to identify similar patient profiles, making this a vital resource for medical researchers and professionals.

### Features

- **Extensive Collection:** Over 1,000 algorithms covering a wide range of medical conditions and treatments.
- **Vector Search:** Utilize a powerful search mechanism to find algorithms that match specific patient profiles.
- **Partial Access:** Some algorithms are fully available, while others are locked due to publisher restrictions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ruipreis/afp-algorithms.git
   ```
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the vector search functionality, ensure you have set your `OPENAI_API_KEY` as it's required for the script to function properly.

### Running the Script

Execute the `find_medical_profile.py` script with a medical profile to find relevant algorithms:
```bash
python find_medical_profile.py --profile "example medical profile" --k 5
```
- `--profile`: A string representing the medical profile to search for.
- `--k`: The number of search results to return (default is 5).

### Examples

Here's how you can search for a medical profile:
```bash
python find_medical_profile.py --profile "broken arm" --k 3
```

## Data Structure

Each JSON algorithm file under the `algorithms` path includes:
- **URL**: Link to the source document.
- **Title**: Name of the algorithm.
- **Author**: Author(s) of the document.
- **DOI**: Document identifier.
- **Abstract**: Summary of the algorithm.
- **Headers** and **Content**: Structured details and medical content.

Adding concrete examples to your README, including how to call your script and the expected output, can significantly enhance user understanding and showcase the functionality of your project. Here's how you can integrate sample examples with script calls and the expected raw output into the README:


## Example Usage

Below are three examples demonstrating how to use the `find_medical_profile.py` script to search for medical algorithms based on a specific medical profile. These examples illustrate different query complexities and show the typical output you can expect.

### Example 1

**Command:**
```bash
python find_medical_profile.py --profile "38-year-old female presenting with two weeks of persistent lower right quadrant abdominal pain, occasional nausea, and decreased appetite." --k 5
```

**Expected Output:**
```
> "A 55-year-old woman presented with multiple episodes of right upper quadrant abdominal pain over the course of one year. The episodes were separated by months during which she felt well. Each episode started abruptly, without warning, and without a relationship to food. Previously, she had undergone computed tomographic (CT) scanning of the abdomen, barium radiography and endoscopy of the digestive tract, and endoscopic retrograde cholangiopancreatography. The findings of these studies were normal."
        Title: The Abdominal Wall: An Overlooked Source of Pain | AAFP
        Author: SAUD SULEIMAN, M.D., AND DAVID E. JOHNSTON, M.D.
        URL: https://www.aafp.org/pubs/afp/issues/2001/0801/p431.html#afp20010801p431-f1
        DOI: Am Fam Physician.2001;64(3):431-439
        Score: 0.9091862440109253


> "The patient was now admitted with acute right upper quadrant pain. A tender, fluctuant 8-cm mass was felt in the right upper quadrant, several centimeters inferior to a subcostal scar from a previous open cholecystectomy. An abdominal CT scan was initially read as normal, but review of the scan showed herniation of omentum through a defect in the abdominal wall near the site of the cholecystectomy scar(Figure 3)."
        Title: The Abdominal Wall: An Overlooked Source of Pain | AAFP
        Author: SAUD SULEIMAN, M.D., AND DAVID E. JOHNSTON, M.D.
        URL: https://www.aafp.org/pubs/afp/issues/2001/0801/p431.html#afp20010801p431-f1
        DOI: Am Fam Physician.2001;64(3):431-439
        Score: 0.8712348937988281


> "The patient described previously returns two months later with intermittent nausea and vomiting that is much less severe than on initial presentation. Her current symptoms have lasted two days, and she has had six bouts of emesis. She has no fever, chills, or headache, but has intermittent epigastric discomfort associated with nausea and vomiting. Her symptoms are not relieved by antacids, and she has no melena or blood in her stool. She says she feels full quickly when eating and often feels bloated. She has not had contact with any sick persons or toxins, does not drink alcohol, and appears well hydrated."
        Title: Evaluation of Nausea and Vomiting in Adults: A Case-Based Approach | AAFP
        Author: WILLIAM D. ANDERSON, III, MD, AND SCOTT M. STRAYER, MD, MPH
        URL: https://www.aafp.org/pubs/afp/issues/2013/0915/p371.html#afp20130915p371-f1
        DOI: Am Fam Physician.2013;88(6):371-379
        Score: 0.8706697225570679


> "A 33-year-old woman with a history of nephrolithiasis presents with a four-week history of urinary frequency, urgency, urge incontinence, and dysuria. She recently had ureteroscopy with lithotripsy of a 9-mm obstructing left ureteral stone; she does not know if a ureteral stent was placed. She has constant dull left flank pain that becomes sharp with voiding. Results of her urinalysis with microscopy are shown inTable 4."
        Title: Urinalysis: Case Presentations for the Primary Care Physician | AAFP
        Author: VICTORIA J. SHARP, MD, DANIEL K. LEE, MD, AND ERIC J. ASKELAND, MD
        URL: https://www.aafp.org/pubs/afp/issues/2014/1015/p542.html#afp20141015p542-f1
        DOI: Am Fam Physician.2014;90(8):542-547
        Score: 0.8662539124488831


> "Patients often present with acute, constant abdominal pain that is usually in the left lower quadrant.1,9Other possible symptoms include anorexia, constipation, nausea, diarrhea, and dysuria.1Patients may have a history of diverticulosis or diverticulitis. Although patients with diverticulitis typically have a fever (usually below 102°F [39°C]), in one study, nine of 62 patients with acute diverticulitis were afebrile.10Tachycardia and hypotension may occur and should raise suspicion for complicated diverticulitis. On examination, tenderness only in the left lower quadrant significantly increases the likelihood of acute diverticulitis (positive likelihood ratio = 10.4), as do a palpable mass and abdominal distention.9"
        Title: Diagnosis and Management of Acute Diverticulitis | AAFP
        Author: THAD WILKINS, MD, KATHERINE EMBRY, MD, AND RUTH GEORGE, MD
        URL: https://www.aafp.org/pubs/afp/issues/2013/0501/p612.html#afp20130501p612-f3
        DOI: Am Fam Physician.2013;87(9):612-620
        Score: 0.8659937381744385
```

### Example 2

**Command:**
```bash
python find_medical_profile.py --profile "45-year-old male experiencing recurrent bouts of diarrhea, abdominal cramping, and unintended weight loss over the past three months." --k 5
```

**Expected Output:**
```
> "Irritable bowel syndrome (IBS) is the most common cause of functional diarrhea in the developed world. IBS is a symptom complex of crampy abdominal pain accompanied by altered bowel habits, either with diarrhea or constipation. Usually watery diarrhea occurs while awake, often following meals. Discomfort is alleviated by defecation, and stool mucus is noted in one-half of patients.12Women are diagnosed twice as often as men. “Alarm” symptoms such as nocturnal diarrhea, progressive pain, weight loss, or blood in the stool suggest another diagnosis."
        Title: Evaluation of Chronic Diarrhea | AAFP
        Author: GREGORY JUCKETT, MD, MPH, AND RUPAL TRIVEDI, MD
        URL: https://www.aafp.org/pubs/afp/issues/2011/1115/p1119.html#afp20111115p1119-f2
        DOI: Am Fam Physician.2011;84(10):1119-1126
        Score: 0.8529992699623108


> "Irritable bowel syndrome (IBS) is the most common cause of functional diarrhea in the developed world. IBS is a symptom complex of crampy abdominal pain accompanied by altered bowel habits, either with diarrhea or constipation. Usually watery diarrhea occurs while awake, often following meals. Discomfort is alleviated by defecation, and stool mucus is noted in one-half of patients.12Women are diagnosed twice as often as men. “Alarm” symptoms such as nocturnal diarrhea, progressive pain, weight loss, or blood in the stool suggest another diagnosis."
        Title: Evaluation of Chronic Diarrhea | AAFP
        Author: GREGORY JUCKETT, MD, MPH, AND RUPAL TRIVEDI, MD
        URL: https://www.aafp.org/pubs/afp/issues/2011/1115/p1119.html#afp20111115p1119-f1
        DOI: Am Fam Physician.2011;84(10):1119-1126
        Score: 0.8529992699623108


> "A 37-year-old woman with a history of irritable bowel syndrome and a benign breast tumor presents with recurring nausea as well as a six-month history of intense but brief episodes of dizziness, chest tightness and shortness of breath. During the episodes, the patient reports feelings of being “trapped” and fears that she has a serious medical problem or is about to have a “nervous breakdown.” Eight months before this visit, the patient had obtained a challenging new position in her desired field. While pleased with her success, the patient is worried about new responsibilities and “office politics.” The patient does not drink, but has resumed smoking, indulging in two or three cigarettes in the mornings."
        Title: Using DSM-IV Primary Care Version: A Guide to Psychiatric Diagnosis in Primary Care | AAFP
        Author: DAVID PINGITORE, PH.D., AND RANDY A. SANSONE, M.D.
        URL: https://www.aafp.org/pubs/afp/issues/1998/1015/p1347.html#afp19981015p1347-f1
        DOI: Am Fam Physician.1998;58(6):1347-1352
        Score: 0.8529711365699768


> "Functional diarrhea is distinct from IBS. Rome IV diagnostic criteria for functional diarrhea are “loose or watery stools, without predominant abdominal pain or bothersome bloating, occurring in greater than 25% of stools” for the past three months, with the onset of symptoms at least six months before diagnosis. Patients who meet the criteria for IBS cannot receive a diagnosis of functional diarrhea. The prevalence of functional diarrhea in adults may be as high as 17%. Functional diarrhea should be diagnosed after a reasonable effort at evaluating for organic disease. Lack of improvement with empiric loperamide (Imodium) should prompt reconsideration of the diagnosis.3"
        Title: Chronic Diarrhea in Adults: Evaluation and Differential Diagnosis | AAFP
        Author: KRISTINA BURGERS, MD, BRIANA LINDBERG, MD, AND ZACHARY J. BEVIS, MD
        URL: https://www.aafp.org/pubs/afp/issues/2020/0415/p472.html#afp20200415p472-f1
        DOI: Am Fam Physician.2020;101(8):472-480
        Score: 0.8494458198547363


> "A diagnosis of Crohn's disease should be considered in any patient who presents with chronic or nocturnal diarrhea, abdominal pain, bowel obstruction, weight loss, fever, or night sweats.5However, symptoms of Crohn's disease are often insidious, and diagnosis can be difficult. Patients may have intermittent symptoms with varying periods of remission. Over time, symptomatic periods may increase in frequency and severity."
        Title: Management of Crohn's Disease—A Practical Approach | AAFP
        Author: DOUG KNUTSON, M.D., GREG GREENBERG, M.D., AND HOLLY CRONAU, M.D.
        URL: https://www.aafp.org/pubs/afp/issues/2003/0815/p707.html#afp20030815p707-f1
        DOI: Am Fam Physician.2003;68(4):707-715
        Score: 0.8484129309654236
```
