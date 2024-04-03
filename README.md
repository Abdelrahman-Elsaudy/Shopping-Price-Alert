# Shopping Price Alert

---

- This tool emails you when the price of a product you are interested in drops to a certain price:

![email_alert](https://github.com/Abdelrahman-Elsaudy/NLP-Workout-Tracker-on-Google-Sheets/assets/158151388/7cd48bc8-1151-4005-b49c-c9dbd1315d81)

---

## Skills Practiced:

---

- Web scrapping using `BeautifulSoup` module in Python.
- Sending emails using `SMTP` module in Python.
- Code automation using [PythonAnywhere](www.pythonanywhere.com).

---

## Prerequisites:

---

- Determining a product you are interested in and getting its purchase link on [Noon](www.noon.com).
- Setting a fair price for yourself, you can use [Camelcamelcamel](https://camelcamelcamel.com/) for this.
- Getting your [HTTP headers](https://myhttpheader.com/).
- Having two emails for sending and receiving, and generating App Password for the sending email.

---
## How This Tool Works:

1. This tool scraps the product webpage to find its current price.
```
# Web scrapping.
response = requests.get(url=product_page, headers=my_headers)
noon_content = response.text
soup = BeautifulSoup(noon_content, "lxml")
price_tag = soup.find_all(name="div", class_="priceNow")
product_price = float(price_tag[0].getText().split()[1])
```
2. After that it compares it to the price you set, if the current price is lower, it emails you the product webpage so 
you can order it.
```
if product_price < my_set_price:
    msg = f"Purchase link: {product_page}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        full_msg = f"Subject: IPhone 15 Pro for Less than {int(my_set_price)} EGP!\n\n{msg}"
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="abdelrahman.elsaudy@gmail.com",
                            msg=full_msg)
```
---

## User Tips:
- I recommend saving your HTTP headers inside a text file and including it in `gitignore` so your code is shareable.
- If you want the code to run everyday you can upload it on [PythonAnywhere](www.pythonanywhere.com) and set a time for
its daily activation.

---
_Credits to: 100-Days of Code Course on Udemy._