import requests
from bs4 import BeautifulSoup
import json

def extract_text_between_substrings(url):
    try:
        # Make a GET request to fetch the raw HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and clean the text from the page
        text = soup.get_text().strip().replace('\n', ' ').replace('\r', '')

        # Find indices of the specified substrings
        start_index = text.find("CompanyJobs")
        end_index = text.find("Footer", start_index)

        if start_index != -1 and end_index != -1:
            # Extract the text between the substrings, including the end substring
            extracted_text = text[start_index + len("CompanyJobs"):end_index]
            return extracted_text
        else:
            return "Substrings not found in the text."
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

with open('companies.json', 'r') as infile:
    data = json.load(infile)

# Iterate over each URL and add the description
counter =0
for item in data:
    if "url" in item:
        counter += 1
        result = extract_text_between_substrings(item["url"])
        item["description"] = result
        print(counter)

# Save the updated data to a JSON file
with open("companies_with_description.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

print("Data saved to companies_with_description.json")