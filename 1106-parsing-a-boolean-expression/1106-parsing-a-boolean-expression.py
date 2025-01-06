class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parse_and(subExprs):
            subExprBool = [True if x == 't' else False for x in subExprs]
            and_eval = all(subExprBool)
            return 't' if and_eval else 'f'
        def parse_or(subExprs):
            subExprBool = [True if x == 't' else False for x in subExprs]
            or_eval = any(subExprBool)
            return 't' if or_eval else 'f'
        def parse_not(subExpr):
            return 't' if (False if subExpr == 't' else True) else 'f'
        op_stack = []
        val_stack = []
        for e in expression:
            if e == '&' or e == '|' or e == '!':
                op_stack.append(e)
            if e == '(' or e== 'f' or e == 't':
                val_stack.append(e)
            if e == ')':
                op = op_stack.pop()
                vals = []
                pop_val = val_stack.pop() 
                while pop_val != '(':
                    vals.append(pop_val)
                    pop_val = val_stack.pop() 
                if op == '&':
                    val_stack.append(parse_and(vals))
                if op == '|':
                    val_stack.append(parse_or(vals))
                if op == '!':
                    val_stack.append(parse_not(vals[0]))
        return True if val_stack.pop() == 't' else False