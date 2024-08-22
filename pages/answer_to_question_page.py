from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from helpers.constants import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        self.driver.find_element(*self.cook).click()
        dropdown = self.driver.find_element(*question_loc)
        self.scroll_into_view(dropdown)
        self.driver.find_element(*question_loc).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(answer_to_question_loc)
        )
        answer_text = self.get_element_text(answer_to_question_loc)
        assert answer_text == answer_to_question_text