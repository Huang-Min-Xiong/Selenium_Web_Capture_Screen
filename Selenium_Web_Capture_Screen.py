from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\user\chromedriver_win32\chromedriver.exe')
Web_url = 'https://www.google.com/'
driver.get(Web_url)
driver.save_screenshot(r'./Img.png')
