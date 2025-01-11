from data import *
from locators import TestLocators

class TestsConstructorSection:

    def test_check_tabs(self, driver):
        driver.get(URL)

        locators = [
            TestLocators.CONSTRUCTOR_SAUCES,
            TestLocators.CONSTRUCTOR_BUN,
            TestLocators.CONSTRUCTOR_FILLINGS
        ]

        for locator in locators:
            driver.find_element(*locator).click()
            current_class = driver.find_element(*locator).get_attribute('class')
            assert "tab_tab_type_current" in current_class