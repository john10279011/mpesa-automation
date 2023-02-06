from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://developer.safaricom.co.ke/"
wait = driver.implicitly_wait(5)


pas = input("Do you have a safaricom daraja a/c? (choose y/n)")


if pas == "y":
    # proceed to login
    username = input("enter your username details")
    password = input("enter your password")

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
    driver.find_element_by_xpath("//input[contains(@name,'password')]").send_keys(
        password
    )

    driver.implicitly_wait(2)
    time.sleep(0.2)
    driver.find_element_by_xpath(
        "//button[contains(@class,'v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--small primary')]"
    ).click()

    # creating a new project

    driver.find_element_by_xpath(
        "//button[contains(@class,'mt-3 v-btn v-btn--outlined theme--light v-size--default primary--text')]"
    ).click()
    wait

    driver.find_element_by_xpath("//input[contains(@name,'AppName')]").send_keys(
        "amschel1"
    )

    driver.find_element_by_xpath(
        "(//div[contains(@class,'v-input--selection-controls__ripple')])[2]"
    ).click()

    driver.find_element_by_xpath(
        "//button[contains(@class,'mt-4 v-btn v-btn--block v-btn--is-elevated v-btn--has-bg theme--light v-size--small primary')]"
    ).click()


elif pas == "n":
    # create acc
    pass

else:
    print("choose between y and n")
