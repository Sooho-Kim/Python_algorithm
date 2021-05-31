# 학생 수와 그룹 수 할당
n, m = map(int, input().split())

# 키 차이를 넣는 리스트
diff = []

# 학생들의 키 리스트로 만들기 
student = list(map(int, input().split()))

# 학생들의 키 차이 넣기
for i in range(1, len(student)):
    diff.append(student[i] - student[i-1])

# 결과 출력
print(sum(diff[m-1:]))
