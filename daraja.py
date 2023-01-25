from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# login details
fName = input("what's your First name ")
sName = input("what's your second name ")
email = input("enter email number ")
username = input("prompt your preffered username ")

# website url and webdriver definition
url = "https://developer.safaricom.co.ke/"
driver = webdriver.Chrome(ChromeDriverManager().install())


# login
driver.get(url)
driver.find_element_by_xpath(
    "//button[contains(@class,'v-btn v-btn--is-elevated v-btn--has-bg v-btn--rounded theme--light v-size--default primary')]"
).click()


login_btn = driver.find_element_by_xpath(
    "//button[contains(@class,'v-btn v-btn--is-elevated v-btn--has-bg v-btn--rounded theme--light v-size--large primary')]"
).click()

driver.implicitly_wait(2)

# create accounts
sign_up_btn = driver.find_element_by_xpath(
    "//button[contains(@class,'v-btn v-btn--outlined theme--light v-size--default primary--text')]"
).click()


fname = driver.find_element_by_xpath("//input[contains(@name,'FirstName')]").send_keys(
    fName
)

sname = driver.find_element_by_xpath("//input[contains(@name,'LastName')]").send_keys(
    sName
)

Email = driver.find_element_by_xpath(
    "//input[contains(@name,'EmailAddress')]"
).send_keys(email)

usrname = driver.find_element_by_xpath("//input[contains(@name,'Username')]").send_keys(
    username
)
