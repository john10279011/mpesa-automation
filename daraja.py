from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# login details
fName = input("what's your First name ")  # fName = "john"
sName = input("what's your second name ")  # sName = "Mukundi"
email = input("enter email number ")  # email = "johnmukundi@gmail.com"
username = input("prompt your preffered username ")  # username = "jmukundi"
phonenumber = input("enter your mobile number")  # phonenumber = 12344444

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

pnumber = driver.find_element_by_xpath(
    "//input[contains(@name,'telephone')]"
).send_keys(phonenumber)


atype = driver.find_element_by_xpath(
    '//*[@id="app"]/div[5]/div/div/div/form/div/div[6]/div/div/div[1]/div[2]/div[1]'
)
select = Select(atype)
select.select_by_visible_text("Individual")


# checkbox = driver.find_element_by_xpath('//*[@id="input-165"]').click()
