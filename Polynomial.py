#ask user to input the polynomial
expr = input("Enter the multiplication of polynomials: ")

#we remove spaces from the expression
expr = expr.replace(' ', '')

#we initialize an empty list for tokens
tokens = []
i = 0

#we start tokenizing the expression
while i < len(expr):
    c = expr[i]
    if c.isdigit():
        #if c is a digit, we collect the whole number
        num = c
        i += 1
        while i < len(expr) and expr[i].isdigit():
            num += expr[i]
            i += 1
        tokens.append(num)
        #if a variable follows the number, we add '*'
        if i < len(expr) and expr[i].isalpha():
            tokens.append('*')
    elif c.isalpha():
        #if c is a letter, we collect the full variable name
        var = c
        i += 1
        while i < len(expr) and expr[i].isalpha():
            var += expr[i]
            i += 1
        #if a digit follows, it's an exponent
        if i < len(expr) and expr[i].isdigit():
            tokens.append(var)
            tokens.append('^')
            num = ''
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(num)
        else:
            tokens.append(var)
    elif c in '+-*/^()':
        #if c is an operator or parenthesis, we add it to tokens
        tokens.append(c)
        i += 1
    else:
        #we ignore other characters
        i += 1

#we insert '*' where necessary
i = 0
while i < len(tokens) - 1:
    curr = tokens[i]
    next = tokens[i + 1]
    if (curr.isdigit() or curr.isalpha() or curr == ')') and (next.isdigit() or next.isalpha() or next == '('):
        tokens.insert(i + 1, '*')
    i += 1

#we convert tokens to postfix notation
output = []
stack = []
precedence = {'+': 1, '-': 1, '*': 2, '^': 3}

for token in tokens:
    if token.isdigit() or token.isalpha():
        #operands go to output
        output.append(token)
    elif token == '(':
        #push '(' to stack
        stack.append(token)
    elif token == ')':
        #pop until '('
        while stack and stack[-1] != '(':
            output.append(stack.pop())
        stack.pop()  #remove '('
    else:
        #operators
        while stack and stack[-1] != '(' and precedence.get(token, 0) <= precedence.get(stack[-1], 0):
            output.append(stack.pop())
        stack.append(token)

#pop remaining operators
while stack:
    output.append(stack.pop())

postfix = output

#evaluate postfix expression
stack = []

for token in postfix:
    if token.isdigit():
        #push numbers as terms with coef and empty vars
        stack.append([{'coef': int(token), 'vars': {}}])
    elif token.isalpha():
        #push variables as terms with coef=1 and vars
        stack.append([{'coef': 1, 'vars': {token: 1}}])
    elif token == '^':
        #exponentiation
        exp = stack.pop()
        base = stack.pop()
        exponent = exp[0]['coef']
        result = []
        for term in base:
            #multiply powers by exponent
            term_vars = {var: power * exponent for var, power in term['vars'].items()}
            #coef to the exponent
            term_coef = term['coef'] ** exponent
            result.append({'coef': term_coef, 'vars': term_vars})
        stack.append(result)
    elif token in '+-*':
        #binary operators
        b = stack.pop()
        a = stack.pop()
        if token == '+':
            #addition
            result = a + b
            #combine like terms
            combined = {}
            for term in result:
                key = tuple(sorted(term['vars'].items()))
                if key in combined:
                    combined[key]['coef'] += term['coef']
                else:
                    combined[key] = {'coef': term['coef'], 'vars': term['vars']}
            result = [term for term in combined.values() if term['coef'] != 0]
            stack.append(result)
        elif token == '-':
            #subtraction
            neg_b = [{'coef': -term['coef'], 'vars': term['vars']} for term in b]
            result = a + neg_b
            #combine like terms
            combined = {}
            for term in result:
                key = tuple(sorted(term['vars'].items()))
                if key in combined:
                    combined[key]['coef'] += term['coef']
                else:
                    combined[key] = {'coef': term['coef'], 'vars': term['vars']}
            result = [term for term in combined.values() if term['coef'] != 0]
            stack.append(result)
        elif token == '*':
            #multiplication
            result = []
            for term_a in a:
                for term_b in b:
                    #multiply coefficients
                    coef = term_a['coef'] * term_b['coef']
                    #add exponents
                    vars = term_a['vars'].copy()
                    for var, power in term_b['vars'].items():
                        vars[var] = vars.get(var, 0) + power
                    result.append({'coef': coef, 'vars': vars})
            #combine like terms
            combined = {}
            for term in result:
                key = tuple(sorted(term['vars'].items()))
                if key in combined:
                    combined[key]['coef'] += term['coef']
                else:
                    combined[key] = {'coef': term['coef'], 'vars': term['vars']}
            result = [term for term in combined.values() if term['coef'] != 0]
            stack.append(result)

#final result
terms = stack[0]

#format terms in explicit format (* and ^)
terms_explicit = sorted(terms, key=lambda x: (-sum(x['vars'].values()), sorted(x['vars'].items())))
result_explicit = ''
for term in terms_explicit:
    coef = term['coef']
    vars = term['vars']
    vars_str = ''
    for var in sorted(vars):
        power = vars[var]
        if power == 1:
            vars_str += f'*{var}'
        else:
            vars_str += f'*{var}^{power}'
    if coef > 0 and result_explicit:
        result_explicit += ' + '
    elif coef < 0:
        result_explicit += ' - ' if result_explicit else '-'
    elif coef == 0:
        continue
    else:
        result_explicit += ''
    abs_coef = abs(coef)
    if abs_coef != 1 or not vars:
        result_explicit += f'{abs_coef}'
        result_explicit += vars_str
    else:
        result_explicit += vars_str[1:]  #remove leading '*'
    if abs_coef == 1 and vars_str:
        result_explicit = result_explicit.replace('1*', '', 1)
explicit = result_explicit.strip()

#format terms in implicit format
terms_implicit = sorted(terms, key=lambda x: (-sum(x['vars'].values()), sorted(x['vars'].items())))
result_implicit = ''
for term in terms_implicit:
    coef = term['coef']
    vars = term['vars']
    vars_str = ''
    for var in sorted(vars):
        power = vars[var]
        if power == 1:
            vars_str += var
        else:
            vars_str += f'{var}{power}'
    if coef > 0 and result_implicit:
        result_implicit += ' + '
    elif coef < 0:
        result_implicit += ' - ' if result_implicit else '-'
    elif coef == 0:
        continue
    else:
        result_implicit += ''
    abs_coef = abs(coef)
    if abs_coef != 1 or not vars:
        result_implicit += f'{abs_coef}'
        if vars_str:
            result_implicit += vars_str
    else:
        result_implicit += vars_str
implicit = result_implicit.strip()

#display results
print("Resulting polynomial in explicit format (* and ^):")
print(explicit)
print("\nResulting polynomial in implicit format (2X and X2):")
print(implicit)
