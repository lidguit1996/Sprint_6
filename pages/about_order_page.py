from pages.base_page import BasePage
from locators.about_order_page_locators import AboutOrderPageLocators


class AboutOrderPage(BasePage):

    def set_order_date(self, date_locator):
        search_order_date = self.wait_and_find_element(AboutOrderPageLocators.DATE_FIELD)
        search_order_date.click()
        choose_order_date = self.wait_and_find_element(date_locator)
        choose_order_date.click()

    def set_order_period(self, period_locator):
        search_order_period = self.wait_and_find_element(AboutOrderPageLocators.ORDER_PERIOD_FIELD)
        search_order_period.click()
        choose_order_period = self.wait_and_find_element(period_locator)
        choose_order_period.click()

    def set_colour(self, colour_locator):
        set_colour = self.wait_and_find_element(colour_locator)
        set_colour.click()

    def set_comment(self, comment):
        set_comment = self.wait_and_find_element(AboutOrderPageLocators.COMMENT_FIELD)
        set_comment.send_keys(comment)


    def set_about_order_data(self, date_locator, period_locator, colour_locator, comment):
        self.set_order_date(date_locator)
        self.set_order_period(period_locator)
        self.set_colour(colour_locator)
        self.set_comment(comment)

    def submit_order(self):
        submit_order = self.wait_and_find_element(AboutOrderPageLocators.SUBMIT_ORDER_BUTTON)
        return submit_order.click()

    def confirm_order(self):
        confirm_order = self.wait_and_find_element(AboutOrderPageLocators.CONFIRM_ORDER_BUTTON)
        return confirm_order.click()

    def watch_success_order_window(self):
        return self.wait_and_find_element(AboutOrderPageLocators.SUCCESS_ORDER_WINDOW)



