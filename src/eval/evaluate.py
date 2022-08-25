import ast
import operator as op

def _operators():
    return {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

class Evaluator:
# supported operators
    def __init__(self, operators = _operators()) -> None:
        self.operators = operators

    def eval_expr(self, expr):
        """
        >>> eval_expr('2^6')
        4
        >>> eval_expr('2**6')
        64
        >>> eval_expr('1 + 2*3**(4^5) / (6 + -7)')
        -5.0
        """
        return self.eval_(ast.parse(expr, mode='eval').body)

    def eval_(self, node):
        operators = self.operators
        eval_ = self.eval_
        if isinstance(node, ast.Num): # <number>
            return node.n
        elif isinstance(node, ast.BinOp): # <left> <operator> <right>
            return operators[type(node.op)](eval_(node.left), eval_(node.right))
        elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
            return operators[type(node.op)](eval_(node.operand))
        else:
            raise TypeError(node)

    def __call__(self, expr):
        print(expr)
        try:
            return self.eval_expr(expr)
        except Exception as e:
            print(e)
