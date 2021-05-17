import pytest

import scripts
from mysql.builder import MySQLBuilder
from mysql.models import Top5xx, Top4xx, MethodCounts, NumberOfRequests, Top10Urls


class MySQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)

        self.prepare()


class TestTop4xx(MySQLBase):

    def prepare(self):
        data = scripts.get_res4xx()
        for item in data:
            self.top4xx = self.mysql_builder.create_top4xx(url=item[0], statuscode=item[1], requestsize=item[2],
                                                           ipadress=item[3])

    def get_top4xx(self):
        top4xx = self.mysql.session.query(Top4xx).all()
        print(top4xx)
        return top4xx

    def test_top4xx(self):
        top4xx = self.get_top4xx()
        assert len(top4xx) == 5


class TestTop5xx(MySQLBase):

    def prepare(self):
        data = scripts.get_res5xx()
        for item in data:
            self.top4xx = self.mysql_builder.create_top5xx(ipadress=item[0], requestsize=item[1])

    def get_top5xx(self):
        top5xx = self.mysql.session.query(Top5xx).all()
        print(top5xx)
        return top5xx

    def test_top5xx(self):
        top5xx = self.get_top5xx()
        assert len(top5xx) == 5


class TestTop10Urls(MySQLBase):
    def prepare(self):
        data = scripts.get_url()
        for item in data:
            self.top10urls = self.mysql_builder.create_top10urls(url=item[0], count=item[1])

    def get_top10urls(self):
        top10urls = self.mysql.session.query(Top10Urls).all()
        print(top10urls)
        return top10urls

    def test_top10urls(self):
        top10 = self.get_top10urls()
        assert len(top10) == 10


class TestMethodCounts(MySQLBase):
    def prepare(self):
        data = scripts.get_method()
        for item in data:
            self.method_counts = self.mysql_builder.create_method_counts(method=item[0], count=item[1])

    def get_res(self):
        top = self.mysql.session.query(MethodCounts).all()
        print(top)
        return top

    def test_methods_count(self):
        count = self.get_res()

        assert len(count) == 4
        print(count)


class TestNumberOfRRequests(MySQLBase):
    def prepare(self):
        data = scripts.get_count()
        self.method_counts = self.mysql_builder.create_number_of_requests(count=data)

    def get_count(self):
        count = self.mysql.session.query(NumberOfRequests).all()
        print(count)
        return count

    def test_number_of_requests(self):
        data = self.get_count()
        assert len(data) == 1
