from pom.home_page_elements import HomePage


def test_about_us(login_set_up) -> None:

    page = login_set_up

    assert page.is_visible(HomePage.celebrating_beauty_header)
    assert page.is_visible(HomePage.celebrating_beauty_body)

