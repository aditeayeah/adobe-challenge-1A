# PDF Outline Extraction API

## Overview
This project provides a simple REST API to extract the outline (headings) from a PDF document. The API is built using Flask and leverages the PyMuPDF (`fitz`) library to parse PDF files and extract their structure. A test script is included to demonstrate how to interact with the API and save the output to a JSON file.

---

## Approach
- The API accepts a PDF file upload via a POST request to the `/extract-outline` endpoint.
- The server processes the PDF using PyMuPDF, extracting headings and their page numbers.
- The extracted outline is returned as a JSON response, including heading levels, page numbers, and text.
- The test script (`test_api.py`) sends a sample PDF to the API and saves the JSON response to `output.json`.

---

## Models and Libraries Used
- **Flask**: For building the REST API server.
- **PyMuPDF (fitz)**: For reading and parsing PDF files.
- **requests**: For sending HTTP requests in the test script.
- **json**: For handling JSON serialization in the test script.

---

## Build and Run Instructions

### 1. Install Dependencies
Make sure you have Python 3.6+ installed. Install all required packages using:

```
pip install -r requirements.txt
```

### 2. Start the API Server
Run the following command in your project directory:

```
python api.py
```
You should see output indicating the server is running on `http://127.0.0.1:5000`.

### 3. Test the API
Edit `test_api.py` to set the correct path to your PDF file:
```python
file_path = r"C:\path\to\your\document.pdf"
```
Then, in a new terminal, run:
```
python test_api.py
```
This will send the PDF to the API and save the response to `output.json` in the same directory.

### 4. Output
- The extracted outline will be printed in the terminal and saved to `output.json`.

---

## Notes
- Ensure the API server is running before executing the test script.
- The solution is intended for local/development use only (do not use Flask's built-in server in production).
- If you encounter missing module errors, install them using `pip install <module>`.

---

## Example
Example output in `output.json`:
```json
{
  "outline": [
    {"level": "H1", "page": 2, "text": "Welcome to the"},
    {"level": "H1", "page": 3, "text": "Round 1A: Understand Your Document"}
  ],
  "title": "Welcome to the"
}
``` 