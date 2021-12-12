from selenium import webdriver
from selenium.webdriver.common.by import By

#Open Chrome using webdriver, install chocolatey, selenium,chrome webdriver(Gecko for Mozilla)
driver = webdriver.Chrome()
#implicit wait
driver.implicitly_wait(0.5)
#maximize browser
driver.maximize_window()

#Get request for a URL
driver.get('https://www.google.com/')

#Search the required element using id/xpath/class/etc
searchbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

#Send the text to the selectd element
searchbox.send_keys("creative gladiators placement academy")
#Enter
searchbox.submit()