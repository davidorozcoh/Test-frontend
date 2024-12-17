import pdb
import time
from telnetlib import EC

from behave import when, use_step_matcher
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from lib.components.generalcomponents import GeneralComponents
from lib.helpers.generalhelpers import transformation_helper
from lib.pages.webelements.homewebelements import HomeWebElements

use_step_matcher("re")


@when(u'I click on the "(?P<element_name>.*)" "(?P<element_type>button|dropdown|option)"')
def step_impl(context, element_name, element_type):
    element_name = transformation_helper(element_name, element_type)
    if GeneralComponents.wait_until_element_is_clickable(
            context, context.current_page.webElements.__dict__.get(element_name)
    ):
        return context.browser.find_element(context.current_page.webElements.__dict__.get(element_name)).click()


@when(u'I navigate to the "(?P<url>.*)" URL')
def step_impl(context, url):
    return context.browser.visit(url)


@when('I select "(?P<option>.*)" in the dropdown')
def step_impl(context, option):
    return context.current_page.text_value_in_the_select(option)


@when(u'I search "(?P<option>.*)" in the input')
def step_impl(context, option):
    return context.current_page.text_value_in_the_filter(option)


@when('I click on the dropdown button to open the left menu')
def step_impl(context):
    dropdown_button = GeneralComponents.wait_until_element_is_clickable(context, HomeWebElements.dropdown_button)
    dropdown_button.click()
    time.sleep(5)


@when('I click on the "{menu_option}" button')
def step_impl(context, menu_option):
    time.sleep(5)
    menu_button_locator = HomeWebElements.left_menu_buttons.get(menu_option)
    if not menu_button_locator:
        raise ValueError(f"La opción '{menu_option}' no existe en el menú desplegable.")
    menu_button = GeneralComponents.wait_until_element_is_clickable(context, menu_button_locator)
    menu_button.click()
    print(f"Se hizo clic en la opción del menú: {menu_option}.")
