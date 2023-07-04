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

def getMakeMyTripFlights(fromplacecode, toplacecode,flights):
    # Settingup the browser and opening it
    print("working on makemytrip", fromplacecode, toplacecode)
    options = Options()
    #options.add_argument("headless")
    service = Service(executable_path = 'chromedriver.exe')
    browser = webdriver.Chrome(service = service, options = options)
    browser.maximize_window()
    browser.get('https://www.makemytrip.com/flights/')
    

    # settingup from and to places and clicking on search button
    #settingup the from value
    time.sleep(3)
    try:
        #browser.find_element(By.XPATH, '//*[@id="SW"]/div[1]/div[2]/div[2]').click()
        #webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
        browser.find_element(By.XPATH, '//*[@id="SW"]/div[1]/div[2]/div/div/nav/ul/li[1]/div').click()
    except:
        pass
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]').click()

    fromsearchbox = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input') # finding the from search box 
    fromsearchbox.send_keys(fromplacecode) # setting text in search box
    time.sleep(3)
    firstsearchresult = browser.find_element(By.XPATH, '//*[@id="react-autowhatever-1-section-0-item-0"]')
    firstsearchresult.click()
    
    tosearchbox = browser.find_element(By.XPATH, '//*[@id="toCity"]') #finding the tosearch box 
    tosearchbox.send_keys(toplacecode) # setting text in search box
    time.sleep(3)
    secondsearchresult = browser.find_element(By.XPATH, '//*[@id="react-autowhatever-1-section-0-item-0"]')
    secondsearchresult.click()
    
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/ul/li[1]').click()
    # clicking on search button
    browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/p/a').click()
    time.sleep(5)
    

    try: 
        while browser.find_element(By.XPATH, '//*[@id="fullpage-error"]/div/div/div/button'):
            browser.find_element(By.XPATH, '//*[@id="fullpage-error"]/div/div/div/button').click()
            time.sleep(1)
    except:
        pass
    time.sleep(5)
        

    try:
        browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/span').click()
    except:
        pass 
    
    browser.execute_script("window.scrollTo(0, 100000);")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, 100000);")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, 100000);")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, 100000);")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, 100000);")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, 100000);")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, 100000);")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, 100000);")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, 100000);")
    time.sleep(5)
    
    list = browser.find_elements(By.CLASS_NAME, 'fli-list')
    for f in list:
            flightname = f.find_element(By.XPATH, './div[1]/div[2]/div[1]/div/p[1]').text
            flightnumber = f.find_element(By.XPATH, './div[1]/div[2]/div[1]/div/p[2]').text
            starttime = f.find_element(By.XPATH, './div[1]/div[2]/div[2]/label/div/div/div/div[1]/p[1]/span').text
            endtime = f.find_element(By.XPATH, './div[1]/div[2]/div[2]/label/div/div/div/div[3]/p[1]/span').text
            totaljourneytime = f.find_element(By.XPATH, './div[1]/div[2]/div[2]/label/div/div/div/div[2]/p').text
            totalstops = f.find_element(By.XPATH, './div[1]/div[2]/div[2]/label/div/div/div/div[2]/div/p').text
            price = f.find_element(By.XPATH, './div[1]/div[2]/div[4]/div/div/p').text
            flights.append(flight(flightname,flightnumber, starttime,endtime, totaljourneytime, totalstops, price))
    return flights


