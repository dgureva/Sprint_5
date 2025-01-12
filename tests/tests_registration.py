from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *
from locators import TestLocators
from conftest import driver
import random


# Функция для генерации случайного email
def generate_random_email():
    random_number = random.randint(0, 999999)
    return f"{random_number}@ya.ru"


class TestsRegistration:
    def test_registration_true(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_HREF)
        ).click()

        random_email = generate_random_email()

        driver.find_element(*TestLocators.NAME_FIELD).send_keys(NAME)
        driver.find_element(*TestLocators.EMAIL_FIELD_REG).send_keys(random_email)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_IN_PA))
        assert driver.current_url == LOGIN_WINDOW_URL


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
