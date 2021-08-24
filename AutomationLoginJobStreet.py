from selenium import webdriver
import selenium
import time

driver = webdriver.Chrome()
driver.get("https://www.jobstreet.co.id/")
time.sleep(2)
# mengklik class name masuk/login pada halaman utama
driver.find_element_by_class_name('GIz8i_0').click()
time.sleep(1)
# memasukan email dan password yang sudah terdaftar
driver.find_element_by_id('login_id').send_keys('youremail@gmail.com')
time.sleep(1)
driver.find_element_by_id('password').send_keys('yourpassword')
time.sleep(1)
# harus chek bagian remember account apakah ingin di remember atau tidak jika tidak
# dapat menggunakan sintak remember dibawah ini
driver.find_element_by_id('remember').click()
time.sleep(1)
# klik button login
driver.find_element_by_id('btn_login').click()
