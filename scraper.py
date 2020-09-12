# Load Selenium Components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import bs4 as bs
import json as js


# Establish chrome driver and options
opts = webdriver.ChromeOptions()
opts.headless = True
driver = webdriver.Chrome(options=opts)

def get_financial_statements(ticker):
    url = "https://www.reuters.com/companies/{t}.AX/financials/income-statement-annual".format(t=ticker)
    try:
        data = get_json(url, "__NEXT_DATA__")
    except:
        print("Error")
    return data["props"]["initialState"]["markets"]["financials"]

def get_metrics(ticker):
    url = "https://www.reuters.com/companies/{t}.AX/key-metrics".format(t=ticker)
    try:
        data = get_json(url, "__NEXT_DATA__")
    except:
        print("Error")
    return data["props"]["initialState"]["markets"]["keymetrics"]

def get_profile(ticker):
    url = "https://www.reuters.com/companies/{t}.AX/profile".format(t=ticker)
    try:
        data = get_json(url, "__NEXT_DATA__")
    except:
        print("Error")
    return data["props"]["initialState"]["markets"]

def get_json(url, element_id):
    driver.get(url)
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, element_id)))
        data = driver.find_element_by_id(element_id).get_attribute('innerHTML')
        json = js.loads(data.strip())
    except:
        print("Error")
    finally:
        driver.quit()
    return json
