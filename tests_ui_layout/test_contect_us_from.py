from pom.contact_us_page import ContactUsPage
import pytest


@pytest.mark.smoke
def test_submit_form(set_up) -> None:
    page = set_up

    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Albin", "ST 122", "mail@mail.com", "123-234-3452", "test subject", "message")


