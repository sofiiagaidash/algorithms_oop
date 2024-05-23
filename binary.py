def binary_search(num1,num2,goal,count = 1):
    result = sum(range(num1,num2+1))//len(range(num1,num2+1))
    print(result)
    if result < goal:
        count += 1
        return binary_search(result,num2,goal,count)

    if result > goal:
        count += 1
        return binary_search(num1,result,goal,count)
    return count

print(binary_search(1,100,44))