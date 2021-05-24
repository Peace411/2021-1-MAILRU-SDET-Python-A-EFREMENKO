from faker import Faker

from mysql.models import Top4xx, Top5xx, Top10Urls, MethodCounts, NumberOfRequests

fake = Faker()


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_top4xx(self, url=None, statuscode=None, requestsize=None, ipadress=None):
        top4xx = Top4xx(
            url=url,
            statuscode=statuscode,
            requestsize=requestsize,
            ipadress=ipadress
        )
        self.client.session.add(top4xx)
        self.client.session.commit()
        return top4xx

    def create_top5xx(self, ipadress=None, requestsize=None):

        top5xx = Top5xx(
            ipadress=ipadress,
            reqestsize=requestsize
        )
        self.client.session.add(top5xx)
        self.client.session.commit()
        return top5xx

    def create_top10urls(self, url=None, count=None):
        top10url = Top10Urls(
            url=url,
            count=count
        )
        self.client.session.add(top10url)
        self.client.session.commit()
        return top10url

    def create_method_counts(self, method=None, count=None):
        method_counts = MethodCounts(
            method=method,
            count=count
        )
        self.client.session.add(method_counts)
        self.client.session.commit()
        return method_counts

    def create_number_of_requests(self, count=None):
        number_of_requests = NumberOfRequests(count=count)
        self.client.session.add(number_of_requests)
        self.client.session.commit()
        return number_of_requests
