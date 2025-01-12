from data import *
from locators import TestLocators

class TestsConstructorSection:

    def test_check_sauces_tab(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES).click()
        current_class = driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES).get_attribute('class')
        assert "tab_tab_type_current" in current_class

    def test_check_filling_tab(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.CONSTRUCTOR_FILLINGS).click()
        current_class = driver.find_element(*TestLocators.CONSTRUCTOR_FILLINGS).get_attribute('class')
        assert "tab_tab_type_current" in current_class

    def test_check_bun_tab(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUN).click()
        current_class = driver.find_element(*TestLocators.CONSTRUCTOR_BUN).get_attribute('class')
        assert "tab_tab_type_current" in current_class