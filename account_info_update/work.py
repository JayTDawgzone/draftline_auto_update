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

base_url = 'https://www.draftlinesmartsystem.com/Companies.aspx?id='
base_url2 = 'https://www.draftlinesmartsystem.com/locations.aspx?id='
df = pd.read_excel('emails_2020-01-23.xlsx')
# x = 0
for index, row in df.iterrows():



    accid = str(round(row['Account ID']))
    locid = str(round(row['location']))
    # address = row['Address']
    # city = row['City']
    # postal_code = row['Postal Code']
    # # phone_number = row['Phone Number']
    locname = row['msgDate']
    # zone = row['Zone']
    # area = row['Area']
    # custid = str(round(row['WW Cust ID']))
    # email = row['body']

    ############################
    #Pull up Accounts Page
    ###########################
    driver.implicitly_wait(60)
    url = base_url + accid
    driver.get(url)
    sleep(15)
    url = base_url2 + locid
    driver.get(url)
    sleep(15)


    # ############################
    # #Click add account button
    # ###########################
    # driver.find_element_by_class_name('addNew').click()
    # sleep(1)
    # driver.find_element_by_id('addNew_tbNameNew').send_keys(locname)
    # driver.find_element_by_id('addNew_tbGSANew').send_keys(zone)
    # driver.find_element_by_id('addNew_btnSaveAndEdit').click()
    # sleep(2)
    # acctid = driver.current_url.split('=',1)[1]
    # acctid = acctid.split('&',1)[0]
    # df.loc[index, 'Acct Id'] = acctid
    # df.to_excel('SAC_Send_Orders.xlsx')


    ############################
    #Click edit details button
    ###########################
    # driver.find_element_by_id('main_btnEditAccountOverview').click()
    # sleep(2)


    ############################
    #Enter in the desired information
    ###########################
    # driver.find_element_by_id('main_ExtraAttributes1_rptAttributes_tbAttrValue_3').clear()
    # driver.find_element_by_id('main_ExtraAttributes1_rptAttributes_tbAttrValue_3').send_keys(custid)
    # # driver.find_element_by_id('main_ExtraAttributes1_rptAttributes_tbAttrValue_0').clear()
    # # driver.find_element_by_id('main_ExtraAttributes1_rptAttributes_tbAttrValue_0').send_keys(area)
    # # driver.find_element_by_id('main_ExtraAttributes1_rptAttributes_tbAttrValue_1').clear()
    # # driver.find_element_by_id('main_ExtraAttributes1_rptAttributes_tbAttrValue_1').send_keys('sandra@huppsigns.com; cesar@huppdraft.com; nick@huppdraft.com')
    # # driver.find_element_by_id('main_ExtraAttributes1_rptAttributes_tbAttrValue_2').clear()
    # # driver.find_element_by_id('main_ExtraAttributes1_rptAttributes_tbAttrValue_2').send_keys(zone)
    # driver.find_element_by_id('main_ExtraAttributes1_rptAttributes_tbAttrValue_4').clear()
    # driver.find_element_by_id('main_ExtraAttributes1_rptAttributes_tbAttrValue_4').send_keys(email)
    # driver.find_element_by_id('main_btnSaveDetails').click()
    # driver.find_element_by_id('main_btnSaveDetails').click()
    # sleep(3)
    print(locid + " " + locname + " updated.", flush=True)


    # driver.find_element_by_class_name('gvImageTd').click()
    # driver.find_element_by_id('main_btnEditLocDetails').click()
    # sleep(5)
    # driver.find_element_by_id('main_tbAddress1').clear()
    # driver.find_element_by_id('main_tbAddress1').send_keys(address)
    # driver.find_element_by_id('main_tbCity').clear()
    # driver.find_element_by_id('main_tbCity').send_keys(city)
    # driver.find_element_by_xpath("//select[@name='ctl00$main$ddlState']/option[text()='California']").click()
    # driver.find_element_by_id('main_tbZip').clear()
    # driver.find_element_by_id('main_tbZip').send_keys(postal_code)
    # # driver.find_element_by_id('main_tbPhone').clear()
    # # driver.find_element_by_id('main_tbPhone').send_keys(postal_code)
    #
    # sleep(1)
    # driver.find_element_by_id('main_btnSaveLocationDetails').click()
    # sleep(8)
