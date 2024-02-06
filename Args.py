def add(*n):
    sum = 0 
    nums = list(n)
    nums[0] = 0
    for i in nums:
        sum+=i
    return sum

print(add(8,1,8,90))