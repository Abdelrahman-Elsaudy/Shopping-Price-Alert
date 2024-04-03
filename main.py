import requests
from bs4 import BeautifulSoup
import smtplib
import os

# To do web scrapping, it's recommended to have your HTTP headers and pass them into the get request.
# You can get yours from: "https://myhttpheader.com/".
# You can save them inside a text file and retrieve them inside your code so that it can be shareable.
with open("http_headers.txt") as file:
    lines = file.readlines()

# Remove newline characters from each line.
lines = [line.strip() for line in lines]

my_headers = {
    "User-Agent": lines[0],
    "Accept": lines[1],
    "sec-ch-ua": lines[2],
    "sec-ch-ua-platform": lines[3],
    "Accept-Encoding": lines[4],
    "Accept-Language": lines[5]
}

# Get a link for the product you are interested in, I used noon.com as the online store.
product_page = ("https://www.noon.com/egypt-en/iphone-15-pro-256gb-natural-titanium-5g-with-facetime-international-"
                "version/N53432599A/p/?o=b4d0556ce71c086b&gclid=Cj0KCQjw2a6wBhCVARIsABPeH1utntNFCaI23cAa1l-AXjimh5OGMOh"
                "ru61h9SH-EoffIhb-3a7M_FkaAuWYEALw_wcB&utm_campaign=C1000151355N_eg_en_web_searchxxexactandphrasexxbr"
                "andpurexx08082022_noon_web_c1000088l_acquisition_sembranded_&utm_medium=cpc&utm_source=C1000088L")

# You can get a history of its price on amazon.com, so you can set a fair price for yourself.
# You can do that from this website: "https://camelcamelcamel.com/"
my_set_price = 60000.0

# Web scrapping.
response = requests.get(url=product_page, headers=my_headers)
noon_content = response.text
soup = BeautifulSoup(noon_content, "lxml")
price_tag = soup.find_all(name="div", class_="priceNow")
product_price = float(price_tag[0].getText().split()[1])

# Sending yourself an email when the price drops below your set price.
my_email = "abdelrahmanelsaudyyy@gmail.com"
password = os.getenv("elsaudyyy_email_pass")   # Saved windows environment variable.

if product_price < my_set_price:
    msg = f"Purchase link: {product_page}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        full_msg = f"Subject: IPhone 15 Pro for Less than {int(my_set_price)} EGP!\n\n{msg}"
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="abdelrahman.elsaudy@gmail.com",
                            msg=full_msg)
