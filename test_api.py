import requests
import os

API_URL = 'http://localhost:5000/extract-outline'

INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'

pdf_files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith('.pdf')]

for pdf_file in pdf_files:
    with open(os.path.join(INPUT_FOLDER, pdf_file), 'rb') as f:
        files = {'file': (pdf_file, f, 'application/pdf')}
        response = requests.post(API_URL, files=files)
        if response.status_code == 200:
            output_path = os.path.join(OUTPUT_FOLDER, pdf_file.replace('.pdf', '.json'))
            with open(output_path, 'w', encoding='utf-8') as out_f:
                out_f.write(response.text)
        else:
            print(f'Failed to process {pdf_file}: {response.text}')