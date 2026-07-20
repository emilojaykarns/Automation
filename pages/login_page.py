from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.username_field = (By.XPATH, "//*[@id='root']/div/div[2]/form/div[1]/input")
        self.password_field = (By.XPATH, "//*[@id='root']/div/div[2]/form/div[2]/input")
        self.login_button = (By.XPATH, "//*[@id='root']/div/div[2]/form/button")

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.wait.until(
            EC.visibility_of_element_located(self.username_field)
        ).send_keys(username)

        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_logged_in(self):
        self.wait.until(
            lambda driver: driver.current_url != "https://stage.emilo.in/login"
        )

        print("Current URL:", self.driver.current_url)

        return self.driver.current_url != "https://stage.emilo.in/login"