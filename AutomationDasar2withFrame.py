from selenium import webdriver
import time
import pyautogui
driver = webdriver.Chrome()
# menunggu windows 10 detik jika internet lemot biasanya
driver.implicitly_wait(10)
# driver.get("https://jqueryui.com/datepicker/")

# # jika melakukan tes seperti datepicker atau lainnya chek apakah
# # masuk di dalam frame atau tidak jika iya lakukan sprt berikut

# driver.switch_to.frame(driver.find_element_by_xpath(
#     '/html/body/div[1]/div[2]/div/div[1]/iframe'))
# driver.find_element_by_id("datepicker").click()
# driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[4]/a').click()
# time.sleep(2)
# driver.find_element_by_id('datepicker').send_keys('02/08/1996')
# driver.find_element_by_id('datepicker').clear()
# time.sleep(3)
# driver.find_element_by_id('datepicker').send_keys('01/08/1996 ')
# ------------------------------- bagian beda --------------------------------

driver.get('https://demoqa.com/date-picker/')

driver.find_element_by_id("datePickerMonthYearInput").click()
# ini digunakan untuk menghapus kolom defaul gambar dengan backspacee auto sebanyak 10x dngan import liblary pyautogui
pyautogui.press('backspace', presses=10)
time.sleep(3)
driver.find_element_by_id("datePickerMonthYearInput").send_keys('02/08/1996')
