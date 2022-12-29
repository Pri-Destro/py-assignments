n=int(input("Enter number of fibonacci series:\n "))
if n<=0 :
    print("Enter number greater than zero.")
else:
    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    else:
        list1 = [1, 1]
        a = 1
        b = 1
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        print(f"\nThe fibonacci series with {n} elements is shown below:")
        print(list1)
        sum = 0 
        for num in list1:
            sum = sum + num
        average = (sum / n)

        two_decimal = "{:.2f}".format(average)
        
        print(f"\nAverage of given fibonacci series is {two_decimal}")