import socket

from faker import Faker

from base import BaseCase
from mock.flask_mock import MOCK_DATA

fake = Faker()

host = socket.gethostbyname("app") + ':8080'
host.split(':')


class TestLoginPage(BaseCase):
    def test_autorization(self):
        self.login_page.user_login('Radmir', 'qwerty12345')

    def test_registartion(self):
        self.login_page.go_to_registation()
        self.registr_page.registration(name=fake.lexify(text='?????????'), email=fake.email(), password=fake.password())
        assert self.driver.current_url == f'http://{host}/welcome/'

    def test_invalid_autorization(self):
        self.login_page.user_login(name=fake.lexify(text="?????????"), password=fake.password())
        self.login_page.invalid_login()
        assert self.driver.current_url == f'http://{host}/login'

    def test_not_true_sdet(self):
        self.login_page.go_to_registation()
        self.registr_page.registration(name=fake.lexify(text='?????????'), email=fake.email(), password=fake.password(),
                                       SDET=False)
        assert self.driver.current_url == f'http://{host}/reg'


class TestMainPage(BaseCase):
    class TestNavbar(BaseCase):
        def go_to_navbar_link(self, expected_url, button_href, link_href):
            name = fake.lexify(text='?????????')
            email = fake.email()
            password = fake.password()
            self.login_page.go_to_registation()
            self.registr_page.registration(name=name, email=email, password=password)
            self.main_page.go_to_navbar_link(button_href, link_href)
            try:
                window = self.driver.window_handles
                self.driver.switch_to_window(window[1])
            except:
                raise AssertionError('the page did not open in a separate window')
            assert self.driver.current_url == expected_url, f'the expected link {self.driver.current_url} is not equal ' \
                                                            f'to the current one{expected_url} '

        def test_go_to_linux_centos(self):
            self.go_to_navbar_link('https://www.centos.org/download/', 'Linux', 'Download Centos7')

        def test_go_to_python_history(self):
            self.go_to_navbar_link('https://en.wikipedia.org/wiki/History_of_Python', 'Python', 'Python history')

        def test_go_to_python_about_flask(self):
            self.go_to_navbar_link('https://flask.palletsprojects.com/en/1.1.x/#', 'Python', 'About Flask')

        def test_go_to_networks_news(self):
            self.go_to_navbar_link('https://www.wireshark.org/news/', 'Network', 'News')

        def test_go_to_networks_downloads(self):
            self.go_to_navbar_link("https://www.wireshark.org/#download", "Network", "Download")

        def test_go_to_networks_expempls(self):
            self.go_to_navbar_link('https://hackertarget.com/tcpdump-examples/', "Network", "Examples")

    def test_overlay_link_api(self):
        name = fake.lexify(text='?????????')
        email = fake.email()
        password = fake.password()
        self.login_page.go_to_registation()
        self.registr_page.registration(name=name, email=email, password=password)
        link = 'https://en.wikipedia.org/wiki/Application_programming_interface'
        url = self.main_page.go_to_overlay_link(link)
        assert url == 'https://en.wikipedia.org/wiki/API'

    def test_overlay_link_future(self):
        name = fake.lexify(text='?????????')
        email = fake.email()
        password = fake.password()
        self.login_page.go_to_registation()
        self.registr_page.registration(name=name, email=email, password=password)
        link = 'https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/'
        url = self.main_page.go_to_overlay_link(link)
        assert url == link

    def test_overlay_link_SMTP(self):
        name = fake.lexify(text='?????????')
        email = fake.email()
        password = fake.password()
        self.login_page.go_to_registation()
        self.registr_page.registration(name=name, email=email, password=password)
        link = 'https://ru.wikipedia.org/wiki/SMTP'
        url = self.main_page.go_to_overlay_link(link)
        assert url == link
    def test_vk_id(self):
        name = fake.lexify(text='?????????')
        email = fake.email()
        password = fake.password()
        self.login_page.go_to_registation()
        self.registr_page.registration(name=name, email=email, password=password)
        MOCK_DATA['user_name'] = name
        self.main_page.check_vk_id(name)
