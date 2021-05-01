import re
from collections import defaultdict


def get_url():
    result = []
    with open('../access.log') as f:
        res = f.read().splitlines()
    for i in res:
        result.append(i.split(' '))
    url = []
    for i in result:
        url.append(i[6])
    return url


def leaders(xs, top=10):
    counts = defaultdict(int)
    for x in xs:
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]


if __name__ == "__main__":
    url = get_url()
    top = leaders(url)
    file = open('res3', 'w')
    for l in top:
        file.write(str(l).replace('(', '').replace(')', '').replace("'", '') + '\n')
