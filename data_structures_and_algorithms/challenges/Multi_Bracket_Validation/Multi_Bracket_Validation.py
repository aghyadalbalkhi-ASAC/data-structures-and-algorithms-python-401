# Multi Bracket Validation 

def multi_bracket_validation(input):
    stack = []
    brackets ={
        '{':'}',
        '(':')',
        '[':']'
    }
    for char in input:
        if char in brackets:
            stack.append(char)
        if char in  brackets.values():
            # print(stack)
            # print(char)
            if char==brackets[stack[-1]]:
                # print('access pop')
                stack.pop()

    if len(stack)==0:
        return True
    else:

        return False


if __name__ == "__main__":
    print(multi_bracket_validation('{}'))
    print(multi_bracket_validation('{}(){}'))
    print(multi_bracket_validation('()[[Extra Characters]]'))
    print(multi_bracket_validation('(){}[[]]'))
    print(multi_bracket_validation('{}{Code}[Fellows](())'))
    print(multi_bracket_validation('[({}]'))
    print(multi_bracket_validation('(]('))
    print(multi_bracket_validation('{(})'))


