from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


browser = webdriver.Chrome(executable_path = 'chromedriver.exe')
browser.get('https://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.htm')
list = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'XYZ']

f = open("Airport_list.txt", "w")

num = 2
counter = 1
for cha in list:
    while True:
        try:
            browser.find_element(By.XPATH, '//*[@id="{}"]/div/table/tbody/tr[{}]'.format(cha, num))         
        except NoSuchElementException:
            break
        city = browser.find_element(By.XPATH, '//*[@id="{}"]/div/table/tbody/tr[{}]/td[1]'.format(cha, num)).text
        country = browser.find_element(By.XPATH, '//*[@id="{}"]/div/table/tbody/tr[{}]/td[2]'.format(cha, num)).text
        IATA = browser.find_element(By.XPATH, '//*[@id="{}"]/div/table/tbody/tr[{}]/td[3]'.format(cha, num)).text
        newcity = ""
        for char in city:
            val = ord(char)
            if((96<val and val<123) or (64<val and val<91) or val==32):
                newcity += chr(val)
            else:
                if newcity[-1] == ' ':
                    city = newcity[0:-1]
                else:
                    city = newcity
                break
        print(str(counter) + "  {}, {}, {}".format(city.lower(), country, IATA))
        f.write("{}, {}\n".format(city.lower(), IATA))
        num+=1
        counter += 1
    num = 3






  
