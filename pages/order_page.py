from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def enter_name(self, name):
        enter_name = self.wait_and_find_element(OrderPageLocators.NAME_FIELD)
        enter_name.send_keys(name)

    def enter_surname(self, surname):
        enter_surname = self.wait_and_find_element(OrderPageLocators.SURNAME_FIELD)
        enter_surname.send_keys(surname)

    def enter_address(self, address):
        enter_address = self.wait_and_find_element(OrderPageLocators.ADDRESS_FIELD)
        enter_address.send_keys(address)

    def enter_subway_station(self, subway_locator):
        search_subway_station = self.wait_and_find_element(OrderPageLocators.SUBWAY_STATION_FIELD)
        search_subway_station.click()
        choose_subway_station = self.wait_and_find_element(subway_locator)
        choose_subway_station.click()

    def enter_phone_number(self, phone_number):
        enter_phone_number = self.wait_and_find_element(OrderPageLocators.PHONE_NUMBER_FIELD)
        enter_phone_number.send_keys(phone_number)

    def enter_user_data(self, name, surname, address, subway_locator, phone_number):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_subway_station(subway_locator)
        self.enter_phone_number(phone_number)

    def click_next_button(self):
        click_next_button = self.wait_and_find_element(OrderPageLocators.NEXT_BUTTON)
        return click_next_button.click()

    def click_scooter_logo(self):
        click_scooter_logo = self.wait_and_find_element(OrderPageLocators.SCOOTER_LOGO)
        return click_scooter_logo.click()