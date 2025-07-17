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

### 1. Install Dependencies (One-Time, Online)
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

## Docker Usage (No Python/Library Install Needed)

1. **Build the Docker image:**
   ```sh
   docker build -t pdf-outline-api .
   ```
2. **Run the Docker container:**
   ```sh
   docker run -p 5000:5000 pdf-outline-api
   ```
3. **Upload a PDF from your host:**
   - Use the provided `test_api.py` script (recommended), or
   - Use `curl`:
     ```sh
     curl -F "file=@C:/path/to/your/file.pdf" http://localhost:5000/extract-outline
     ```

---

## Offline Usage
- After installing dependencies or building the Docker image once (while online), you can run the API and process PDFs **completely offline**.
- No internet connection is required for running the API or uploading files.

---

## Step-by-Step: Host User Guide

1. **Install Docker Desktop** (if not already installed)
2. **Build the Docker image:**
   ```sh
   docker build -t pdf-outline-api .
   ```
3. **Run the Docker container:**
   ```sh
   docker run -p 5000:5000 pdf-outline-api
   ```
4. **Upload a PDF:**
   - Edit `test_api.py` to set your PDF path.
   - Run `python test_api.py` from your host.
   - Or use `curl` as shown above.
5. **View the output:**
   - Output will be printed in the terminal and saved to `output.json`.

---

## How to Push This Code to GitHub

1. Create a new repository on GitHub (do not initialize with README).
2. In your project directory, run:
   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git
   git branch -M main
   git push -u origin main
   ```
   Replace `YOUR-USERNAME` and `REPO-NAME` with your GitHub username and repository name.

---

## What Not to Do
- **Do not hardcode headings or file-specific logic:** The code must work for any PDF, not just a specific file.
- **Do not make API or web calls:** All processing is local; no external web requests are made.
- **Do not exceed runtime/model size constraints:** The code is efficient and uses only lightweight libraries.

---

## Example Output
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