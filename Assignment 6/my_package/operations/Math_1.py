def get_average():
    x = int(input('enter the number of list items: '))
    list1=[]
    summ=0
    for i in range(x):
        list1.append(int(input(f'enter the {i} number: ')))
        summ+=list1[i]
    average_num=summ/len(list1)
    return print(f"the average is {average_num}")
