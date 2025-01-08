from selenium.webdriver.common.by import By


class TestLocators:
    # Кнопка перехода в личный кабинет
    PERSONAL_AREA = By.XPATH, '//p[text() = "Личный Кабинет"]'
    # Гиперссылка на окно регистрации
    REGISTRATION_HREF = By.XPATH, '//*[@href = "/register"]'
    # Поле ввода "Имя"
    NAME_FIELD = By.XPATH, '(//input[@type = "text"])[1]'
    # Поле ввода "Email" при регистрации
    EMAIL_FIELD_REG = By.XPATH, '(//input[@type = "text"])[2]'
    # Поле ввода "Email"
    EMAIL_FIELD = By.XPATH, '//input[@type = "text"]'
    # Поле ввода "Пароль"
    PASSWORD_FIELD = By.XPATH, '//input[@type = "password"]'
    # Кнопка "Зарегистрироваться"
    REGISTRATION_BUTTON = By.XPATH, '//button[text() = "Зарегистрироваться"]'
    # Подпись "Некорректный пароль"
    INCORRECT_PASSWORD = By.XPATH, '//p[text() = "Некорректный пароль"]'
    # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = By.XPATH, '//button[text() = "Войти в аккаунт"]'
    # Кнопка "Войти" в форме ЛК
    LOGIN_BUTTON_IN_PA = By.XPATH, '//button[text() = "Войти"]'
    # Гиперссылка на окно входа в ЛК
    LOGIN_XREF = By.XPATH, '//*[@href = "/login"]'
    # Гиперссылка на окно восстановления пароля
    FORGOT_PASSWORD_XREF = By.XPATH, '//*[@href = "/forgot-password"]'
    # Кнопка "Оформить заказ"
    ORDER_BUTTON = By.XPATH, '//button[text() = "Оформить заказ"]'
    # Логотип
    LOGO = By.XPATH, '//div[contains(@class, "AppHeader_header__logo")]'
    # Кнопка перехода в конструктор
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text() = "Конструктор"]'
    # Вкладка "Булки"
    CONSTRUCTOR_BUN = By.XPATH, '//span[text() = "Булки"]'
    # Вкладка "Соусы"
    CONSTRUCTOR_SAUCES = By.XPATH, '//span[text() = "Соусы"]'
    # Вкладка "Начинки"
    CONSTRUCTOR_FILLINGS = By.XPATH, '//span[text() = "Начинки"]'
    # Кнопка "Выход"
    LOGOUT_BUTTON = By.XPATH, '//*[text() = "Выход"]'