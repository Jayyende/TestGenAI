def generate_documentation(functions):

    docs = {}

    for func in functions:

        if "add" in func.lower():

            docs[func] = (
                "Adds two values and returns the result."
            )

        elif "subtract" in func.lower() or "sub" in func.lower():

            docs[func] = (
                "Subtracts one value from another."
            )

        elif "multiply" in func.lower() or "mul" in func.lower():

            docs[func] = (
                "Multiplies two values."
            )

        elif "divide" in func.lower():

            docs[func] = (
                "Divides one value by another."
            )

        else:

            docs[func] = (
                "User defined function."
            )

    return docs