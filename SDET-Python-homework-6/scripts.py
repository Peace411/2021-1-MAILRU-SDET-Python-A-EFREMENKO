import os
from collections import defaultdict
from operator import itemgetter
import re

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


def read_access():
    result = []
    with open(repo_root + '/access.log') as f:
        res = f.read().splitlines()
    for i in res:
        result.append(i.split(' '))
    return result


def get_res4xx():
    result = read_access()
    s = []
    tpl = '4..'
    for i in result:
        if re.match(tpl, i[8]) is not None:
            s.append((i[6], i[8], int(i[9]), i[0]))
    s.sort(key=itemgetter(2), reverse=True)
    return s[0:5]


def get_res5xx():
    result = read_access()
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


def get_url():
    result = read_access()
    url = []
    for i in result:
        url.append(i[6])
    counts = defaultdict(int)
    for x in url:
        counts[x] += 1
    top = 10
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]


def get_method():
    count_get = 0
    count_post = 0
    count_put = 0
    count_head = 0
    for line in open(repo_root + '/access.log', 'r'):
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


def get_count():
    data = sum(1 for line in open(repo_root + '/access.log', 'r'))
    return data
