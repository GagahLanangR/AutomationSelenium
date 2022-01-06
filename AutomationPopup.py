from selenium import webdriver
import selenium
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
# webdriver expeceted_condition untuk menjalan printah pada halaman web dengan kondisi yang di harapkan
# webdriberwait itu untuk menunggu berapa lama waktu tunggu yang di ingin sampai kondisi yang dimau keluar
# TimeoutException untuk jenjang waktu habis selamawaktu tunggu biasanya di pakai di try except
# import by untuk mencari element tapi tidak menggunakan sintak find element by .....

driver = webdriver.Chrome()


driver.get('https://shopee.co.id/')

try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div/div[2]')))
    print('Pop up keluar')
    driver.find_element_by_class_name('shopee-popup__close-btn').click()
    print('Pop up di close')

except TimeoutException:
    print('tidak ada pop up')
    pass

driver.find_element_by_class_name('shopee-button-no-outline').click()
print('sudah klik halaman flash sale')
driver.find_element_by_class_name(
    'flash-sale-item-card__image-overlay flash-sale-item-card__image-overlay--landing-page _2GchKS').click()
print('Berhasil memilih item')
driver.find_element_by_class_name(
    'shopee-button-solid shopee-button-solid--primary ').click()
driver.find_element_by_class_name(
    'product-variation product-variation--selected').click()
driver.find_element_by_class_name('checkout-bank-transfer-item__title').click()
driver.find_element_by_class_name(
    'stardust-button stardust-button--primary stardust-button--large _1qSlAe').click()
