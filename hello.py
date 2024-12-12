#This is a comment
def main()-> None:
    """_summary_
    """
    print("Hello, World")
    num1, num2 = map(int, input("Enter two numbers: ").split(" "))
    print(add(num1=num1, num2=num2))

def add(num1: int, num2: int)-> int:
    return num1 +  num2

if __name__ == "__main__":
    #Main comment
    
    main()
    
    
    
    
    