from bs4 import BeautifulSoup
import requests
import lxml

url = ('https://www.jumia.com.ng/generic-color-screen-smart-bracelet-d13-waterproof-bracelet-73112864.html')
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(class_="-b -ltr -tal -fs24").get_text()

#print(price)


import smtplib

title = soup.find(class_="-b -ltr -tal -fs24").get_text().strip()
print(title)

BUY_PRICE = '₦ 4,000'

if price < BUY_PRICE:
    message = f"{title} is now {price}"



    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login('paradoxoxymoron5@gmail.com', 'Abdulkareem150')
        connection.sendmail(
            from_addr='paradoxoxymoron5@gmail.com',
            to_addrs='paradoxoxymoron5@gmail.com',
            msg=f"Subject: jumia Price Alert!\n\n{message}\n{url}".encode('utf-8')
        )
