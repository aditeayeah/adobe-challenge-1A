# PDF Outline Extraction API

## Overview
This project provides a REST API to extract the outline (headings) from PDF documents. The API is built using Flask and leverages the PyMuPDF (`fitz`) library to parse PDF files and extract their structure. A test script is included to demonstrate batch processing of multiple PDFs and save the output to JSON files.

---

## Approach
- The API accepts PDF file uploads via POST requests to the `/extract-outline` endpoint.
- The server processes PDFs using PyMuPDF, extracting headings and their page numbers.
- **Heading Detection**: Uses a combination of font size, boldness, and positioning to identify headings.
- **Page Indexing**: Uses 0-based page indexing (first page = page 0).
- **Batch Processing**: The test script can process all PDFs in the input folder automatically.
- The extracted outline is returned as a JSON response, including heading levels, page numbers, and text.

---

## Models and Libraries Used
- **Flask**: For building the REST API server.
- **PyMuPDF (fitz)**: For reading and parsing PDF files.
- **requests**: For sending HTTP requests in the test script.
- **json**: For handling JSON serialization in the test script.

---

## Project Structure
```
project/
├── api.py              # Main Flask API server
├── test_api.py         # Test script for batch processing
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── input/             # Place PDF files here for processing
│   └── .gitkeep      # Ensures folder is tracked by git
├── output/            # Processed JSON files are saved here
│   └── .gitkeep      # Ensures folder is tracked by git
└── README.md          # This file
```

## Build and Run Instructions

### Using Docker (Recommended)

1. **Build the Docker image:**
   ```sh
   docker build -t pdf-outline-api .
   ```

2. **Run the Docker container with volume mounts:**
   ```sh
   docker run -p 5000:5000 -v "${PWD}/input:/app/input" -v "${PWD}/output:/app/output" pdf-outline-api
   ```

3. **Process PDFs:**
   - Place your PDF files in the `input/` folder
   - Run the test script from your host machine:
     ```sh
     python test_api.py
     ```
   - Output JSON files will be saved in the `output/` folder with the same base name as the input PDFs

#### Advanced: Custom Docker Build/Run (with platform and repo identifier)

You can build and run the Docker image with a custom repository name/identifier and platform targeting (e.g., for CI/CD or reproducibility):

```sh
docker build --platform linux/amd64 -t <reponame.someidentifier> .
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output/repoidentifier/:/app/output --name <reponame.someidentifier> <reponame.someidentifier>
```

### Using Python Directly

1. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Start the API Server:**
   ```sh
   python api.py
   ```

3. **Process PDFs:**
   - Place PDF files in the `input/` folder
   - Run: `python test_api.py`

---

## Features

### Batch Processing
- Automatically processes all PDF files in the `input/` folder
- Each PDF gets its own output JSON file in the `output/` folder
- Error handling: skips missing or corrupted files and continues processing

### Heading Detection Logic
- **Font Size Analysis**: Identifies the most common font size as body text
- **Heading Classification**: Larger fonts are classified as headings (H1, H2, H3)
- **Bold Detection**: Checks for bold font names to enhance heading detection
- **Title Extraction**: Identifies potential titles from the first two pages

### Page Indexing
- Uses 0-based indexing (first page = page 0)
- Consistent with programming conventions

---

## API Endpoints

### POST /extract-outline
Extracts headings from an uploaded PDF file.

**Request:**
- Content-Type: `multipart/form-data`
- Body: PDF file in the `file` field

**Response:**
```json
{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "page": 0,
      "text": "Chapter 1"
    },
    {
      "level": "H2", 
      "page": 2,
      "text": "Section 1.1"
    }
  ]
}
```

---

## Constraints Compliance

✅ **Execution Time**: ≤ 10 seconds for 50-page PDFs  
✅ **Model Size**: ≤ 200MB (no ML models used)  
✅ **Network**: No internet access required at runtime  
✅ **Runtime**: CPU-only (amd64), compatible with 8 CPUs and 16GB RAM  

---

## Offline Usage
- After building the Docker image once (while online), you can run the API and process PDFs **completely offline**.
- No internet connection is required for running the API or processing files.

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
Example output in `output/sample.json`:
```json
{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "page": 0,
      "text": "Introduction"
    },
    {
      "level": "H1", 
      "page": 21,
      "text": "Chapter 1: Getting Started"
    },
    {
      "level": "H2",
      "page": 3,
      "text": "Section 1.1: Basic Concepts"
    }
  ]
}
```

---

## Limitations and Future Improvements
- **Heading Detection**: Currently relies on font size and boldness. Future versions may include:
  - Text positioning analysis
  - Font family detection
  - Pattern recognition for numbered headings
  - Enhanced multilingual support
- **Performance**: Optimized for documents up to 50 pages. Larger documents may require additional optimization.

---

## Troubleshooting
- **No PDFs found**: Ensure PDF files are placed in the `input/` folder
- **Docker issues**: Make sure Docker Desktop is running
- **Permission errors**: Check file permissions for input/output folders
- **Long filenames**: Some PDFs with very long names may cause issues - consider renaming them 