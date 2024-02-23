from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import ddddocr

chrome_options = Options()
chrome_options.add_argument('--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})
chrome_options.add_experimental_option("detach",True)
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://ticketplus.com.tw/order/c752489ad3e922cbd8943deccdd22696/f985a29962a5b0072d835d6e70190183')
driver.maximize_window()
time.sleep(2.2)
#driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div/div/div[3]/div[2]/div[2]/button').click()
#time.sleep(1)

'''account = driver.find_element(By.XPATH,'//*[@id="MazPhoneNumberInput-20_phone_number"]')
account.clear()
account.send_keys("0937058582")
password = driver.find_element(By.XPATH,'//*[@id="input-26"]')
password.clear()
password.send_keys("Qq940403")
driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[2]/div[1]/form/button/span').click()
time.sleep(2.7)'''

driver.execute_script("window.scrollBy(0,320)")
time.sleep(0.7)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div/main/div/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/button').click()
driver.execute_script("window.scrollBy(320,document.body.scrollHeight)")
time.sleep(0.7)

code = driver.find_element(By.XPATH,'//*[@id="input-52"]')
code.clear()
imgcode = driver.find_element(By.CLASS_NAME,'captcha-img')
imgcode.screenshot("code.png")
ocr = ddddocr.DdddOcr()
with open("code.png", "rb") as fp:
    image = fp.read()
catch = ocr.classification(image)
code.send_keys(catch)