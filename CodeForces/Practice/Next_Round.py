t, mini = map(int, input().split())
arr = list(map(int, input().split()))
check = arr[mini-1]
ans = 0
for i in arr:
    if i >= check and i > 0:
        ans += 1
print(ans)