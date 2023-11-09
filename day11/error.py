"""while True:
    try:
        
       number=int(input("Enter a number:"))
       number2=int(input("Enter a number:"))
       print(number/number2)
    except ZeroDivisionError:
        print("Number cannot be divissible by Zero")
    except ValueError:
        print("you didnt enter a String!!")
    except IndexError:
        print("there is index Error")
    except Exception as e:
        raise Exception("unexpected error occurred")
        print("hello")"""
def EqualTOFive(num):
    if num==5:
        raise Exception("Number cannot be five")
    return "ok"
EqualTOFive(2)