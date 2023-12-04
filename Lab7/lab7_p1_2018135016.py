import re

t = open("input_7_1.txt").read().split('\n')

for i in range(len(t)):
    a = re.match("def\s[a-zA-Z0-9_]+[(].*[)]", t[i]) # 각 줄에 대하여 def <함수>(인자) 꼴의 모든 경우 탐색
    if a:
        l=[]
        b = re.split("[\s(]", a.group())[1] # 함수명을 받아와 b에 저장
        for j in range(len(t)):
            c = re.search(b+"[(].*[)]", t[j]) # 각 줄에 대하여 <함수>(인자) 꼴의 모든 경우 탐색
            if c and i!=j: # 같은 줄이라면 declaration이므로 제외
                l.append(j+1)
        print("{0}: def in {1}, calls in {2}".format(b,i+1,l))