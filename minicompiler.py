def lexical_analysis(code):
    print(" Lexical Analysis:")
    tokens = code.replace(';', '').split()
    print("Tokens:", tokens)
    return tokens

def syntax_analysis(tokens):
    print("\n Syntax Analysis:")
    if len(tokens) >= 3 and tokens[1] == '=':
        print("Syntax is valid")
    else:
        print("Invalid Syntax")
    return tokens[0], tokens[2:]

def semantic_analysis(var):
    print("\n Semantic Analysis:")
    if var.isalpha():
        print(f"{var} is a valid variable name")
    else:
        print("Invalid variable name")

def intermediate_code(expr):
    print("\n Intermediate Code Generation:")
    t1 = f"{expr[2]} * {expr[3]}"
    t2 = f"{expr[0]} + t1"
    print("t1 =", t1)
    print("t2 =", t2)
    return "t2"

def optimize():
    print("\n Code Optimization:")
    result = 2 + 3 * 4
    print("t1 = 12")
    print("t2 = 2 + 12 = 14")
    return 14

def target_code(var, value):
    print("\n Target Code Generation:")
    print(f"{var} = {value}")

# === Main Driver ===
code = "a = 2 + 3 * 4;"
tokens = lexical_analysis(code)
var, expr = syntax_analysis(tokens)
semantic_analysis(var)
intermediate = intermediate_code(expr)
value = optimize()
target_code(var, value)
