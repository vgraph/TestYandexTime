import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


class TestYandexTime:
    
    def test_01(self, driver):
        driver.get("https://yandex.ru/time/")
        first_city = driver.find_element_by_css_selector(".city__label")
        print("Text:", first_city.get_property("textContent"))
