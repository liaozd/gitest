import ast

file = open('test.py', 'r')
source = file.read()


class NodeVisitor(ast.NodeVisitor):

    def visit_ClassDef(self, node):
        print node

node = ast.parse(source)

visitor = NodeVisitor()
visitor.visit(node)
