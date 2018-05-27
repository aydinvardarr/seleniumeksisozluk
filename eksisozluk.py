
from selenium import webdriver
import random
import time

browser = webdriver.Chrome("/Users/aydinvardar/PycharmProjects/eksisozluk/venv/bin/chromedriver")
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
pageCount = 1
entries = []
entryCount = 1
while pageCount <= 10:
    randomPage = random.randint(1,1290)
    newUrl = url + str(randomPage)
    browser.get(newUrl)

    elemets = browser.find_elements_by_css_selector(".content")
    for element in elemets:
        entries.append(element.text)

    time.sleep(3)
    pageCount += 1

with open("entries.txt","w",encoding= "UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + ".\n")
        file.write("**********************************\n")
        entryCount += 1



browser.close()
