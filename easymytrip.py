import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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


def getEasyMyTripFlights(fromplacecode, toplacecode, flights):
    #settingup browser and opening it
    print("working on easymytrip")
    options = Options()
    #options.add_argument("headless")
    service = Service(executable_path = "chromedriver.exe")
    browser= webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    browser.get('https://www.easemytrip.com/flights.html')


    timespace = 0.5
    # This is to set boarding place for tirp
    frombox = browser.find_element(By.CSS_SELECTOR, "#FromSector_show")
    frombox.click()
    time.sleep(timespace)
    firstsearchbox = browser.find_element(By.CSS_SELECTOR, "#a_FromSector_show")
    firstsearchbox.send_keys(fromplacecode)
    time.sleep(timespace)
    firstsearchresult = browser.find_element(By.XPATH, '//*[@id="fromautoFill"]/ul/li[1]')
    firstsearchresult.click()
    time.sleep(timespace)

    # This is to set destination for trip
    tobox = browser.find_element(By.CSS_SELECTOR, "#Editbox13_show")
    tobox.click()
    time.sleep(timespace)
    secondsearchbox = browser.find_element(By.CSS_SELECTOR, "#a_Editbox13_show")
    secondsearchbox.send_keys(toplacecode)
    time.sleep(timespace)
    secondsearchresult = browser.find_element(By.XPATH, '//*[@id="toautoFill"]/ul/li[1]')
    secondsearchresult.click()

    time.sleep(3)

    # Clicking on search button 
    searchbutton = browser.find_element(By.XPATH, '//*[@id="showOWRT"]/div/div[7]/button')
    searchbutton.click()

    time.sleep(8)


    #getting the information of the flight details like flightname, start time, end time, price, total time
    list = browser.find_elements(By.CLASS_NAME, 'main-bo-lis')
    
    for curflight in list:
            flightname = curflight.find_element(By.XPATH, './div[1]/div[1]/div/div[2]/span[1]').text
            flightnumber1 = curflight.find_element(By.XPATH, './div[1]/div[1]/div/div[2]/span[2]/span[1]').text
            flightnumber2 = curflight.find_element(By.XPATH, './div[1]/div[1]/div/div[2]/span[2]/span[2]').text
            flightnumber = flightnumber1 + "-" + flightnumber2
            starttime = curflight.find_element(By.XPATH, './div[1]/div[2]/span[1]').text
            endtime = curflight.find_element(By.XPATH, './div[1]/div[4]/span[1]').text
            totaljourneytime = curflight.find_element(By.XPATH, './div[1]/div[3]/span[1]').text
            totalstops = curflight.find_element(By.XPATH, './div[1]/div[3]/span[2]').text
            #try:
                #price1 = curflight.find_element(By.XPATH, './div[1]/div[5]/div[2]')
                #price = price1.find_element(By.CLASS_NAME, 'ng-binding').text
            #except:
            pricelist  = curflight.find_elements(By.XPATH, './div[1]/div[5]/div[1]/div[2]')
            price = pricelist[0].text
            #    price = 23
            f = flight(flightname, flightnumber, starttime, endtime, totaljourneytime, totalstops, price)
            #print(f)
            flights.append(f)
    #print(list)
    return flights


#flights =[]
#getEasyMyTripFlights("bangalore", "delhi", flights)
