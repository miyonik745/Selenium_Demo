# pip install selenium
from selenium import webdriver
import time

# ----------------------- Kurulum -----------------------------------
username = "seleniumogretmen1@gmail.com"
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()


# --------------------------------------------------------------------
# --------------------------- Login ----------------------------------
driver.get("https://panel.kodris.com/login")
time.sleep(2)

if "Kodris" in driver.title:
    print("Login Sayfasi Acildi")

usernameInput = driver.find_element_by_name("username")
usernameInput.send_keys(username)

passwordInput = driver.find_element_by_name("password")
passwordInput.send_keys(username)

loginButton = driver.find_element_by_id("loginBtn")
loginButton.click()

time.sleep(4)   


# -----------------------------------------------------------------------
# ---------------------------- Panel ------------------------------------
driver.get("https://panel.kodris.com/home#profile/profile/general")
time.sleep(4)

usernameInputProfile = driver.find_element_by_name("username")
usernameProfile = usernameInputProfile.get_attribute('value')

if usernameProfile  == username:
    print("Kullanici Ismi Dogru")

driver.quit()
