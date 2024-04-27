from behave import given, when, then
from django.test import Client

@given('I am on the homepage')
def step_impl(context):
    context.client = Client()

@when('I navigate to the home page')
def step_impl(context):
    context.response = context.client.get('/')

@then('I should see the welcome message')
def step_impl(context):
    assert 'Welcome' in context.response.content.decode()
