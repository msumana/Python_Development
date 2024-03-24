# Author Sumana Price stock and sending email
from selenium import webdriver
import time
import smtplib
import os


def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
  return driver


def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(" ")[0])
  return output


def send_mail(price_percentage):
  sender = os.getenv('SENDER')
  reciever = os.getenv('RECIEVER')
  password = os.getenv('PASSWORD')

  message = """
  This is to inform you that the percentage change of the stock is {}%
  """.format(price_percentage)
  # print(message)

  server = smtplib.SMTP('smtp.office365.com', 587)
  server.starttls()
  server.login(sender, password)
  server.sendmail(sender, reciever, message)
  server.quit()


def main():
  driver = get_drvier()
  time.sleep(2)
  element = driver.find_element(
      by="xpath",
      value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
  price_percentage = str(clean_text(element.text))
  # print(price_percentage)
  if float(price_percentage) <= 0.43:
    send_mail(price_percentage)


main()
