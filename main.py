# A python script to track the prize of your favourite item on Amazon
# and it will send you an email when the prize has fallen down to your desired value

#imports
import requests
from bs4 import BeautifulSoup
import smtplib

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('example@gmail.com','password@123')
    subject = ' Hey The Price went Down !'
    body = 'chech the link https://www.amazon.in/Apple-iPhone-Pro-Max-64GB/dp/B07XVLMZHH/ref=sr_1_1_sspa?crid=12IX598OL25CR&dchild=1&keywords=iphone+11+pro+max+512gb&qid=1595413045&sprefix=ihpne+%2Caps%2C526&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWlM1RlpaNzZYTUw0JmVuY3J5cHRlZElkPUEwNjg1OTEwWlI0U01JV1BQT0FYJmVuY3J5cHRlZEFkSWQ9QTA4NTY5NzUzSlBaRlZLSUNRWDRNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    msg = f"Subject : (subject}\n\n\n{body}"
    server.sendmail(
        'example@gmail.com',
        'example@gmail.com',
        msg
    )
    print('Hey , mail sent successfully !')
    server.quit()
while(true):
    url = "https://www.amazon.in/Apple-iPhone-Pro-Max-64GB/dp/B07XVLMZHH/ref=sr_1_1_sspa?crid=12IX598OL25CR&dchild=1&keywords=iphone+11+pro+max+512gb&qid=1595413045&sprefix=ihpne+%2Caps%2C526&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWlM1RlpaNzZYTUw0JmVuY3J5cHRlZElkPUEwNjg1OTEwWlI0U01JV1BQT0FYJmVuY3J5cHRlZEFkSWQ9QTA4NTY5NzUzSlBaRlZLSUNRWDRNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
    headers = {"User-Agent" :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id ="productTitle").get_text()
    price = soup.find(id ='priceblock_ourprice').get_text()
    converted_price = float(price[0:5])
    if(converted_price < 1,15,000.00):
        send_mail()
    sleep(60*60)
