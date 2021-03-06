import Node as nd
import glob
import ast
import sys
import os
import numpy as np
import MCTS

RootState = np.array([1.,1.,1.,1.])
Root = nd.Node(RootState)


if not sys.argv[1]:
  exit('please input dir as argv1')
time_t = 0
class NodeVisitor(ast.NodeVisitor):
    def visit_Str(self, tree_node):
        print("\nTree node:")
        print('{}'.format(tree_node.s))


class NodeTransformer(ast.NodeTransformer):
    def visit_Str(self, tree_node):
        return ast.Str('String: ' + tree_node.s)


#file = open("./vaitp_dataset/train/vulnerable/38b.txt", "r")

"""
tree_node = ast.parse(file.read())


print("\nAST tree:")
print(ast.dump(tree_node))



print("\nAST node visitor:")
NodeTransformer().visit(tree_node)
NodeVisitor().visit(tree_node)
"""

#print("\nAST parser:")
#print(ast.dump(ast.parse(file.read(), mode='exec'), indent=4))

for filename in glob.iglob(f'{sys.argv[1]}/*.txt'):
    print(f'Processing: {filename}')
    astf = f'{os.path.splitext(filename)[0]}.ast'
    f = open(astf,'w')
    fin = open(filename, "r")
    f.write(ast.dump(ast.parse(fin.read(), mode='exec'), indent=4))
    f.close
    fin.close
    print(f'Created AST file: {astf}')





x = MCTS.MCTS(Root)
x.Run()
print("The Time taken for Tradional Monte Carlo is", time_t)
