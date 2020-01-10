# encoding=utf-8

import pytest
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from src.lib.Browser import Browser
from src.b_webdriver.b_find_element.Common import Common


class TestAction:

    def setup(self):
        self.browser = Browser().browser(location="./src/lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.get()

    def teardown(self):
        self.browser.quit()

    def test_find_element_by_css_selector(self):
        sleep(3)
        bai_du_img = self.browser.find_element_by_xpath("//img[@alt='div2-img2']")
        ActionChains(self.browser).move_to_element_with_offset(bai_du_img, 370, 272).click().perform()
        sleep(3)
        assert "百度一下" in self.browser.page_source


if __name__ == "__main__":
    pytest.main()
