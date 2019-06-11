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
    number_of_clocks = 5
    
    def test_number_of_clocks(self, driver):
        driver.get("https://yandex.ru/time/")
        cities = driver.find_elements_by_css_selector(".city__label")
        assert len(cities) == self.number_of_clocks
