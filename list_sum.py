def SumList(List):
    sum=0
    for ele in List:
        sum=sum+ele
    return sum




List=list(map(int,input("Please enter list element ").split()))
print(SumList(List))