if __name__ == "__main__":
    count_get = 0
    count_post= 0
    count_put=0
    count_head=0
    for line in open('../access.log','r'):
        if 'POST' in line:
            count_post += 1
        if 'GET' in line:
            count_get+=1
        if  'PUT' in line:
            count_put+=1
        if 'HEAD' in line:
            count_head+=1
    myfile =open ('res2','w')
    myfile.write(f'POST- {count_post}\n GET- {count_get}\n PUT- {count_put}\nHEAD- {count_head}')
    print(f'POST- {count_post}\n GET- {count_get}\n PUT- {count_put}\nHEAD- {count_head}')
