import time

import pytest


@pytest.mark.regression
@pytest.mark.parametrize("email", ["alrami_26@hotmail.com",
                                    pytest.param("fame@mail.com", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("pwd", ["Con#123",
                                    pytest.param("masss", marks=pytest.mark.xfail)])
def test_login(set_up, email, pwd) -> None:

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

    page.fill("[data-testid=\"siteMembers\\.container\"] input[type=\"email\"]", email)

    page.press("[data-testid=\"siteMembers\\.container\"] input[type=\"email\"]", "Tab")

    page.fill("input[type=\"password\"]", pwd)

    page.click("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]")


