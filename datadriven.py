import XLUtlis
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
s=Service(r"C:\Users\lenovo\chrome driver\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
path="C:\\Users\\lenovo\\xl\\test1.xlsx"
rows=XLUtlis.getRowCount(path,"Sheet1")
for i in range(2,rows+1):
    username=XLUtlis.readData(path,"Sheet1",i,1)
    passward=XLUtlis.readData(path,"Sheet1",i,2)
    driver.find_element(By.NAME,"userName").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(passward)

    driver.find_element(By.NAME, "submit").click()
    print(driver.title)
    if driver.title=="Login: Mercury Tours":
        print("test case pass")
        XLUtlis.writeData(path,"Sheet1",i,3,"test passed")
    else:
        print('test failed')
        XLUtlis.writeData(path,"Sheet1",i,3,"test failed")
    driver.find_element(By.LINK_TEXT,"Home").click()