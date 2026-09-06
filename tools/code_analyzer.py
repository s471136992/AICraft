"""
AICraft Code Analyzer

A simple tool for analyzing Python code.
"""

import ast
import sys


def analyze_file(filename):

    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()

    tree = ast.parse(code)

    functions = []
    classes = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        if isinstance(node, ast.ClassDef):
            classes.append(node.name)


    print("AICraft Code Analysis")
    print("---------------------")

    print("Functions:", len(functions))
    print("Classes:", len(classes))


if __name__ == "__main__":

    analyze_file(sys.argv[1])
