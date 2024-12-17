import time
from telnetlib import EC

from behave import then, use_step_matcher
from hamcrest import equal_to, assert_that, only_contains
from selenium.webdriver.support.wait import WebDriverWait

from lib.components.generalcomponents import GeneralComponents
from lib.helpers.generalhelpers import validate_text, transform_validation, transformation_helper, join_words, \
    split_and_replace_string, transformation_to_element_name
from lib.pages.webelements.homewebelements import HomeWebElements

use_step_matcher("re")


@then(u'The page title should "(?P<assertion>contain|equal)" the "(?P<page_name>.*)" text')
def step_impl(context, assertion, page_name):
    validation_result = validate_text(assertion, page_name, context.current_page.get_title_page())
    return assert_that(validation_result, equal_to(True),
                       f'The expected title is "{page_name}", but was "{context.current_page.get_title_page()}"')


@then(u'I should be in the "(?P<expected_title>.*)" page')
def step_impl(context, expected_title):
    expected_locator = HomeWebElements.expected_element_locator.get(expected_title)
    if not expected_locator:
        raise ValueError(f"No se encontró un elemento esperado para la página: '{expected_title}'")
    GeneralComponents.wait_until_element_is_visible(context, expected_locator)
    print(f"Se validó que la página esperada '{expected_title}' está visible.")


@then(u'The page "(?P<expression>should|should not)" contain the next elements')
def step_impl(context, expression):
    list_validation = context.browser.are_element_presents(context.table, context)
    assertion = transform_validation(expression)
    return assert_that(list_validation, only_contains(assertion))


@then(u'The "(?P<element_name>.*)" "(?P<element_type>label|button|container)" should contain the "('
      u'?P<text_to_validate>.*)" text')
def step_impl(context, element_name, element_type, text_to_validate):
    element = transformation_helper(element_name, element_type)
    text_element = GeneralComponents.get_text_element(context, element).rstrip()
    new_text_to_validate = join_words(split_and_replace_string(text_to_validate))
    new_text_element = join_words(split_and_replace_string(text_element))
    return assert_that(new_text_to_validate, equal_to(new_text_element))


@then(u'The "(?P<element_name>.*)" "(?P<element_type>label|button|container)" "(?P<expression>should|should not)" be '
      u'present')
def step_impl(context, element_name, element_type, expression):
    element = transformation_helper(element_name, element_type)
    element_validation = GeneralComponents.check_exist_element(context, element)
    assertion = transform_validation(expression)
    return assert_that(element_validation, equal_to(assertion))


@then(u'The url page should be equal to the next "(?P<url>.*)" url')
def step_impl(context, url):
    if not hasattr(context.browser, "get_current_url"):
        raise AttributeError(
            "The 'context.browser' object is not configured properly. "
            "Ensure it is an instance of BasePage with a valid WebDriver."
        )
    current_url = context.browser.get_current_url()
    print(f"Captured Current URL: {current_url}")
    assert current_url == url, (
        f"Expected URL '{url}', but got '{current_url}'"
    )


@then(u'The "(?P<element_name>.*)" "(?P<element_type>button)" "('u'?P<expression>should|should 'u'not)" be enabled')
def step_impl(context, element_name, element_type, expression):
    element_name = transformation_helper(element_name, element_type)
    assertion = transform_validation(expression)
    button_enabled = GeneralComponents.is_enabled_in_page(context, element_name)
    return assert_that(button_enabled, equal_to(assertion))


@then('I should see the "{expected_title}" page')
def step_impl(context, expected_title):
    expected_locator = HomeWebElements.expected_title.get(expected_title)
    if not expected_locator:
        raise ValueError(f"No se encontró un elemento esperado para la página: '{expected_title}'")
    GeneralComponents.wait_until_element_is_visible(context, expected_locator)
    print(f"Se validó que la página esperada '{expected_title}' está visible.")
    time.sleep(5)