with open('day18.txt' , 'r') as f:
    lines = f.readlines()

# Return x op y.
def do_operation(x, y, op):
    if(op == '+'):
        return x + y
    elif(op == '*'):
        return x * y
    else:
        return -1

# Preprocessing: instead of x)) do x) + 0) to simplify things.
new_lines = []
for l in lines:
    i = 0
    while(i < len(l) - 1):
        if(l[i] == ')' and l[i+1] == ')'):
            l = l[:i+1] + " + 0" + l[i+1:]
        i += 1
    new_lines.append(l)

lines = new_lines

# Preprocessing: instead of )( do ) * (.
new_lines = []
for l in lines:
    i = 0
    while(i < len(l) - 1):
        if(l[i] == ')' and l[i+1] == '('):
            l = l[:i+1] + " * " + l[i+1:]
        i += 1
    new_lines.append(l)

lines = new_lines

# Preprocessing: instead of (( do (0 + (.
new_lines = []
for l in lines:
    i = 0
    while(i < len(l) - 1):
        if(l[i] == '(' and l[i+1] == '('):
            l = l[:i+1] + "0 + " + l[i+1:]
        i += 1
    new_lines.append(l)

lines = new_lines

print(lines)

total = 0

for l in lines:
    print(l)
    # The stack contains the accumulated value and operation
    # before the parenthesis.
    stack = []

    symbols = l.split()

    acc = 0

    # Solve the arithmetic. We first get the starting value "x" or "(x"" and
    # then we get "op" and "x" over and over until we're done.
    idx = 0
    while(idx < len(symbols)):
        symbol = symbols[idx]
        # print(stack, acc, symbol)
        # If we see "x" then we're starting with the first value.
        if(symbol.isdigit()):
            acc = int(symbol)
            idx += 1
        # If we start with "(x" then we must be starting
        # the entire sequence with '('. In this case it's the
        # equivalent of '0 + (' so we put that on the stack.
        elif(symbol.startswith('(')):
            stack.append((acc, '+'))
            acc = int(symbol[1:])
            idx += 1
        # If we have addition or multiplication then also
        # get the value after to do the operation.
        elif(symbol == '+' or symbol == '*'):
            next_symbol = symbols[idx+1]
            # If the next symbol is a number then we do the operation.
            if(next_symbol.isdigit()):
                acc = do_operation(acc, int(next_symbol), symbol)
                idx += 2
            # If the next symbol is a '(' then we put our op on the
            # stack and get ready to solve the parenthesis first.
            elif(next_symbol.startswith('(')):
                stack.append((acc, symbol))
                acc = int(next_symbol[1:])
                idx += 2
            # If we have 'x)' then we do that op end the current stack and do the
            # operation. From the preprocessing we're guaranteed there won't be any
            # next symbols with 'x))'.
            elif(next_symbol.endswith(')')):
                # Do the operation and then end the stack.
                # print(next_symbol, len(next_symbol.strip()))
                acc = do_operation(acc, int(next_symbol.strip()[:-1]), symbol)
                # Save the current acc as the second operand for the stack's saved
                # operation.
                val = acc
                # Pop the stack.
                acc, op = stack[-1]
                stack = stack[:-1]
                acc = do_operation(acc, val, op)
                idx += 2

    print(acc)
    total += acc

print(total)

