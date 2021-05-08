from collections import defaultdict
from operator import itemgetter
import re
import pytest

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
        r = self.get_res4xx()
        for item in r:
            self.top4xx = self.mysql_builder.create_top4xx(url=item[0], statuscode=item[1], ipadress=item[2])

    def get_top4xx(self):
        top4xx = self.mysql.session.query(Top4xx).all()
        print(top4xx)
        return top4xx

    def get_res4xx(self):
        result = []
        with open('../access.log') as f:
            res = f.read().splitlines()
        for i in res:
            result.append(i.split(' '))
        s = []
        tpl = '4..'
        for i in result:
            if re.match(tpl, i[8]) is not None:
                s.append((i[6], i[8], int(i[9]), i[0]))
        s.sort(key=itemgetter(2), reverse=True)
        return s[0:5]

    def test_top4xx(self):
        top4xx = self.get_top4xx()
        assert len(top4xx) == 5


class TestTop5xx(MySQLBase):

    def prepare(self):
        r = self.get_res5xx()
        for item in r:
            self.top4xx = self.mysql_builder.create_top5xx(ipadress=item[0], requestsize=item[1])

    def get_res5xx(self):
        result = []
        with open('../access.log') as f:
            res = f.read().splitlines()
        for i in res:
            result.append(i.split(' '))
        ip = []
        tpl = '5..'
        for i in result:
            if re.match(tpl, i[8]) is not None:
                ip.append(i[0])
        counts = defaultdict(int)
        top = 5
        for x in ip:
            counts[x] += 1
        return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]

    def get_top5xx(self):
        top5xx = self.mysql.session.query(Top5xx).all()
        print(top5xx)
        return top5xx

    def test_top5xx(self):
        top5xx = self.get_top5xx()
        assert len(top5xx) == 5


class TestTop10Urls(MySQLBase):
    def prepare(self):
        r = self.get_url()
        for item in r:
            self.top10urls = self.mysql_builder.create_top10urls(url=item[0], count=item[1])

    def get_url(self):
        result = []
        with open('../access.log') as f:
            res = f.read().splitlines()
        for i in res:
            result.append(i.split(' '))
        url = []
        for i in result:
            url.append(i[6])
        counts = defaultdict(int)
        for x in url:
            counts[x] += 1
        top = 10
        return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]

    def get_top10urls(self):
        top10urls = self.mysql.session.query(Top10Urls).all()
        print(top10urls)
        return top10urls

    def test_top10urls(self):
        top10 = self.get_top10urls()
        assert len(top10) == 10


class TestMethodCounts(MySQLBase):
    def prepare(self):
        r = self.get_method()
        for item in r:
            self.method_counts = self.mysql_builder.create_method_counts(method=item[0], count=item[1])

    def get_method(self):
        count_get = 0
        count_post = 0
        count_put = 0
        count_head = 0
        for line in open('../access.log', 'r'):
            if 'POST' in line:
                count_post += 1
            if 'GET' in line:
                count_get += 1
            if 'PUT' in line:
                count_put += 1
            if 'HEAD' in line:
                count_head += 1
        res = ('GET', count_get), ('POST', count_post), ('PUT', count_put), ('HEAD', count_head)
        return res

    def get_res(self):
        topm = self.mysql.session.query(MethodCounts).all()
        print(topm)
        return topm

    def test_methods_count(self):
        count = self.get_res()
        res = self.get_method()

        assert count[0].count == res[0][1] and count[3].count == res[3][1]
        print(count)


class TestNumberOfRRequests(MySQLBase):
    def prepare(self):
        r = sum(1 for line in open('../access.log', 'r'))
        self.method_counts = self.mysql_builder.create_number_of_requests(count=r)

    def get_count(self):
        topm = self.mysql.session.query(NumberOfRequests).all()
        print(topm)
        return topm

    def test_number_of_requests(self):
        top10 = self.get_count()
        assert top10[0].count == 225133
