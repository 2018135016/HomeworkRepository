t = open("input_7_2.txt").read().upper() #입력을 받아 대문자로 변환
d={}
for i in t:
    if 65<=ord(i)<=90:d[i] = d[i]+1 if i in d else 1 #대문자이면 딕셔너리에 저장
ans=list(d.items())
ans.sort(key=lambda x:(-x[1],x[0])) # 빈도가 작은 것을 기준으로 정렬
print([i[0] for i in ans])