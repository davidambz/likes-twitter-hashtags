from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import dotenv_values
import time

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

config = dotenv_values('.env')

driver.get(r"https://twitter.com/i/flow/login")

while(len(driver.find_elements(By.NAME, 'text'))) == 0:
    time.sleep(1)


driver.find_element(By.NAME, 'text').send_keys(config['TWITTER-USER'])
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()

while(len(driver.find_elements(By.NAME, 'password'))) == 0:
    time.sleep(1)

driver.find_element(By.NAME, 'password').send_keys(config['TWITTER-PASSWORD'])
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()

time.sleep(2)

driver.get(config['TWITTER-HASHTAG_URL'])

while(len(driver.find_elements(By.XPATH, '//div[@data-testid="like"]'))) == 0:
    time.sleep(1)

like_buttons = driver.find_elements(By.XPATH, '//div[@data-testid="like"]')
for like_button in like_buttons:
    like_button.click()