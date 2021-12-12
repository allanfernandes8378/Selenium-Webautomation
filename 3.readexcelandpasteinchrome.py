from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

#Open Chrome using webdriver, install chocolatey, selenium,chrome webdriver(Gecko for Mozilla)
driver = webdriver.Chrome()
#implicit wait
driver.implicitly_wait(0.5)
#maximize browser
driver.maximize_window()

#Provide sheet path to a variable(path)
path = "G:\\newexcel.xlsx"
#Load the Sheet
wb = openpyxl.load_workbook(path)
sheet = wb.active
#copy the value
x = sheet.cell(1,1)
a = x.value

#Get request for a URL
driver.get('https://www.google.com/')

#Search the required element using id/xpath/class/etc
searchbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

searchbox.send_keys(a)
#Enter
driver.implicitly_wait(2)
searchbox.submit()

