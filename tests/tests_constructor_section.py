from data import *
from locators import TestLocators


class TestsConstructorSection:

    def test_section_bun(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUN).click()
        assert driver.find_element(*TestLocators.CONSTRUCTOR_BUN).text == "Булки"

    def test_section_sauces(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES).click()
        assert driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES).text == "Соусы"

    def test_section_fillings(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.CONSTRUCTOR_FILLINGS).click()
        assert driver.find_element(*TestLocators.CONSTRUCTOR_FILLINGS).text == "Начинки"