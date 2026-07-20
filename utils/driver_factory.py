from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def build_driver():
    options = Options()
    options.add_argument("--headless")              # GUI nahi hai CI mein
    options.add_argument("--no-sandbox")            # GitHub Actions ke liye zaroori
    options.add_argument("--disable-dev-shm-usage") # memory issue fix
    options.add_argument("--disable-gpu")           # headless mein GPU nahi chahiye
    options.add_argument("--window-size=1920,1080") # screenshot ke liye

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver