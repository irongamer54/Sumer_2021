import json 
level=[]
with open("test.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
level=[jsonObject['map1'],jsonObject['map1_bg'],jsonObject['map1_bg2']]

x = y = 0
for i in range(len(level)):
    for row in level[0]:       
        print(row)
        if i==0:
            col_bool=True
        else:
            col_bool=False
        for col in row:              
            x+32
            y+=32
            x=0