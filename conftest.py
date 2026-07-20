from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # Start browser maximized
    options.add_argument("--start-maximized")

    # Uncomment if you want the browser to stay open after the script ends
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)

    yield driver

    # Close browser after test
    driver.quit()