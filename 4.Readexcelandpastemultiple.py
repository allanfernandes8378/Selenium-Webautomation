from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

path = "G:\\newexcel.xlsx"
wb = openpyxl.load_workbook(path)
sheet = wb.active

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.maximize_window()

#Copy 0 entries from the first column and google search

z = 1
while (z<10):
    driver.get('https://www.google.com/')
    searchbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    cellvalue = sheet.cell(z,1).value
    searchbox.send_keys(cellvalue)
    searchbox.submit()
    z += 1


