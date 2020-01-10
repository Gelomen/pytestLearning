# encoding=utf-8

import pytest
import time
from src.lib.Browser import Browser


class TestClass:

    def setup(self):
        self.browser = Browser().browser(headless=False, location="./src/lib/chromedriver.exe")

    def teardown(self):
        self.browser.quit()

    def test_search(self):
        self.browser.get("http://www.baidu.com")

        self.browser.find_element_by_id("kw").clear()

        self.browser.find_element_by_id("kw").send_keys(u"Webdriver")

        self.browser.find_element_by_id("su").click()

        time.sleep(3)

        assert "Webdriver" in self.browser.page_source


if __name__ == "__main__":
    pytest.main()
