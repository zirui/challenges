import sys
#import psyco
#psyco.full()

op = ['+','-','*','/']
precedence = {k:v for k,v in zip(op,range(len(op)))}
#print precedence

def is_operator(ch):
    return ch in ('+','-','*','/','^')

def is_operand(ch):
    return 'a' <= ch <= 'z'

def rpn(infix_notion):
    rst = ''
    op_stk = []
    for ch in infix_notion:
        if is_operand(ch):
            rst += ch 
        elif is_operator(ch):
            while len(op_stk) > 0 and is_operator(op_stk[-1]) and precedence[ch] < precedence[op_stk[-1]]:
                rst += op_stk.pop()
            op_stk.append(ch)
        elif ch == '(':
            op_stk.append(ch)
        elif ch == ')':
            while op_stk[-1] is not '(':
                rst += op_stk.pop()

            op_stk.pop() # pop '('
        
    while len(op_stk) > 0:
        rst += op_stk.pop()
    return rst



case_num = input()
for i in xrange(0,case_num):
    infix_notation = sys.stdin.readline()
    print rpn(infix_notation)


