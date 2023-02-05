import math            # Importing math module for sqrt() function

 # Function to find roots of quadratic equation 
 
def quadratic_equation(a, b, c):  
    discriminant = (b**2) - (4*a*c)
    sqrt_val = (b**2) - (4*a*c)**0.5
    root1 = (-b + sqrt_val) / (2 * a)
    root2 = (-b - sqrt_val) / (2 * a)
    
    # Checking condition for discriminant
    
    if discriminant > 0:
        return f"Roots are real and different.\nRoot 1: {root1}\nRoot 2: {root2}" # Returning roots  if discriminant is positive
    elif discriminant == 0:
        return f"Roots are real and same.\nRoot: {root1}" # Returning root  if discriminant is 0
    else:
        return "Roots are complex and different." # Returning roots are complex and different 



def main():         # Main function to call the calculator function
    while True:     # While loop to continue the program until user wants to exit the program
        menu = (
                "***MENU***\n"
                "1. ADDITION\n"
                "2. SUBTRACTION\n"
                "3. MULTIPLICATION\n"
                "4. DIVISION\n"
                "5. SQUARE\n"
                "6. CUBE\n"
                "7. MODULUS\n"
                "8. EXPONENTIAL\n"
                "9. QUADRATIC EQUATION\n"
                "10.EXIT\n"
             "Enter your choice: "
)
        choice = int(input(menu))         # Taking input from user for choice of operation
        

        if choice == 10:                  # If user wants to exit the program
            break
     
        elif choice == 9:                # If user wants to find roots of quadratic equation 
          a = float(input("Enter the coefficient 'a' of x^2: "))
          b = float(input("Enter the coefficient 'b' of x: "))
          c = float(input("Enter the constant 'c': "))
          result = quadratic_equation(a, b, c)
          print(f"Result: {result}\n")
          
        elif choice not in range(1,10):   # If user enters any other choice other than 1-10 then it will print invalid choice
            print("Error: Please enter a valid choice between 1 and 10\n")
            continue                 # Continue the loop if user enters invalid choice and ask for input again
          
        else:       #start calculation if user enters valid choice
            num1 = float(input("Enter the num1 for calculation: "))
            num2 = float(input("Enter the num2 for calculation: "))
            
        if choice == 1:
            ADD = num1 + num2
            print(f"ADD = {num1} + {num2} = {ADD}\n")
        elif choice == 2:
            SUB = num1 - num2
            print(f"SUB = {num1} - {num2} = {SUB}\n")
        elif choice == 3:
            MUL = num1 * num2
            print(f"MUL = {num1} * {num2} = {MUL}\n")
        elif choice == 4:
            DIV = num1 / num2
            print(f"DIV = {num1} / {num2} = {DIV}\n")
        elif choice == 5:
            SQR1 = num1 * num1
            SQR2 = num2 * num2
            print(f"SQR1 = ({num1})^2 = {SQR1}\n")
            print(f"SQR2 = ({num2})^2 = {SQR2}\n")
        elif choice == 6:
            CUBE1 = num1 * num1 * num1
            CUBE2 = num2 * num2 * num2
            print(f"CUBE1 = ({num1})^3 = {CUBE1}\n")
            print(f"CUBE2 = ({num2})^3 = {CUBE2}\n")
        elif choice == 7:
            MOD = num1 % num2
            print(f"MOD = {num1} % {num2} = {MOD}\n")
        elif choice == 8:
            EXP = num1 ** num2
            print(f"EXP = {num1} ** {num2} = {EXP}\n")
       
        else:        # If user enters any other choice other than 1-10 then it will print invalid choice
            print("\n***THANK YOU***\n")
            
        
        
        continue_program = input("Do you want to continue the program? (y/n): ") # Asking user if he wants to continue the program
        if continue_program.lower() == "n": # If user enters n then it will end the program
            break
    print("\n***THANK YOU***\n")

main()  # Calling the main function

