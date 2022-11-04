from behave import given, when, then


@given(u'que accesso a página de Google')
def step_impl(context):
    context.web.get("https://www.google.com.br/")

@when(u'realizo uma pesquisa')
def step_impl(context):
    context.element = context.web.find_element("name", "q")
    context.element.click()
    context.element.send_keys("PyJamas Conf")
    context.element.submit()

@when(u'pesquisa e realiza')
def step_impl(context):
    assert context.web.title == "PyJamas conf - Buscar con Google"

@then(u'o titulo da página deve ser validado')
def step_impl(context):
    pass