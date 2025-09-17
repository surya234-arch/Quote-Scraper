from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import csv
 
 # Csv file open krna write mode me
with open('quotes.csv','w',encoding='utf-8',newline="") as file:
    writer=csv.writer(file)
    # header likh do
    writer.writerow(['Quote','Author'])

    # 5 pages scrape krnge
    for page in range(1,6):
        url = f"https://quotes.toscrape.com/page/{page}/"
        print("Scraping page:",{page})
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')
        quotes = soup.find_all('span',class_='text')
        authors = soup.find_all('small',class_='author')
        for quote,author in zip(quotes,authors):
            # csv me type krwa do
            writer.writerow([quote.text.strip()])
            writer.writerow([author.text.strip()])

            # terminal pe print 
            # print("Quote:",quote.text)
            # print("Author:",author.text)
        
            
 