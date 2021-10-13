from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://demoqa.com/alerts')
driver.implicitly_wait(10)
# singgel button
# driver.find_element_by_id('alertButton').click()
# driver.switch_to.alert.accept()

# --------------------------Alert 2 ------------------------------------

# driver.find_element_by_id('confirmButton').click()
# driver.switch_to.alert.dismiss()

# --------------- Alert 3 ------------------

driver.find_element_by_xpath('//*[@id="promtButton"]').click()
# time.sleep(2)
# driver.switch_to.alert.send_keys("percobaan automation")
# time.sleep(2)
# driver.switch_to.alert.accept()
