# pip install selenium
from selenium import webdriver
import time



class Control:
    def __init__(self):
        self.username = "seleniumogretmen1@gmail.com"
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://panel.kodris.com/login")

        try:
            assert "Kodris" in self.driver.title
        except AssertionError  :
            print("Hatali Web Sitesi")

        usernameInput = self.driver.find_element_by_name("username")
        usernameInput.send_keys(self.username)

        passwordInput = self.driver.find_element_by_name("password")
        passwordInput.send_keys(self.username)

        loginButton = self.driver.find_element_by_id("loginBtn")
        loginButton.click()

        time.sleep(4)   

    def checkProfile(self):
        self.driver.get("https://panel.kodris.com/home#profile/profile/general")
        time.sleep(4)

        usernameInputProfile = self.driver.find_element_by_name("username")
        usernameProfile = usernameInputProfile.get_attribute('value')

        try:
            assert usernameProfile  == self.username
        except AssertionError  :
            print("Yanlis Kulanici Ismi")



control = Control() # Control classindan bir obje olusturuluyor
control.login() # Control classindan login metodu() cagriliyor
control.checkProfile() # Control classindan checkProfile() metodu cagriliyor
