from behave import given, use_step_matcher
from lib.pages.basepage import BasePage

use_step_matcher("re")


@given(u'I navigate to the kayak main page')
def visit_kayak_main_page(context):
    url = BasePage.get_url_per_environment(context)
    context.browser.visit_page(url)
