
def Sort(sub_li): 
    l = len(sub_li) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (sub_li[j][1] > sub_li[j + 1][1]): 
                tempo = sub_li[j] 
                sub_li[j]= sub_li[j + 1] 
                sub_li[j + 1]= tempo 
    return sub_li 

def make_table(string):
    table =[]
    for character in string:
        found=False
        for item in table:
            if item[0] == character:
                item[1]+=1
                found=True
        if not found:
            table.append([character,1])
    return table

def encode(table):
    dic={}
    encoding=""
    array = table
    while True:
        if len(array)>1:
            array = table[0]
            encoding+="0"
        else:
            dic[array]=encoding
            encoding=""

def make_tree(table):
    while len(table)>1:
        Sort(table)
        print(table)
        newitem = [[table[0][0], table[1][0]], table[0][1]+table[1][1]]
        table.append(newitem)
        table.remove(table[0])
        table.remove(table[0])
    return table[0][0]

#def encode_string(table, string):
  #  for character in string:

print(make_tree(make_table("missisipi river")))
            

