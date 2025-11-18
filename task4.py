import requests
from bs4 import BeautifulSoup
import csv

# Base URL of the practice site
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

# Open CSV file for writing
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write header row
    writer.writerow(["Product Name", "Price", "Rating"])

    # Loop through multiple pages (first 5 pages for demo)
    for page in range(1, 6):
        url = BASE_URL.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract product info
        products = soup.find_all("article", class_="product_pod")
        for product in products:
            # Product name
            name = product.h3.a["title"]

            # Price
            price = product.find("p", class_="price_color").text

            # Rating (stored as class name, e.g., "star-rating Three")
            rating_class = product.find("p", class_="star-rating")["class"]
            rating = rating_class[1] if len(rating_class) > 1 else "No rating"

            # Write row to CSV
            writer.writerow([name, price, rating])

print("✅ Data extracted and saved to products.csv")