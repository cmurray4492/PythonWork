#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests

import csv

url = 'https://www.imdb.com/chart/top/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)


soup = BeautifulSoup(response.content, 'html.parser')

movies = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent')

print(len(movies))

csv_filename = "movies_data1.csv"


with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

    # Write the header row
    header = ['Rank', 'Name', 'Year', 'Rating']
    writer.writerow(header)

    # Write data for each movie in the list
    for movie in movies:
        name = movie.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-14dd939d-7 fjdYTb cli-title').a.text.split('.')[1]
        rank = movie.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-14dd939d-7 fjdYTb cli-title').a.text.split('.')[0]
        year = movie.find('div', class_='sc-14dd939d-5 cPiUKY cli-title-metadata').span.text
        rating = movie.find('div', class_='sc-951b09b2-0 hDQwjv sc-14dd939d-2 fKPTOp cli-ratings-container').span.text

        # Write the data row for the current movie directly to the CSV file
        writer.writerow([rank, name, year, rating])

print("Data has been written to the CSV file:", csv_filename)

