from src.main.pages.main_page import MainHeaderBar
from src.main.pages.login_modal import LoginModalWindow

def test_valid_login(driver):

    main_page = MainHeaderBar(driver)
    login_modal = LoginModalWindow(driver)
    email = "pajibir101@skrak.com"
    password = "Bb123456aA"

    main_page.open_page()
    main_page.click_login_head_bar_button()
    main_page.click_entry_button()

    login_modal.input_creds(email, password)
    login_modal.login()
    login_modal.check_login_modal_invisibility()

    actual_account_text = main_page.get_text_head_bar_button()
    expect_account_text = "Юрий Петров"

    assert expect_account_text in actual_account_text