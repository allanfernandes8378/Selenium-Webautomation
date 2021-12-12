
from selenium import webdriver
import openpyxl  #pip install openpyxl

#https://www.selenium-tutorial.com/blog/184444/selenium-python-tutorial-excel-reading-pyxl


#Provide sheet path to a variable(path)
path = "G:\\newexcel.xlsx"
#Load the Sheet
wb = openpyxl.load_workbook(path)
sheet = wb.active


#Make changes in the R1,C1 of the sheet
#Read value
x = sheet.cell(1,1)
#change value
x.value = "apple"
#Save the sheet 
wb.save("G:\\newexcel.xlsx")






