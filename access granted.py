#THIS CODE GRANTS THE USER ACCES TO A COMPUETR IF THE INFO. PROVIDED IS TRUE
while True:
    print('What is your name')
    name = input()
    if name != 'Kesse':
        print('it is not you dude')
        break
    print('Hello, Mr. Kesse. What is your age?')
    age = int(input())
    if age != 19:
        print("Haahahah... you tried man, its not you get off!!!")
        break
    print('So where were you born?')
    town = input()
    if town == 'Santasi':
        print("access granted")
        break
    else:
         print("Go away intruder!!")
         break 

