import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username_field = (By.XPATH, "//*[@id='root']/div/div[2]/form/div[1]/input")
        self.password_field = (By.XPATH, "//*[@id='root']/div/div[2]/form/div[2]/input")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div[2]/form/button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located(self.username_field)).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

        # Dashboard pe pahunchne ke baad 30 second ruko
        time.sleep(30)

    def is_logged_in(self):
        return "inventory" in self.driver.current_url