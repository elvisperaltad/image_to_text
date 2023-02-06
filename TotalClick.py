import re

arr1 = []
result = []
pattern = r'[0-9]'
n1 =["ID12-55","jose","30","ID342-66","Carlos","25","ID123-77","Miguel","33"]
counter = 0

for x in n1:
    #splitter = x.split("-")
    splitter = re.sub(pattern, '', x)
    if counter > 0 and splitter == "ID-":
        result.append(arr1)
        arr1 = [x]
        counter += 1
        #print("resultado es:",result)
    else:
        arr1.append(x)
        counter += 1
        

result.append(arr1)
print("resultado es:",len(result), "el arreglo es: ",result)

