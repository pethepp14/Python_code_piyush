numbers=[2,3,4,5,6,7,8,9,10]
def composite(numbers):
    composite_num=[]
    for i in numbers:
        if i>1:
            for j in range(2,i):
                if(i%j)==0:
                    composite_num.append(i)
                    break
    return composite_num

print(composite(numbers))