from selenium import webdriver
import selenium
import time

driver = webdriver.Chrome()

# driver.get("https://the-internet.herokuapp.com/login")
# driver.find_element_by_id("username").send_keys('Gagah')
# driver.find_element_by_name("password").send_keys('1234')
# driver.find_element_by_class_name('radius').click()
# driver.find_element_by_css_selector("button.radius").click()
# driver.find_element_by_css_selector('#login > button').click()

# berdasarkan kata yang ada didalam tag html yang di jadikan link
# driver.find_element_by_partial_link_text("Elemental").click()

# untuk bagian xpath dibawah ini perharikan kutip karena terdapat 2 kutip berbeda untuk
# digunakan
# driver.find_element_by_xpath('//*[@id="login"]/button').click()
# -----------------------------------------------------------------------------------

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
# time sleep di gunakan untuk di bawah link tujuan agar berjalan sesuai
time.sleep(3)
# diambil dengan copy -> selector
driver.find_element_by_css_selector("#content > div > button").click()
