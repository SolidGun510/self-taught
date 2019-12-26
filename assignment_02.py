numbers = [1, 5, 7, 11, 14]

while True:
    a=input("Enter a number or 'q' to quit")
    try:
        if a == 'q':
            break
        if int(a) in numbers:
            print("number is present")
        else:
            print("number is not in list")
    except:
        print("not a valid response, try again")
        
