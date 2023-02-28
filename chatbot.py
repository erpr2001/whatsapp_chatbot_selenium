import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

jokes = ["You don't need a parachute to go skydiving. You need a parachute to go skydiving twice.",
        "Women call me ugly until they find out how much money I make. They they call me ugly and poor."]

options = Options()
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome('D:\\pythoninstaller\\chromedriver_win32\\chromedriver.exe', options=options)
driver.maximize_window()
driver.get('https://web.whatsapp.com')  # Already authenticated

time.sleep(20)

##################### Provide Recepient Name Here ###############################
driver.find_element_by_xpath("//*[@title='MyJakartaNumber']").click()

for joke in jokes:
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(joke)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
    time.sleep(10)

time.sleep(30)
driver.close()