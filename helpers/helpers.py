from selenium.webdriver.common.by import By

class OrderPageLocators:
    BUTTON_ORDER_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    BUTTON_ORDER_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM')]")