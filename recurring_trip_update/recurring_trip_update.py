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

base_url = 'https://www.draftlinesmartsystem.com/ReccuringTrips.aspx?id='
df = pd.read_excel('recurring_trips.xlsx')
for index, row in df.iterrows():

    tripID = str(round(row['Trip ID']))
    title = row['Correct Name']
    start = row['Correct Start Time']
    end = row['Correct End Time']

    ############################
    #Updates Trip Title
    ###########################
    url = base_url + tripID
    driver.get(url)
    driver.find_element_by_id('main_tbTitle').clear()
    driver.find_element_by_id('main_tbTitle').send_keys(title)


    ############################
    #Changes Time Field
    ###########################

    driver.find_element_by_id('main_tbTimeFrom').clear()
    driver.find_element_by_id('main_tbTimeTo').clear()
    driver.execute_script("document.getElementById('main_tbTimeFrom').value = " + "'" + start + "'" + ";");
    driver.execute_script("document.getElementById('main_tbTimeTo').value = " + "'" + end + "'" + ";");


    driver.find_element_by_id('main_btnSave').click()
    driver.find_element_by_id('main_btnSave').click()
    sleep(4)

    ############################
    #If Warning, Click Save
    ###########################


    try:
        driver.find_element_by_xpath('//*[@onclick="saveRecuringTrip(false, true);"]').click()
        sleep(4)
    except:
        sleep(1)

    print(tripID + " " + title + " updated.")
