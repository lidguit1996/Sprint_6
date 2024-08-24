from selenium.webdriver.common.by import By


class AboutOrderPageLocators:
    DATE_FIELD = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']")
    DATE_1 = (By.XPATH, ".//div[contains(text(), '28')]")
    DATE_2 = (By.XPATH, ".//div[contains(text(), '29')]")
    ORDER_PERIOD_FIELD = (By.XPATH, ".//div[contains(text(), '* Срок аренды')]")
    TWO_DAYS = (By.XPATH, ".//*[contains(text(), 'двое суток')]")
    THREE_DAYS = (By.XPATH, ".//*[contains(text(), 'трое суток')]")
    BLACK_COLOUR = (By.XPATH,".//input[@id = 'black']")
    GREY_COLOUR = (By.XPATH, ".//input[@id = 'grey']")
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']")
    SUBMIT_ORDER_BUTTON = (By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Да')]")

    SUCCESS_ORDER_WINDOW = (By.XPATH, ".//*[contains(text(), 'Заказ оформлен')]")
