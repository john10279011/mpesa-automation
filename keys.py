from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

username = "kariukiamschel9@gmail.com"
password = "@iamLehcsma9"


driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://developer.safaricom.co.ke/"
wait = driver.implicitly_wait(5)

driver.get(url)

time.sleep(1)
# removing dialog-box
wait
wait

driver.find_element_by_xpath(
    "//button[contains(@class,'v-btn v-btn--is-elevated v-btn--has-bg v-btn--rounded theme--light v-size--default primary')]"
).click()

# clicking the login button
driver.find_element_by_xpath(
    "//button[contains(@class,'v-btn v-btn--is-elevated v-btn--has-bg v-btn--rounded theme--light v-size--large primary')]"
).click()

# adding login details

driver.find_element_by_xpath("//input[contains(@name,'email')]").send_keys(username)
driver.find_element_by_xpath("//input[contains(@name,'password')]").send_keys(password)

driver.implicitly_wait(2)
time.sleep(0.2)
driver.find_element_by_xpath(
    "//button[contains(@class,'v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--small primary')]"
).click()

time.sleep(5)
items = driver.find_elements_by_xpath(
    "//div[contains(@class,'col-sm-6 col-md-4 col-lg-3 col-xl-2 col-12')]"
)
print(len(items))

driver.close()
