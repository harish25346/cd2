# This variable is used to name temporary variables like t1, t2, etc.
temp_counter = 1

# Function to break an expression into smaller steps
def make_TAC(expression):
    global temp_counter
    expression = expression.strip()

    # If it's a single variable or number, just return it
    if expression.isalnum():
        return expression

    # Go through each operator (+, -, *, /) to break the expression
    for op in '+-*/':
        bracket_count = 0

        # Go from right to left so we handle the last operator first
        for i in range(len(expression) - 1, -1, -1):
            char = expression[i]

            if char == ')':
                bracket_count += 1
            elif char == '(':
                bracket_count -= 1
            elif bracket_count == 0 and char == op:
                # Split expression into left and right parts
                left = make_TAC(expression[:i])
                right = make_TAC(expression[i + 1:])
                temp_var = f"t{temp_counter}"
                print(f"{temp_var} = {left} {op} {right}")
                temp_counter += 1
                return temp_var

    # If expression is inside brackets, remove them and try again
    return make_TAC(expression[1:-1])

# Get input from user like: a = b + c * (d - e)
user_input = input("Enter expression (e.g., a = b + c * (d - e)): ")
var_name, expr = user_input.split('=', 1)
var_name = var_name.strip()
expr = expr.strip()

print("\nThree Address Code:")
final_result = make_TAC(expr)
print(f"{var_name} = {final_result}")
