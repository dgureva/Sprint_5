from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *
from locators import TestLocators


class TestsGoToConstructor:

    def test_go_to_constructor_from_pa(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_PA).click()
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CONSTRUCTOR_BUN))
        text_section = driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES).text
        assert text_section == "Соусы"

    def test_go_to_main_page_from_pa_logo_click(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_PA).click()
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.current_url == URL