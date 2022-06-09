from bs4 import BeautifulSoup
import requests
import lxml


url = "https://www.amazon.com/Backpack-Business-Backpacks-Charging-Computer/dp/B08SWBTKBH/ref=sr_1_1_sspa?crid=15FA395J79ND&keywords=backpack&qid=1654017077&s=electronics&sprefix=back%2Celectronics%2C1415&sr=1-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFHU1BCWkRIUUM3VkEmZW5jcnlwdGVkSWQ9QTAyMjk5MzIxTE1QOFoyVFhTUEY5JmVuY3J5cHRlZEFkSWQ9QTA2MDY0NTcxWldWOTRBRFpUSFlRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
#print(price_as_float)


import smtplib

title = soup.find(class_="a-offscreen").get_text().strip()
print(title)

BUY_PRICE = 15

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        result = connection.login('paradoxoxymoron5@gmail.com', 'Abdulkareem150')
        connection.sendmail(
            from_addr='paradoxoxymoron5@gmail.com',
            to_addrs='paradoxoxymoron5@gmail.com',
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )