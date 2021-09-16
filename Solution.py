# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

inp = input().split(" ")
text = inp[0]
num = int(inp[1])



for x in range(1,num+1):
    liste = list(combinations(text,x))
    liste.sort()
    sortedLastList = []
    for a in liste:
        temp = ""
        tempList = []
        for char in a:
            temp += char
        tempList = list(temp)
        tempList.sort()
        temp = ""
        for x in tempList:
            temp += x
        sortedLastList.append(temp)
    sortedLastList.sort()
    for x in sortedLastList:
        print(x)
