import allure
from data import Urls, AnswerTexts
from pages.main_page import MainPage
from locators.main_page_locators import QuestionLocators, AnswersLocators
import pytest


@allure.title('Проверка "Вопросов о важном"')
@allure.description('На главной странице ищем "Вопросы о важном", нажимаем на вопросы, проверяем открытие и текст ответа на вопрос')
class TestClickQuestions:

    how_much_question = [QuestionLocators.HOW_MUCH_QUESTION, AnswersLocators.HOW_MUCH_ANSWER, AnswerTexts.HOW_MUCH_ANSWER_TEXT]
    want_more_scooters_question = [QuestionLocators.WANT_MORE_SCOOTERS_QUESTION, AnswersLocators.WANT_MORE_SCOOTERS_ANSWER, AnswerTexts.WANT_MORE_SCOOTERS_ANSWER_TEXT]
    time_calculation_question = [QuestionLocators.TIME_CALCULATION_QUESTION, AnswersLocators.TIME_CALCULATION_ANSWER, AnswerTexts.TIME_CALCULATION_ANSWER_TEXT]
    order_today_question = [QuestionLocators.ORDER_TODAY_QUESTION, AnswersLocators.ORDER_TODAY_ANSWER, AnswerTexts.ORDER_TODAY_ANSWER_TEXT]
    order_extend_question = [QuestionLocators.ORDER_EXTEND_QUESTION, AnswersLocators.ORDER_EXTEND_ANSWER, AnswerTexts.ORDER_EXTEND_ANSWER_TEXT]
    charge_question = [QuestionLocators.CHARGE_QUESTION, AnswersLocators.CHARGE_ANSWER, AnswerTexts.CHARGE_ANSWER_TEXT]
    order_cancellation_question = [QuestionLocators.ORDER_CANCELLATION_QUESTION, AnswersLocators.ORDER_CANCELLATION_ANSWER, AnswerTexts.ORDER_CANCELLATION_ANSWER_TEXT]
    not_in_moscow_question = [QuestionLocators.NOT_IN_MOSCOW_QUESTION, AnswersLocators.NOT_IN_MOSCOW_ANSWER, AnswerTexts.NOT_IN_MOSCOW_ANSWER_TEXT]

    @pytest.mark.parametrize('question, answer, answer_text', [
        how_much_question,
        want_more_scooters_question,
        time_calculation_question,
        order_today_question,
        order_extend_question,
        charge_question,
        order_cancellation_question,
        not_in_moscow_question
    ]
                             )
    def test_click_questions(self, driver, question, answer, answer_text):
        main_page = MainPage(driver)
        main_page.open_page(Urls.SCOOTER_MAIN)
        main_page.scroll_to_element(question)
        main_page.click_question(question)
        assert main_page.answer_the_question(answer) == answer_text








