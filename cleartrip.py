import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class flight:
    def __init__(self, flightname, starttime, endtime, totaljourneytime, totalstops, price):
        self.flightname = flightname
        self.starttime = starttime
        self.endtime = endtime
        self.totaljourneytime = totaljourneytime
        self.totalstops = totalstops
        self.price = price
    def __str__(self):
        return f"{self.flightname} {self.starttime} {self.endtime} {self.totaljourneytime} {self.totalstops} {self.price}"

def getClearTripFlights(fromplace, toplace, flights):
    print("working on cleartripflights")
    options = Options()
    #options.add_argument("headless")
    service = Service(executable_path = "chromedriver.exe")
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    browser.get("https://www.cleartrip.com/")
    time.sleep(4)
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    time.sleep(4)
    #setting up source place
    browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[1]/input').send_keys(fromplace)
    time.sleep(5)
    browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[1]/div[2]/ul/li').click()
    #setting up destination place
    browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[3]/input').send_keys(toplace)
    time.sleep(5)
    browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[3]/div[2]/ul/li').click()
    #clicking on search button
    browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[4]/div/div[2]').click()
        


    try: 
        while browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/button'):
            browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/button').click()
            time.sleep(1)
    except:
        pass
    time.sleep(5)
        

    time.sleep(10)
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

    # extracting flight data
    try:
        list = browser.find_elements(By.CLASS_NAME, "ow-tuple-container__details-a")
        del list[0]
        for f in list:
            try:
                flightname = f.find_element(By.XPATH, './div[1]/div/div/div[3]/p[1]').text
                starttime = f.find_element(By.XPATH, './div[2]/div/div[1]/p').text
                endtime = f.find_element(By.XPATH, './div[2]/div/div[3]/p').text
                totaljourneytime = f.find_element(By.XPATH, './div[2]/div/div[2]/p[1]').text
                totalstops = f.find_element(By.XPATH, './div[2]/div/div[2]/p[2]/div/p').text
                try: 
                    price = f.find_element(By.XPATH, './div[3]/div[2]/div/p[2]').text
                except:
                    price = f.find_element(By.XPATH, './div[3]/div[2]/div/p').text
                flights.append(flight(flightname, starttime,endtime, totaljourneytime, totalstops, price))
            except:
                pass
    except:
        pass
    return flights

