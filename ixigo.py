import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class flight:
    def __init__(self,  flightname, flightnumber, starttime, endtime, totaljourneytime, totalstops, price):
        self.flightname = flightname
        self.flightnumber = flightnumber
        self.starttime = starttime
        self.endtime = endtime
        self.totaljourneytime = totaljourneytime
        self.totalstops = totalstops
        self.price = price
    def __str__(self):
        return f" {self.flightname} {self.flightnumber} {self.starttime} {self.endtime} {self.totaljourneytime} {self.totalstops} {self.price}"

def getIxigoflights(fromplace, toplace, flights):
    print("working ixigo")
    options = Options()
    #options.add_argument("headless")
    service = Service(executable_path="chromedriver.exe")
    browser = webdriver.Chrome(service = service, options= options)
    browser.maximize_window()
    browser.get('https://www.ixigo.com/?utm_source=Google_Search&utm_medium=paid_search_google&utm_campaign=Ixigo_Brand&utm_source=google&utm_medium=paid_search_google&utm_campaign=ixigo_brand&gclid=EAIaIQobChMI06-x8IfW_QIVZoJLBR3ngQlYEAAYASAAEgK74fD_BwE')
 
    try:
        browser.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[5]/div/div/div[1]/div/div[2]').click()
    except:
        pass

    browser.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[5]/div/div/div[1]/div/div[1]/input').send_keys(fromplace)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[5]/div/div/div[1]/div/div[3]/div/div[1]').click()
    
    try:
        browser.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[5]/div/div/div[1]/div/div[3]/div/div[1]').click()
    except:
        pass
    browser.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[5]/div/div/div[3]/div/div[1]/input').send_keys(toplace)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[5]/div/div/div[3]/div/div[3]/div/div[1]').click()
    
    browser.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[5]/div/div/div[6]/button').click()
    time.sleep(8) 

    pages = browser.find_elements(By.CLASS_NAME, 'page-num')
    for x in pages:
        try:
            browser.find_element(By.XPATH, '//*[@id="content"]/div/div[4]/div[1]/div[3]/div/span[7]').click()
        except:
            pass
        main = browser.find_element(By.XPATH, '//*[@id="content"]/div/div[4]/div[1]/div[2]')
        list = main.find_elements(By.CLASS_NAME, 'c-flight-listing-row-v2')
        for object in list:
            flightname = object.find_element(By.XPATH, './div/div[1]/div[1]/div[2]/div/a/div').text
            flightnumber = object.find_element(By.XPATH, './div/div[1]/div[1]/div[2]/div/div').text
            starttime = object.find_element(By.XPATH, './div/div[1]/div[2]/div[1]/div[2]').text
            endtime = object.find_element(By.XPATH, './div/div[1]/div[2]/div[3]/div[2]').text
            totaljourneytime = object.find_element(By.XPATH, './div/div[1]/div[2]/div[2]/div/div[2]').text
            totalstops = object.find_element(By.XPATH, './div/div[1]/div[2]/div[2]/div/div[6]').text
            price = object.find_element(By.XPATH, './div/div[2]/div/div/div/div[1]/div/span[2]').text
            flights.append(flight(flightname, flightnumber, starttime, endtime, totaljourneytime, totalstops, price))



    time.sleep(10)

