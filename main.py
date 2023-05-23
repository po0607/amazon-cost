import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
MY_BUY_PRICE = 160
my_email = "traderjacob0607@gmail.com"
my_password = "hdruzrceltaxudbo"

url = "https://a.co/d/aPkqHag"
headers = {"Accept-Language": "zh-TW,zh;q=0.5", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = float(soup.find(class_="a-price-whole").get_text())
print(price)

title = soup.find(name="span", id="productTitle").get_text().strip()
print(title)

if price < MY_BUY_PRICE:
    message = f"Philips Norelco 7800 is now {price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
