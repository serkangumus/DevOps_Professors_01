c = int(input('''Please chose your operation :\n1.addition\n2.substraction
3.Multiplication\n4.Division\n5.Fibonacci number up to your number
6.Summation of integers that are divided by 3 or 5 up to your number(inclusive)\n\n'''))
if c < 5:
    a = int(input("Welcome to calculator:\n\nPlease enter your first number : "))
    b = int(input("Please enter your second number : "))
    result = {1:a+b,2:a-b,3:a*b,4:a/b}
    operations = {1: 'multiplication',
              2: 'substraction',
              3: 'multiplication',
              4: 'division'
     }

    print('\nThe result of {} is {}'.format(operations[c],result[c]))
    
elif c == 5:
    d = int(input("Please enter your number between 10 and 10.000 : "))
    x = [1,1]
    for i in range(d):
        if x[i]+x[i+1] > d: break
        x.append(x[i]+x[i+1])
    print('Finocci numbers up to {} are {}'.format(d, x))

elif c == 6 :
    f = int(input("Please enter your number : "))
    B = sum(set(range(0,int(f)+1,3))| set(range(0,int(f)+1,5)))
    print('Summation of integers that divided by 3 or 5 up to {}(inclusive) are {}'.format(f, B))
     
else:
       print('Please enter valid number')