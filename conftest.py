import time

import pytest


@pytest.fixture(scope="function")
def set_up(browser):

    context = browser.new_context()

    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(5000)

    yield page
    page.close()


@pytest.fixture(scope="function")
def login_set_up(set_up):
    page = set_up

    page.wait_for_load_state("domcontentloaded", timeout=7000)

    assert page.is_visible("button:has-text(\"Log In\")")
    time.sleep(1)
    page.click("button:has-text(\"Log In\")")

    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector("[data-testid=\"signUp\\.switchToSignUp\"]")
    assert page.is_visible("[data-testid=\"signUp\\.switchToSignUp\"]")
    page.click("[data-testid=\"signUp\\.switchToSignUp\"]")

    page.click("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]")

    page.click("[data-testid=\"siteMembers\\.container\"] input[type=\"email\"]")

    page.fill("[data-testid=\"siteMembers\\.container\"] input[type=\"email\"]", "alrami_26@hotmail.com")

    page.press("[data-testid=\"siteMembers\\.container\"] input[type=\"email\"]", "Tab")

    page.fill("input[type=\"password\"]", "Con#123")

    page.click("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]")

    yield page


@pytest.fixture
def go_to_new_collection_page(page):

    #page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.goto("/new-collection")
    page.set_default_timeout(5000)

    yield page