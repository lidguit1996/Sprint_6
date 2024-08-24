from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_FIELD = (By.XPATH, ".//input[@placeholder = '* Имя']")
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    SUBWAY_STATION_FIELD = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    SOKOLNIKI_STATION = (By.XPATH, ".//*[contains(text(), 'Сокольники')]")
    LUBIANKA_STATION = (By.XPATH, ".//*[contains(text(), 'Лубянка')]")
    PHONE_NUMBER_FIELD = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Далее')]")
    SCOOTER_LOGO = (By.XPATH, ".//img[@alt = 'Scooter']")




