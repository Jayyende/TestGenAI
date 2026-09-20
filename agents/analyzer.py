import ast

def analyze_code(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        code = file.read()

    tree = ast.parse(code)

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    return functions