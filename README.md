📘 Web Scraping Project – Books to Scrape

This project is a simple web scraping script built using Python, requests, and BeautifulSoup.
It extracts book information such as Product Name, Price, and Rating from the demo website
Books to Scrape, and stores the results in a CSV file.

🚀 Features

Scrapes book data from multiple pages

Extracts:

📌 Product Name

📌 Price

📌 Rating

Saves all data to products.csv

Beginner-friendly and easy to modify

🛠️ Technologies Used

Python 3

requests

BeautifulSoup (bs4)

CSV module

📂 Project Structure
project-folder/
│── task4.py
│── products.csv     # generated automatically
│── README.md

📥 Installation

Install required libraries:

pip install requests beautifulsoup4

▶️ How to Run

Run your Python script:

python task4.py


If everything works, you'll see:

✅ Data extracted and saved to products.csv

📑 Code (task4.py)

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

📝 Sample CSV Output
Product Name, Price, Rating
A Light in the ..., £51.77, Three
Tipping the Velvet, £53.74, One
...

🏁 Conclusion

This project is perfect for beginners who want to understand:

✔ Web scraping

✔ HTML parsing

✔ Working with CSV files

✔ Extracting structured information from websites

You can expand this project further by scraping more details, storing results in a database, or creating a UI.

Happy Coding! 🎉
