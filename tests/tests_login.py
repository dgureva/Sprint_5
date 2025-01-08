from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *
from locators import TestLocators


class TestsLogin:

    def test_login_on_main_page(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_PA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.current_url == URL

    def test_login_use_pa_button(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_PA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.current_url == URL

    def test_login_on_registration_form(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_HREF)).click()
        driver.find_element(*TestLocators.LOGIN_XREF).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_PA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.current_url == URL

    def test_login_on_forgot_password_form(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.FORGOT_PASSWORD_XREF)).click()
        driver.find_element(*TestLocators.LOGIN_XREF).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_PA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.current_url == URL