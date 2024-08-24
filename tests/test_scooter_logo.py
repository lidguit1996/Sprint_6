import allure
from locators.main_page_locators import OrderButtons, Others
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Urls


@allure.title('Проверка клика по логотипу "Самокат"')
@allure.description('Кликаем на логотип "Самокат", находясь не на главной странице, и проверяем редирект на главную страницу')
class TestScooterLogo:

    def test_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.SCOOTER_MAIN)
        main_page.click_order_button(OrderButtons.HEADER_ORDER_BUTTON)

        order_page = OrderPage(driver)
        order_page.click_scooter_logo()

        assert main_page.wait_and_find_element(Others.MAIN_TITLE).is_displayed()

