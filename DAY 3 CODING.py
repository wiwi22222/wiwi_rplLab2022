def ss(list) :
    iterasi = 0
    for i in range(len(list)-1) :
        minimal = i
        for j in range(i+1, len(list)) :
            if list{j} < list{minimal} :
            minimal = j
        iterasi += 1
        list{i},list{minimal} = list {minimal},list{i}
        print(iterasi, list)
 
list = {100, 4, 26, 22, 57, 33, 46, 55, 33, 46, 55, 30, 85, 70, 94}
print('data yang akan di sort :', list)
print('selection sort :')
ss(list)