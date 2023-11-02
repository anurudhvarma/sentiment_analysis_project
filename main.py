import os
import pandas as pd
import openpyxl
import requests
from bs4 import BeautifulSoup
# import urllib3
# from urllib3 import HTTPError
# Load the input excel file
input_file = r""
output_directory = "extracted_articles"
os.makedirs(output_directory, exist_ok=True)
# Load the excel file
df = pd.read_excel(input_file)
skipped_urls=[]
# Iterate through each row in the DataFrames
for index, row in df.iterrows():
    url_id = row["URL_ID"]
    url = row["URL"]
    print(f'index - {index}')

    # send a GET request to the URL
    response = requests.get(url)
    if response.status_code==404:
        print(f'url not accessible skipping')
        skipped_urls.append(url_id)
        continue
    response.raise_for_status()

    # parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # find the article title and text
    article_title = soup.find("title").get_text()
    article_text = ""
    for paragraph in soup.find_all("p"):
        article_text += paragraph.get_text() + "\n"

    # Save the extracted article to get atext file
    output_file = os.path.join(output_directory, f"{url_id}.txt")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(article_title + "\n\n")
        file.write(article_text)

    print(f"Extracted and saved article from {url} to {output_file}")

print(skipped_urls)


