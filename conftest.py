import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OG


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    goptions = OG()
    goptions.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=goptions)
    yield browser
    print("\nquit browser..")
    browser.quit()