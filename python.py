right=int(input('input the value of right factur:'))
left=int(input('input the value of left factur:'))
if left>0 and right>0:
    pass
elif left>0 and right<0:
    temp = left
    left = right
    right = temp
    pass
elif left<0 and right>0:
    pass
elif left<0 and right<0:
    right = abs(right)
    left = abs(left)
    pass
total = 0 #(accumula for addition)
i = 1  #specify the loop variable(i=1)
while i <= right:
    total=total+left
    i=i+1
    pass
print(total)   #(this is the result of left and right)

