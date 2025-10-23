# BitHealth AI Pre-Test Submission

This repository contains the solutions for the BitHealth AI Pre-Test. The test is divided into three cases evaluating skills in Python data processing, SQL querying, and end-to-end API development with LLMs.

## Project Structure

```

.
├── .gitignore
├── Bithealth AI Pre Test.pdf (Original test instructions)
├── LICENSE
├── requirements.txt          (All Python dependencies)
│
├── case\_1/
│   ├── filter\_patients.ipynb (Solution for Case 1)
│   └── patients.csv          (Data for Case 1)
│
├── case\_2/
│   └── test\_data\_logic.sql   (Solution for Case 2)
│
└── case\_3/
├── .env                  (Environment variables template)
├── main.py               (FastAPI application for Case 3)
└── README.md             (Detailed instructions for Case 3)

````

## Global Setup & Installation

Follow these steps to set up the environment and run the solutions.

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/arifsoul/bithealth_test.git](https://github.com/arifsoul/bithealth_test.git)
    cd bithealth_test
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install All Dependencies**
    The `requirements.txt` file contains all packages needed for Case 1 and Case 3.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment for Case 3**
    The FastAPI application requires a Google AI API Key.
    
    * Navigate to the `case_3/` directory.
    * Create a `.env` file by copying the provided `case_3/.env` (which you've uploaded).
    * Ensure your `.env` file contains your API key and the desired model:
    
    ```.env
    GOOGLE_API_KEY="AIzaSy...[YOUR_API_KEY_HERE]"
    LLM_MODEL_NAME="gemini-2.5-flash-preview-09-2025"
    ```

---

## Solutions

### Case 1: Python - Basic Data Processing

* **Objective:** Load a CSV, tokenize symptom strings, and filter patients.
* **Location:** `case_1/`
* **Solution:** `case_1/filter_patients.ipynb`
* **Data:** `case_1/patients.csv`

**How to Run:**
1.  Ensure you have `pandas` and `tabulate` installed (they are in `requirements.txt`).
2.  Open and run the Jupyter Notebook `case_1/filter_patients.ipynb` cell by cell.
3.  The notebook will load `patients.csv`, process the data, and print the filtered results directly in the notebook.

### Case 2: Querying - SQL Insights

* **Objective:** Write a SQL query to find the top 5 recent visits to the 'Neurology' department for patients over 50 with at least 3 symptoms.
* **Location:** `case_2/`
* **Solution:** `case_2/test_data_logic.sql`

**How to Run:**
The file `case_2/test_data_logic.sql` contains the complete SQL query. It can be executed against any SQL database populated with the schema described in `Bithealth AI Pre Test.pdf`.

### Case 3: End-to-End Mini Project

* **Objective:** Create a FastAPI service to recommend a specialist department based on patient info, using an LLM.
* **Location:** `case_3/`
* **Solution:** `case_3/main.py`

**How to Run:**
1.  Navigate to the solution directory: `cd case_3`
2.  Ensure your `.env` file is correctly set up in this directory (see Step 4 of Global Setup).
3.  Run the FastAPI server using Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```
4.  The server will be running at `http://127.0.0.1:8000`.

**How to Test:**

* **Option 1: Interactive Docs (Swagger UI)**
    Open your browser and navigate to **`http://127.0.0.1:8000/docs`**. You can use the "Try it out" feature to test the `/recommend` endpoint.

* **Option 2: Terminal (PowerShell)**
    Use the following command to send a POST request (this command pipes the result to show only the JSON content):
    ```powershell
    curl -Uri "[http://127.0.0.1:8000/recommend](http://127.0.0.1:8000/recommend)" -Method POST -ContentType "application/json" -Body '{"gender": "female", "age": 62, "symptoms": ["pusing", "mual", "sulit berjalan", "kehilangan keseimbangan"]}' | Select-Object -ExpandProperty Content
    ```
    **Expected Response:**
    ```json
    {
      "recommended_department": "Neurologi"
    }
    ```

## Technology Stack

* **Python 3**
* **Pandas:** For data wrangling in Case 1.
* **Jupyter Notebook:** For the Case 1 solution.
* **SQL:** For the Case 2 query.
* **FastAPI & Uvicorn:** For the Case 3 web service.
* **LangChain & langchain-google-genai:** For LLM integration in Case 3.
* **Python-dotenv:** For managing environment variables.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.