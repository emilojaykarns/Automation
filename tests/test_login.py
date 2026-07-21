from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open("https://stage.emilo.in/login")
    login_page.login("jaykarns", "emilo@123#")
    assert login_page.is_logged_in()




def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open("https://stage.emilo.in/login")
    login_page.login("valid_user", "wrong_pass")
    assert not login_page.is_logged_in()