from selenium import webdriver as wb
from time import sleep
import pandas as pd


# username = input("Draftline Username: ")
# password = input("Draftline Password: ")

############################
#Open Draftline & Log In
###########################
driver = wb.Chrome()
driver.get("https://www.draftlinesmartsystem.com")
driver.find_element_by_id('main_LoginBox_tbEmail').send_keys('Terra@huppsigns.com')
driver.find_element_by_id('main_LoginBox_tbPassword').send_keys('Hupp123')
driver.find_element_by_id('main_LoginBox_btnLogin').click()



############################
#Set base url
#Read XLSX file to data frame
#Itterate through rows of dataframe and perform actions for each row
###########################

base_url = 'https://www.draftlinesmartsystem.com/ReccuringTrips.aspx?id='
df = pd.read_excel('cv_routes.xlsx')
for index, row in df.iterrows():

    tripID = str(round(row['TripID']))
    title = row['Rte']
    start = str(row['Start Time'])
    end = str(row['End Time'])
    primary = row['Primary Tech']
    secondary = str(row['Secondary Tech'])
    date = row['Effective Date']
    dateChange = row['Date Change']
    techChange = row['Tech Change']

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

    ############################
    #Changes Date Field
    ###########################

    if dateChange == 'x':
        driver.find_element_by_id('main_tbFromDate').clear()
        driver.execute_script("document.getElementById('main_tbFromDate').value = " + "'" + date + "'" + ";");


    ############################
    #Remove Old Technician
    ###########################
    if techChange == 'x':
        
        if secondary != 'nan':
            print(secondary)
            print(type(secondary))
            driver.find_element_by_xpath("//a[@title=\"Remove Technician\"]").click()
            sleep(3)
            driver.find_element_by_xpath("//a[@title=\"Remove Technician\"]").click()
            sleep(3)
            driver.find_element_by_id('main_tbTechniciansAutCompl').send_keys(primary)
            sleep(3)
            driver.find_element_by_link_text(primary).click()
            sleep(3)
            driver.find_element_by_id('main_tbTechniciansAutCompl').clear()
            driver.find_element_by_id('main_tbTechniciansAutCompl').send_keys(secondary)
            sleep(3)
            driver.find_element_by_link_text(secondary).click()

        else:
            sleep(2)
            driver.find_element_by_xpath("//a[@title=\"Remove Technician\"]").click()
            sleep(3)
            try:
                driver.find_element_by_xpath("//a[@title=\"Remove Technician\"]").click()
                sleep(3)
            except:
                print("No Second Tech to Remove")

            driver.find_element_by_id('main_tbTechniciansAutCompl').send_keys(primary)
            sleep(3)
            driver.find_element_by_link_text(primary).click()
            sleep(3)



    sleep(2)
    # driver.find_element_by_id('main_btnSave').click()
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
