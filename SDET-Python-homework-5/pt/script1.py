import os
if __name__ == "__main__":
    open('result','w').write('All Request -'+str(sum(1 for line in open('../access.log', 'r'))))