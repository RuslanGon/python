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

# print('1 - comedy')
# print('2 - love')
# print('3 - fantasy')

# x = int(input("What genre? ")) 

# match x:
#     case 1:
#         print('You chose comedy')
#     case 2:
#         print('You chose love story')
#     case 3:
#         print('You chose fantasy')
#     case _:
#         print('Unknown genre') 
    

# print('1-Matematica')
# print('2-Fizika')
# print('3-Istiry')

# lessons = int(input('What lesson now '))

# match lessons:
#     case 1 | 2:
#         print("now Matematica") 
#     case 2:
#         print("now Fizika") 
#     case 3:
#         print("now Istory") 
#     case 4:
#         print('not lessons')     
            

# number = int(input('Enter your number'))   

# if number % 2 == 0:
#      print('number parne') 
# else:
#     print('nomber not parne')    

# x = 1
# while x <= 10:
#     if x % 2 == 0 and x % 3 == 0:
#         print(x)
#     x += 1

x = r = 1
while x < 10:
    while r < 10:
        print(x, "*", r, '=', x * r, end='|')
        r +=1
    print()    
    r = 1
    x +=1




