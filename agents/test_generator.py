def generate_test_cases(functions):

    test_cases = {}

    for func in functions:

        if "add" in func.lower():

            test_cases[func] = [
                "add(5,3) = 8",
                "add(0,0) = 0"
            ]

        elif "subtract" in func.lower() or "sub" in func.lower():

            test_cases[func] = [
                "subtract(10,5) = 5",
                "subtract(20,10) = 10"
            ]

        elif "multiply" in func.lower() or "mul" in func.lower():

            test_cases[func] = [
                "multiply(4,5) = 20",
                "multiply(0,10) = 0"
            ]

        else:

            test_cases[func] = [
                f"{func}(sample input)"
            ]

    return test_cases