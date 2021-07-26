from behave import when, then


@when('Hover mouse over new arrivals')
def hover_new_arrivals(context):
    context.app.amazon_fashion_header.hover_new_arrivals()


@then('Women fashion deals are shown')
def verify_women_fashion_panel_present(context):
    context.app.amazon_fashion_header.verify_women_fashion_panel_present()