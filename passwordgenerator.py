def generator():
    print("Welcome to password generator app, we provide you with strong and secured passwords if you need one")
    while True:
        print("Kindly type okay to continue")
        ans = input()
        if ans=="OKAY" or ans=="OK" or ans=="Ok" or ans=="kk" or ans=="okay" or ans=="Okay" or ans=="ok":
            import random
            chars = "abcde!fg@hi#jk$lm%no&pq?rs/tu>vw<xyz132649[58]70AS\DF=GHJKLMPNOBIVUCYXTZREWQ"
            print("please enter how many passwords you want us to generate for you?")
            number = int(input())
            print("What about the lenght, how many characters do you want your password to contain?")
            length = int(input())
            for p in range(number):
                password = ""
                for c in range(length):
                    password += random.choice(chars)
                print(password)
            break
        else:
            continue

      
                
            
            
                
            
        
