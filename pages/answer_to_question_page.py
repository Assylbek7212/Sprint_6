from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from helpers.constants import *
import allure

class AnswerToQuestion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cook = (By.XPATH, "//button[text()='да все привыкли']")
        self.question_loc = [
            (By.XPATH, f'//*[@id="accordion__heading-{i}"]') for i in range(8)
        ]
        self.answer_to_question_loc = [
            (By.XPATH, f'//*[@id="accordion__panel-{i}"]/p') for i in range(8)
        ]

    @allure.step('Проверка FAQ')
    def check_answer(self, question_loc, answer_to_question_loc, answer_to_question_text):
        self.driver.get(url)
        self.click_element(*self.cook)
        dropdown = self.driver.find_element(*question_loc)
        self.scroll_into_view(dropdown)
        self.click_element(*question_loc)
        self.wait_until(answer_to_question_loc)
        answer_text = self.get_element_text(answer_to_question_loc)
        assert answer_text == answer_to_question_text