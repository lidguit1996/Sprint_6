import allure
from data import Urls, OrderData
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.about_order_page import AboutOrderPage
from locators.main_page_locators import OrderButtons
from locators.order_page_locators import OrderPageLocators
from locators.about_order_page_locators import AboutOrderPageLocators
import pytest



@allure.title('Проверка флоу заказа самоката')
@allure.description('Поочередно делаем заказ самоката через обе кнопки "Заказать" с двумя разными данными заказчика и заказа')
class TestOrderFlow:

    yuriy_order = [OrderButtons.HEADER_ORDER_BUTTON,
         OrderData.NAME_1,
         OrderData.SURNAME_1,
         OrderData.ADDRESS_1,
         OrderPageLocators.SOKOLNIKI_STATION,
         OrderData.PHONE_NUMBER_1,
         AboutOrderPageLocators.DATE_1,
         AboutOrderPageLocators.TWO_DAYS,
         AboutOrderPageLocators.BLACK_COLOUR,
         OrderData.COMMENT_1
         ]

    ksenia_order = [OrderButtons.ORDER_BUTTON,
         OrderData.NAME_2,
         OrderData.SURNAME_2,
         OrderData.ADDRESS_2,
         OrderPageLocators.LUBIANKA_STATION,
         OrderData.PHONE_NUMBER_2,
         AboutOrderPageLocators.DATE_2,
         AboutOrderPageLocators.THREE_DAYS,
         AboutOrderPageLocators.GREY_COLOUR,
         OrderData.COMMENT_2
         ]

    @pytest.mark.parametrize('button, name, surname, address, subway, phone_number, date, period, colour, comment',[yuriy_order, ksenia_order])
    def test_order_flow(self, driver, button, name, surname, address, subway, phone_number, date, period, colour, comment):
        main_page = MainPage(driver)
        main_page.open_page(Urls.SCOOTER_MAIN)
        main_page.click_order_button(button)

        order_page = OrderPage(driver)
        order_page.enter_user_data(name, surname, address, subway, phone_number)
        order_page.click_next_button()

        about_order_page = AboutOrderPage(driver)
        about_order_page.set_about_order_data(date, period, colour, comment)
        about_order_page.submit_order()

        about_order_page.confirm_order()

        assert about_order_page.watch_success_order_window().is_displayed()

