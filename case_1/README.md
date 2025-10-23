# Case 1: Python - Basic Data Processing

This folder contains the solution for Case 1 of the BitHealth AI Pre-Test.

## 1. Objective

The objective of this case is to test data wrangling, logic, and language fluency in Python.

## 2. Task Description

The task is to create a Python script within a Jupyter Notebook (`.ipynb`) that performs the following actions:

1.  Loads the `patients.csv` file.
2.  Tokenizes (splits) the `symptoms` column from a string into a list.
3.  Filters the patients to find those who are **older than 40** AND have **more than 2 symptoms**.

## 3. Files in This Directory

* **`filter_patients.ipynb`**: The main solution in Jupyter Notebook format, containing all the code and output.
* **`patients.csv`**: The raw data file used as input for the script.

## 4. Requirements

This script requires the following Python libraries:

* `pandas`
* `tabulate` (used by the notebook to print clean markdown tables)

These dependencies can be installed from the `requirements.txt` file in the root directory:

```bash
pip install -r ../requirements.txt
````

## 5\. How to Run

1.  Ensure you have Jupyter Notebook or a compatible environment (like VS Code with the Jupyter extension) installed.
2.  Make sure you have installed the required libraries (see section 4).
3.  Open the `filter_patients.ipynb` file.
4.  Run the cells sequentially from top to bottom.
5.  The notebook will load `patients.csv`, display the original data, the tokenized data, and finally the filtered results.

## 6\. Expected Output

After running the final cell, the notebook will display the filtered data frame as markdown, matching the required criteria (Age \> 40 & Symptom Count \> 2):

```markdown
--- Hasil Filter (Usia > 40 TAHUN & Jumlah Gejala > 2) ---
|   id | name   |   age | symptoms                       | symptom_list                           |   symptom_count |
|-----:|:-------|------:|:-------------------------------|:---------------------------------------|----------------:|
|    1 | Andi   |    45 | demam, batuk, sesak napas      | ['demam', 'batuk', 'sesak napas']      |               3 |
|    7 | Gio    |    49 | menggigil, batuk, sakit kepala | ['menggigil', 'batuk', 'sakit kepala'] |               3 |
```
