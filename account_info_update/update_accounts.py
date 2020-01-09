from selenium import webdriver as wb
from time import sleep
import pandas as pd



username = input("Draftline Username: ")
password = input("Draftline Password: ")

############################
#Open Draftline & Log In
###########################
driver = wb.Chrome()
driver.get("https://www.draftlinesmartsystem.com")
driver.find_element_by_id('main_LoginBox_tbEmail').send_keys(username)
driver.find_element_by_id('main_LoginBox_tbPassword').send_keys(password)
driver.find_element_by_id('main_LoginBox_btnLogin').click()

############################
#Set base url
#Read XLSX file to data frame
#Itterate through rows of dataframe and perform actions for each row
###########################

base_url = 'https://www.draftlinesmartsystem.com/locations.aspx?id='
df = pd.read_excel('proper_locations.xlsx')
# x = 0
for index, row in df.iterrows():



    locid = str(round(row['LocationID']))
    locname = row['Location']
    address = row['Proper Address']
    city = row['Proper City']

    ############################
    #Pull up location
    ###########################
    url = base_url + locid
    driver.get(url)
    ############################
    #Click edit details button
    ###########################
    driver.find_element_by_id('main_btnEditLocDetails').click()
    driver.implicitly_wait(60)
    sleep(8)
    ############################
    #Enter in the desired information
    ###########################
    driver.find_element_by_id('main_tbAddress1').clear()
    driver.find_element_by_id('main_tbAddress1').send_keys(address)
    driver.find_element_by_id('main_tbCity').clear()
    driver.find_element_by_id('main_tbCity').send_keys(city)
    driver.find_element_by_id('main_btnSaveLocationDetails').click()
    sleep(12)
    driver.implicitly_wait(60)
    print(locid + " " + locname + " updated.")
