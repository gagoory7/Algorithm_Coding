import sys

n, m = map(int, sys.stdin.readline().split())

str_dic = {}

for _ in range(n):
    tmp = sys.stdin.readline().strip()  # 줄바꿈 제거
    if len(tmp) >= m:  # 길이 조건 확인
        if tmp in str_dic:
            str_dic[tmp] += 1
        else:
            str_dic[tmp] = 1

# 정렬: (빈도수 내림차순, 길이 내림차순, 알파벳 오름차순)
sorted_dict = sorted(
    str_dic.items(),
    key=lambda item: (-item[1], -len(item[0]), item[0])
)

# 출력
for i, _ in sorted_dict:
    print(i)