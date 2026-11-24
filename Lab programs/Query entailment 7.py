from itertools import product

def extract_symbols(kb, query):
    symbols = set()

    def find_symbols(expr):
        if isinstance(expr, str):
            symbols.add(expr)
        else:
            for item in expr[1:]:
                find_symbols(item)

    for sentence in kb:
        find_symbols(sentence)

    find_symbols(query)
    return sorted(symbols)


def evaluate(expr, assignment):
    if isinstance(expr, str):
        return assignment[expr]

    operator = expr[0]

    if operator == "NOT":
        return not evaluate(expr[1], assignment)

    elif operator == "AND":
        return evaluate(expr[1], assignment) and evaluate(expr[2], assignment)

    elif operator == "OR":
        return evaluate(expr[1], assignment) or evaluate(expr[2], assignment)

    elif operator == "IMPLIES":
        return (not evaluate(expr[1], assignment)) or evaluate(expr[2], assignment)

    elif operator == "IFF":
        return evaluate(expr[1], assignment) == evaluate(expr[2], assignment)


def check_entailment(kb, query):
    symbols = extract_symbols(kb, query)

    for values in product([False, True], repeat=len(symbols)):
        assignment = dict(zip(symbols, values))

        kb_value = all(evaluate(sentence, assignment) for sentence in kb)

        if kb_value:
            query_value = evaluate(query, assignment)

            if not query_value:
                print("NOT ENTAILED")
                print("Counterexample:", assignment)
                return False

    print("ENTAILED")
    return True


print("\nTest Case 1:")
check_entailment(
    ["P"],
    "P"
)

print("\nTest Case 2:")
check_entailment(
    [("IMPLIES", "P", "Q"), "P"],
    "Q"
)

print("\nTest Case 3:")
check_entailment(
    [("OR", "P", "Q")],
    "P"
)

print("\nTest Case 4:")
check_entailment(
    [("AND", "P", "Q")],
    "Q"
)

print("\nTest Case 5:")
check_entailment(
    [("IMPLIES", "P", "Q")],
    "P"
)
