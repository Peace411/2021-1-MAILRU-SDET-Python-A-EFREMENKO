import pytest
from faker import Faker

from ui_tests.base import BaseCase

fake = Faker()

host = 'my_app:8080'


@pytest.mark.ui
class TestLoginPage(BaseCase):
    authorize = False

    def test_login(self):
        user = self.mysql.create_test_user()
        self.login_page.user_login(user.username, user.password)
        assert self.driver.current_url in f'http://{host}/welcome/'

    def test_invalid_username_authorization(self, get_user):
        self.login_page.user_login(name=fake.first_name(), password=get_user[1])
        self.login_page.invalid_login()
        assert self.driver.current_url == f'http://{host}/login'

    def test_invalid_pass_authorization(self, get_user):
        self.login_page.user_login(name=get_user[0], password=fake.password())
        self.login_page.invalid_login()
        assert self.driver.current_url == f'http://{host}/login'


@pytest.mark.ui
class TestRegPage(BaseCase):
    authorize = False

    def test_not_true_sdet(self):
        self.login_page.go_to_registation()
        self.registr_page.registration(name=fake.lexify(text='?????????'), email=fake.email(), password=fake.password(),
                                       SDET=False)
        assert self.driver.current_url == f'http://{host}/reg'

    def test_reg(self):
        self.login_page.go_to_registation()
        self.registr_page.registration(name=fake.lexify(text='?????????'), email=fake.email(), password=fake.password())

        assert self.driver.current_url == f'http://{host}/welcome/'

    @pytest.mark.parametrize('password', ['', 'a'])
    def test_reg_min_max_len_password(self, password):
        self.login_page.go_to_registation()
        self.registr_page.registration(name=fake.lexify(text='?????????'),
                                       email=fake.email(),
                                       password=password)
        assert self.driver.current_url == f'http://{host}/reg', f'Bad user  registered: {self.driver.current_url}'

    def test_invalid_username_registration(self):
        self.login_page.go_to_registation()
        self.registr_page.registration(name='',
                                       email=fake.email(),
                                       password=fake.password())
        assert 'welcome' not in self.driver.current_url

    @pytest.mark.parametrize(("email", "expected_message"), [(" ", "Incorrect email length"),
                                                             ("@gmail.com", "Invalid email address"),
                                                             ("a" * 65, "Incorrect email length")])
    def test_invalid_email_registration(self, email, expected_message):
        self.login_page.go_to_registation()
        self.registr_page.registration(name=fake.lexify(text='?????????'),
                                       email=email,
                                       password=fake.password())
        assert 'welcome' not in self.driver.current_url
        assert self.registr_page.get_error_message() == expected_message


@pytest.mark.ui
class TestMainPage(BaseCase):

    def go_to_navbar_link(self, expected_url, button_href, link_href):
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
        self.go_to_navbar_link('https://hackertarget.com/tcpdump-examples/', "Network", "Examples ")

    def test_overlay_link_api(self):
        link = 'https://en.wikipedia.org/wiki/Application_programming_interface'
        url = self.main_page.go_to_overlay_link(link)
        assert url == 'https://en.wikipedia.org/wiki/API'

    def test_overlay_link_future(self):
        link = 'https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/'
        url = self.main_page.go_to_overlay_link(link)
        assert url == link

    def test_overlay_link_smpt(self):
        link = 'https://ru.wikipedia.org/wiki/SMTP'
        url = self.main_page.go_to_overlay_link(link)
        assert url == link

    def test_vk_id(self):
        self.main_page.check_vk_id(self.username)

    def go_to_navbar_href(self, name_button, expected_url):
        self.main_page.go_to_navbar_href(name_button)
        assert self.driver.current_url == expected_url

    def test_go_to_python(self):
        self.go_to_navbar_href('Python', 'https://www.python.org/')

    def test_go_to_linux(self):
        self.go_to_navbar_href('Linux', 'https://www.linux.org/')

    def test_go_to_network(self):
        self.go_to_navbar_href('Network', 'https://en.wikipedia.org/wiki/Network')

    def test_menu_random_text(self):
        random_text_first = self.main_page.get_random_text_in_footer()
        self.main_page.driver.refresh()
        random_text_second = self.main_page.get_random_text_in_footer()
        assert random_text_first != random_text_second

    def test_logout(self):
        self.main_page.click_logout()
        assert 'welcome' not in self.driver.current_url
        database_user = self.mysql_client.get_user(username=self.username)
        assert database_user.active == 0
