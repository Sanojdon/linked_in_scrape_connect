from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from parsel import Selector
import selenium_trial
import csv
driver = selenium_trial.driver
driver.maximize_window()

sleep(0.5)
driver.get("https://www.google.com/")
sleep(2)

writer = csv.writer(open(selenium_trial.parameters.result, "w"))
writer.writerow(["Name", "Designation", "Schools", "Location", "LinkedIn URL"])

search_query = driver.find_element_by_xpath("//input[@name='q']")
search_query.send_keys(selenium_trial.parameters.search_query)
search_query.send_keys(Keys.RETURN)

profiles = driver.find_elements_by_xpath("//*[@class='rc']/div/a")
profiles = [profile.get_attribute('href') for profile in profiles]

for profile in profiles:
    driver.get(profile)
    sleep(5)

    sel = Selector(text=driver.page_source)

    check_available = sel.xpath("//div[@class='profile-unavailable']/h1/text()")
    if check_available:
        continue
    name = sel.xpath("//title/text()").extract_first().split(" | ")[0]
    job = sel.xpath("//h2/text()").extract()[2].strip()
    schools = sel.xpath("//*[contains(@class, 'pv-entity__school-name')]/text()").extract()
    location = sel.xpath("//h2/following-sibling::ul/li/text()").extract()[16].strip()
    ln_url = driver.current_url

    print("\n")
    print(ln_url)
    print(name)
    print(job)
    print(schools)
    print(location)
    print("\n")
    writer.writerow([name, job, schools, location, ln_url])
    try:
        driver.find_element_by_xpath("//*[text()='More…']").click()
        sleep(1)
    except Exception as e:
        pass

    driver.find_element_by_xpath("//*[text()='Connect']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[text()='Done']").click()
    sleep(2)


driver.quit()
