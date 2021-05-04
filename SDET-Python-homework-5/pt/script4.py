import re
from operator import itemgetter
from collections import defaultdict


def get_res():
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
    return s


if __name__ == "__main__":
    res = get_res()
    res.sort(key=itemgetter(2), reverse=True)
    file = open('res4', 'w')
    for l in res[0:5]:
        file.write(str(l).replace('(', '').replace(')', '').replace("'", '') + '\n')
