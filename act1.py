#sum of whole numbers
n=int(input("Enter the number till whomes sum you want to find"))
sum=0
for i in range(1, n+1):
    sum=sum+i
    # print("\nSum = ", sum)
print("\n The total sum is", sum)