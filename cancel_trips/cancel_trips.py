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

base_url = 'https://www.draftlinesmartsystem.com/trips.aspx?id='
df = pd.read_excel('cancel.xlsx')

for index, row in df.iterrows():

    tripID = str(row['tripId'])
    url = base_url + tripID
    ############################
    #Updates Trip Title
    ###########################
    driver.get(url)
    driver.find_element_by_id('main_cntSurvey_aCancelTrip').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@name="ctl00$main$cntSurvey$tbCancelReason"]').send_keys('Duplicate Trip')
    driver.find_element_by_id('main_cntSurvey_btnSetTripStatus').click()
    sleep(3)
    print(tripID + " canceled.")
