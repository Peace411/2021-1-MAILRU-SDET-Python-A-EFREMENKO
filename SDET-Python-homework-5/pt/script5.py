import re
from collections import defaultdict


def get_ip():
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
    return ip


def leaders(xs, top=5):
    counts = defaultdict(int)
    for x in xs:
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]


if __name__ == "__main__":
    ip = get_ip()
    top = leaders(ip)
    file = open('res5', 'w')
    for l in top:
        file.write(str(l).replace('(', '').replace(')', '').replace("'", '') + '\n')
