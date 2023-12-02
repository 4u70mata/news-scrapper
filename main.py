######################################################################
#             [ AUTOMATED SPORT NEWS WEB SCRAPPING ]
#
# +[ News headline from ] < https://www.thesun.co.uk/sport/football/ >
#
######################################################################
import os
import sys
from datetime import datetime

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd 
from collections import defaultdict




# settings :: urls, paths and dates
app_path = os.path.dirname(sys.executable)
today = datetime.now().strftime("(%m-%d-%Y)") # today 

website = 'https://www.thesun.co.uk/sport/football/'
path = 'C:/Users/ADMIN/Documents/automation-projects/football-headlines/chromedriver.exe' 


#Add Headless Options + Error logs opts... 
options = webdriver.ChromeOptions()

options.add_argument("--headless=new")
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#Usb log errors ...







############################# START ###################################
service = Service(executable_path=path) 
driver = webdriver.Chrome(service = service, options = options)




try:
    # GET WEBSITE
    driver.get(website)
    containers = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class = "teaser__copy-container"]'))
    )
    # containers = driver.find_elements(by= "xpath", value='//div[@class = "teaser__copy-container"]')


    dict_ = defaultdict(list) 
    for container in containers:

        title = container.find_element(by="xpath", value='./a/span').text
        subtitle = container.find_element(by="xpath", value='./a/h3').text
        link = container.find_element(by="xpath", value='./a').get_attribute("href")
        dict_['title'].append(title)
        dict_['subtitle'].append(subtitle)
        dict_['links'].append(link)

    #Store in DataFrame : 
    df_headlines = pd.DataFrame(dict_)
    csv_ = f'{app_path}/headline-{today}.csv'
    df_headlines.to_csv(os.path.join(app_path, csv_))

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()



