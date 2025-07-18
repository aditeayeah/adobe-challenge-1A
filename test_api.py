import requests
import json
import os

# The URL of the API endpoint
url = 'http://127.0.0.1:5000/extract-outline'

# The path to the PDF file you want to upload
input_folder = os.path.join(os.path.dirname(__file__), 'input')
output_folder = os.path.join(os.path.dirname(__file__), 'output')

# List all PDFs in the input folder
pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
if not pdf_files:
    raise FileNotFoundError('No PDF files found in the input folder.')

for pdf_file in pdf_files:
    file_path = os.path.join(input_folder, pdf_file)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_json_path = os.path.join(output_folder, f'{base_name}.json')

    try:
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f, 'application/pdf')}

            # Send the POST request
            response = requests.post(url, files=files)
            data = response.json()
            print(f"Processed {pdf_file}: {data}")
            with open(output_json_path, 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)
            print(f"Output saved to {output_json_path}")
    except FileNotFoundError:
        print(f"File not found, skipping: {file_path}")
    except Exception as e:
        print(f"Error processing {pdf_file}: {e}")