# Load Selenium Components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import bs4 as bs
import json

# Establish chrome driver and options
opts = webdriver.ChromeOptions()
opts.headless = True
driver = webdriver.Chrome(options=opts)

# Set ticker code and final URL
ticker = "BHP"
url_suffix = {
    "profile": "/profile",
    "metrics": "/key-metrics",
    "income-annual": "/financials/income-statement-annual",
    "income-quarterly": "/financials/income-statement-quarterly"
}

url = "https://www.reuters.com/companies/{t}.AX{s}".format(t=ticker, s=url_suffix["income-annual"])
print(url)

# Request URL
driver.get(url)

# Wait for data to load
try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "__NEXT_DATA__")))
    print("Found!")
    data = driver.find_element_by_id("__NEXT_DATA__").get_attribute('innerHTML')
    data = json.loads(data.strip())
    print(data["props"]["initialState"]["markets"]["financials"])
except:
    print("Not Located :(")
finally:
    driver.quit()
