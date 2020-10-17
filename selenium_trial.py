from selenium import webdriver
from time import sleep
import parameters

driver = webdriver.Chrome(parameters.chromedriver_path)
driver.maximize_window()

sleep(0.5)
driver.get("https://www.linkedin.com/")
sleep(2)

driver.find_element_by_xpath("//a[text()='Sign in']").click()
sleep(3)

username_input = driver.find_element_by_name("session_key")
username_input.send_keys(parameters.username)
sleep(0.5)

username_password = driver.find_element_by_name("session_password")
username_password.send_keys(parameters.password)

driver.find_element_by_xpath("//button[text()='Sign in']").click()
sleep(5)
