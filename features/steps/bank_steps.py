from behave import *
from features.pages.bank_page import BankPage

@given(u'the user is on the home page')
def step_impl(context):
    context.bp = BankPage(context.driver)

@when(u'the user selects "{option}"')
def step_impl(context,option):
    context.bp.select_option(option)

@when(u'the user enters "{value}" as the "{field}"')
def step_impl(context,field,value):
    context.bp.provide_value(field,value)

@when(u'the user select "{value}" as the "{parameter}"')
def step_impl(context,parameter,value):
    context.bp.select_dropdown_value(parameter,value)

@when(u'the user clicks "{button}"')
def step_impl(context,button):
    context.bp.click_button(button)

@then(u'a new customer should be added successfully')
def step_impl(context):
    context.bp.accept_alert()

@then(u'transaction should be successful')
def step_impl(context):
    assert "successful" in context.bp.get_transaction_message().lower()

@then(u'a new account should be added successfully')
def step_impl(context):
    context.bp.accept_alert()
