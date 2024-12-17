from selenium.webdriver.common.by import By


class HomeWebElements:
    expected_element_locator = (By.XPATH, "//span[contains(text(),'Compara cientos de webs a la vez')]")
    where_label = (By.CSS_SELECTOR, '.AQWr-mod-margin-bottom-xlarge c0qPo')
    signin_button = (By.CSS_SELECTOR, '.menu__wrapper .menu-label__wrapper button')
    search_button = (By.CSS_SELECTOR, '.pageContent .SearchPage__FrontDoor .HPw7-form-fields-and-submit .HPw7-submit button')
    image_element = (By.CSS_SELECTOR, '.AQWr-mod-margin-bottom-xlarge.c0qPo')

    dropdown_button = (By.XPATH, '//header/div[1]/div[2]/div[1]/div[1]/div[1]')

    left_menu_buttons = {
        "Stays": (By.XPATH, "//a[@href='/stays']"),
        "Cars": (By.XPATH, "//a[@href='/cars']"),
    }

    expected_title = {
        "Stays": (By.XPATH, "//div[contains(text(),'Buscar hoteles')]"),
        "Cars": (By.XPATH, "//div[contains(text(),'Buscar autos')]"),
    }