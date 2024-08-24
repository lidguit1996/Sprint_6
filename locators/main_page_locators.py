from selenium.webdriver.common.by import By


class QuestionLocators:
    HOW_MUCH_QUESTION = (By.XPATH, ".//*[contains(text(), 'Сколько это стоит')]")
    WANT_MORE_SCOOTERS_QUESTION = (By.XPATH, ".//*[contains(text(), 'Хочу сразу несколько')]")
    TIME_CALCULATION_QUESTION = (By.XPATH, ".//*[contains(text(), 'время аренды')]")
    ORDER_TODAY_QUESTION = (By.XPATH, ".//*[contains(text(), 'прямо на сегодня')]")
    ORDER_EXTEND_QUESTION = (By.XPATH, ".//*[contains(text(), 'продлить заказ или вернуть')]")
    CHARGE_QUESTION = (By.XPATH, ".//*[contains(text(), 'зарядку вместе с самокатом')]")
    ORDER_CANCELLATION_QUESTION = (By.XPATH, ".//*[contains(text(), 'отменить заказ')]")
    NOT_IN_MOSCOW_QUESTION = (By.XPATH, ".//*[contains(text(), 'жизу за МКАДом')]")


class AnswersLocators:
    HOW_MUCH_ANSWER = (By.XPATH, ".//p[contains(text(), 'Сутки — 400 рублей')]")
    WANT_MORE_SCOOTERS_ANSWER = (By.XPATH, ".//p[contains(text(), 'один заказ — один самокат')]")
    TIME_CALCULATION_ANSWER = (By.XPATH, ".//p[contains(text(), 'Отсчёт времени аренды начинается с момента')]")
    ORDER_TODAY_ANSWER = (By.XPATH, ".//p[contains(text(), 'начиная с завтрашнего дня')]")
    ORDER_EXTEND_ANSWER = (By.XPATH, ".//p[contains(text(), 'всегда можно позвонить в поддержку')]")
    CHARGE_ANSWER = (By.XPATH, ".//p[contains(text(), 'к вам с полной зарядкой')]")
    ORDER_CANCELLATION_ANSWER = (By.XPATH, ".//p[contains(text(), 'пока самокат не привезли')]")
    NOT_IN_MOSCOW_ANSWER = (By.XPATH, ".//p[contains(text(), 'И Москве, и Московской области')]")


class OrderButtons:
    HEADER_ORDER_BUTTON = (By.XPATH, ".//button[@class = 'Button_Button__ra12g']")
    ORDER_BUTTON = (By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_UltraBig__UU3Lp']")

class Others:
    YANDEX_LOGO = (By.XPATH, ".//img[@alt = 'Yandex']")
    MAIN_TITLE = (By.XPATH, ".//*[contains(text(), 'Привезём его прямо к вашей двери,')]")


