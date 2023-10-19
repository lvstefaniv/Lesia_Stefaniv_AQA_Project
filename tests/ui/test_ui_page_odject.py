from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    #page object creation
    sign_in_page = SignInPage()

    #Open the page https://github.com/login
    sign_in_page.go_to()

    #Try to sign in GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    #Check the expected page title
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    #Close a browser
    sign_in_page.close()