input()
arr = list(map(int,input().split()))
maxi,cur = 0,0
for i in range(len(arr)):
    cur+= arr[i]
    maxi = max(maxi, cur/(i+1))
cur = 0 
count = 0 
for i in range(len(arr)-1,-1,-1):
    cur+=arr[i]
    count+=1
    maxi = max(maxi,cur/(count))
print(maxi)