import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
prices = []

# Scrape first 5 pages (or you can expand)
for page in range(1, 6):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip()
        titles.append(title)
        prices.append(price)

# Store data in DataFrame
df = pd.DataFrame({'Title': titles, 'Price': prices})
df.to_csv('books.csv', index=False)

print("Scraped data saved to books.csv")
