def ClosestMinMax(array):
    mini=float('inf')
    maxi=-float('inf')
    n=len(array)
    for i in range(n):
        if array[i]<mini:
            mini=array[i]
        elif array[i]>maxi:
            maxi=array[i]
    r_min=-1
    r_max=-1
    res=n
    for i in range(n):
        if array[i]==maxi:
            r_max=i
            if r_min>=0:
                res=min(res,i-r_min+1)
        elif array[i]==mini:
            r_min=i
            if r_max>=0:
                res=min(res,i-r_max+1)
    return res

array = list(map(int, input().split()))
print(ClosestMinMax(array))