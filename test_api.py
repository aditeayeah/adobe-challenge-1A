import requests
import json

# The URL of the API endpoint
url = 'http://127.0.0.1:5000/extract-outline'

# The path to the PDF file you want to upload
file_path = r"C:\Users\ASUS\Downloads\Collection Receipt.pdf" # <-- CHANGE THIS

with open(file_path, 'rb') as f:
    files = {'file': (file_path, f, 'application/pdf')}

    # Send the POST request
    response = requests.post(url, files=files)
    data = response.json()
    print(data)
    with open('output.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
    print("Output saved to output.json")