from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *
from locators import TestLocators
from tests.conftest import driver


class TestsRegistration:

    def test_registration_password_incorrect(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_HREF)).click()
        driver.find_element(*TestLocators.NAME_FIELD).send_keys(NAME)
        driver.find_element(*TestLocators.EMAIL_FIELD_REG).send_keys(EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys("Daria")
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        text_error = driver.find_element(*TestLocators.INCORRECT_PASSWORD).text
        assert text_error == "Некорректный пароль"
        print(text_error)

    def test_registration_true(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_HREF)).click()
        driver.find_element(*TestLocators.NAME_FIELD).send_keys(NAME)
        driver.find_element(*TestLocators.EMAIL_FIELD_REG).send_keys(EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        print("Регистрация успешна!")