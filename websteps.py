from behave import when, then

@when('I click the button "{button_name}"')
def step_click_button(context, button_name):
    pass  # Implement button click logic here

@then('I should see "{text}" on the page')
def step_see_text(context, text):
    pass  # Implement text verification logic here

@then('I should not see "{text}" on the page')
def step_not_see_text(context, text):
    pass  # Implement logic to check text is not present

@then('I should see the message "{message}"')
def step_see_message(context, message):
    pass  # Implement message verification logic here
