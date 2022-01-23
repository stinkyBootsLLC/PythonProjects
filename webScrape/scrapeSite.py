"""
File Name: scrapeSite.py
Created Date: 1/23/2022
Author: Eduardo Estrada
Purpose: Create a csv file from Tobyhanna.army/news of latest 10 articles posted
"""
from bs4 import BeautifulSoup
import requests
import csv

URL = "https://www.tobyhanna.army.mil/Media/News/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
# create the csv file
csv_file = open('newTenArticles.csv', 'w')
csv_writer = csv.writer(csv_file)
# write first row (header)
csv_writer.writerow(['Date', 'Article', 'Summary'])

for row in soup.find_all("div", class_="item row"):
    # get columns
    articleDate = row.find("span", class_="date").text
    articleTitle = row.find("span", class_="title").a.text
    articleSummary = row.find("span", class_="hidden-xs").text
    # write to csv file
    csv_writer.writerow([articleDate, articleTitle, articleSummary])

csv_file.close()