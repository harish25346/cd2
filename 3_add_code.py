 # Three Address Code Generator

temp_counter = 1

def make_TAC(expression):
    global temp_counter
    expression = expression.strip()

    # Base case: if it's a single variable or number
    if all(c.isalnum() for c in expression):
        return expression

    # Handle parentheses first
    bracket_count = 0
    for i, char in enumerate(expression):
        if char == '(':
            bracket_count += 1
        elif char == ')':
            bracket_count -= 1
        elif bracket_count == 0 and char in '+-*/':
            # Split expression at the operator
            left = make_TAC(expression[:i])
            right = make_TAC(expression[i+1:])
            temp_var = f"t{temp_counter}"
            print(f"{temp_var} = {left} {char} {right}")
            temp_counter += 1
            return temp_var

    # If the expression is wrapped in parentheses
    if expression[0] == '(' and expression[-1] == ')':
        return make_TAC(expression[1:-1])

    raise ValueError("Invalid expression format")

# Main program
print("Three Address Code Generator")
print("Enter expressions in the form: result = a + b * (c - d)")
print("Type 'quit' to exit\n")

while True:
    user_input = input("Enter expression like  x = a + b * (c - d): ").strip()
    if user_input.lower() == 'quit':
        break
    
    try:
        if '=' in user_input:
            var_name, expr = user_input.split('=', 1)
            var_name = var_name.strip()
            expr = expr.strip()
            
            print("\nGenerated Three Address Code:")
            final_result = make_TAC(expr)
            print(f"{var_name} = {final_result}\n")
        else:
            print("Error: Expression must contain '=' sign\n")
    except Exception as e:
        print(f"Error: {str(e)}\n")
