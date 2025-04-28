from behave import given, when, then
from selenium import webdriver
from pages.mercadolibre_page import mercadolibreSearch, mercadolibreResults

@given('el usuario esta en la pagina principal de mercadolibre')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.mercadolibre.com.co")
    context.search_page = mercadolibreSearch(context.driver)
    context.results_page = mercadolibreResults(context.driver)

@when('el usuario busca "{search_term}"')
def step_impl(context, search_term):
    context.search_page.search(search_term)

@then('al menos 1 resultados deben contener la palabra "iPhone"')
def step_then_impl(context):
    product_titles = context.results_page.get_product_titles().text.lower()
    print(product_titles)
    assert "iphone 13" in product_titles