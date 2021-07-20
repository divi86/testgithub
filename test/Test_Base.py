import pytest
from selenium import webdriver
from test.Signup import SignUpPage
from test.test_fb import Base
from test.LoginPage import LoginPage

class Test_Case(Base):
    @pytest.fixture()
    def setup(self):
        self.driver = self.browser()
        self.load_url("http://en-gb.facebook.com/")
        yield
        self.quit_browser()

    def test_login(self,setup):
        l = LoginPage(self.driver)
        self.set_text(l.getTxtUser(), "12345")
        self.set_text(l.getTxtPass(), "hello123@")
        self.btn_click(l.getLogin())

    def test_register(self,setup):
        l1 = LoginPage(self.driver)
        self.btn_click(l1.getCreate())

        s = SignUpPage(self.driver)
        self.set_text(s.getTxtfn(), "Divya")
        self.set_text(s.getTxtln(), "Duraisamy")
