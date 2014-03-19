from pprint import pprint

f = open('input.txt', 'r')
count = 0
masterList = {}
for line in f:
    count += 1
    print(count)
    list = []
    for item in line.split(','):
        list.append(item)
    for name1 in list:
        for name2 in list:
            if name1 == name2:
                continue
            if name1 + '_' + name2 in masterList.keys():
                masterList[name1 + '_' + name2] += 1
            elif name2 + '_' + name1 in masterList.keys():
                masterList[name2 + '_' + name1] += 1
            else:
                masterList[name1 + '_' + name2] = 1
print('done')
pprint(masterList)
