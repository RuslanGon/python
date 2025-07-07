# x = int(input('Введите число: '))

# if x == 2:
#     print('Число равно двум')
# elif x > 0:
#     print('Число положительное')
# elif x == 0:
#     print('Число равно нулю')
# else:
#     print('Число отрицательное')
# ////////////////////////////////

# name = input("Enter name: ")

# if name.strip():  # .strip() удаляет пробелы и пустые строки
#     print(name)
# else:
#     print('You did not enter a name')

# a = False
# b = True
# if a:
#     if b:
#         print(1)
#     else:
#         print(2)
# else:
#     if b:
#         print(3)
#     else:
#         print(4)
            
# a = int(input('Enter your number'))
# if 10< a <20:
#     print('helo')

# a = int(input('Enter Your Number'))
# if a == 8 or a == 12:
#     print(a)
# elif a > 10 and a < 100:
#     print(a,'big')
        
# else:
#     print('hello')

# a = int(input('number'))
# if a == 8 or a == 12:
#     print(a)
# elif a < 10:
#     pass
        
# else:
#     print('hello')

# a = int(input('Your number'))
# if a < 20:
#     number = a
# else:
#     number = a
# print(number)    
    
    
# a = int(input('Your number'))
# x = a if 10 < a <100 else 'not number'
# print(x)

# print('1 - comedy')
# print('2 - love')
# print('3 - fantasy')

# x = int(input("What genre? ")) 

# if x == 1:
#     print('You chose comedy')
# elif x == 2:
#     print('You chose love story')
# elif x == 3:
#     print('You chose fantasy')
# else:
#     print('Unknown genre')

print('1 - comedy')
print('2 - love')
print('3 - fantasy')

x = int(input("What genre? ")) 

match x:
    case 1:
        print('You chose comedy')
    case 2:
        print('You chose love story')
    case 3:
        print('You chose fantasy')
    case _:
        print('Unknown genre') 
    



