from selenium import webdriver
import selenium
import time

driver = webdriver.Chrome()

driver.get("https://www.jobstreet.co.id/")
time.sleep(2)
driver.find_element_by_id('searchKeywordsField').send_keys("Quality Assurance")
time.sleep(1)
driver.find_element_by_class_name("ZS3A5_0").click()
time.sleep(2)
driver.find_element_by_id("Select-0-508").click()
time.sleep(1)
driver.find_element_by_id('locationAutoSuggest').send_keys("Jakarta")
time.sleep(1)
driver.find_element_by_partial_link_text("Cari").click()
