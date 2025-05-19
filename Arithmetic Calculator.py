while True:     #makes sure the program is always running unless false is returned or the loop is broken
    expression = input("Enter an arithmetic expression or 'q' to quit: ")   #lets users input the arithmetic expression
    if expression == 'q':
        quit()   #lets user end the program by using the quit() function. We could also use break or exit()

    par = []  #an empty list that can be modified later to indicate whether there is an opening parantheses or not
    end_par = False #indicates the ending parantheses as existing if it is False and true if it exists
    for char in expression:
        if char == '(':
            par.append(char)    #appendds it to the par list if there is an ending paranthesis
        elif char == ')':
            if not par: #if there is only an ending parantheses, changes end_par into True
                end_par = True
                break
            par.pop()  #remove the matching '(' from the stack

    if par or end_par:  #error message if one of the parantheses, either opening or ending do not both exist
        print("Error: Unbalanced parentheses.")
        continue

    try:    #uses try to only evaluate the expression when there are no errors. if there were errors, print what error it was
        result = eval(expression)   #uses eval to evaluate the expression. If eval is not allowed to be used, we can use HW3_p2 and modify some parts to include parantheses'
        #expressions to evaluate the expressions
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except SyntaxError:
        print("Error: Unsupported character.")
    except NameError:
        print("Error: Operand error.")
