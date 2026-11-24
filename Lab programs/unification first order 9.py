
import re

def is_variable(term):
    return term.islower() and term.isalpha()


def parse(term):
    term = term.strip()

    if "(" not in term:
        return term, []

    name = term[:term.index("(")]
    inside = term[term.index("(") + 1:-1]

    args = []
    depth = 0
    current = ""

    for ch in inside:
        if ch == "," and depth == 0:
            args.append(current.strip())
            current = ""
        else:
            current += ch

            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1

    if current.strip():
        args.append(current.strip())

    return name, args


def apply_substitution(term, theta):
    if is_variable(term):
        if term in theta:
            return apply_substitution(theta[term], theta)
        return term

    name, args = parse(term)

    if not args:
        return term

    new_args = [
        apply_substitution(arg, theta) for arg in args
    ]

    return name + "(" + ", ".join(new_args) + ")"


def occurs(variable, term, theta):
    term = apply_substitution(term, theta)

    if variable == term:
        return True

    name, args = parse(term)

    for arg in args:
        if occurs(variable, arg, theta):
            return True

    return False


def unify(expression1, expression2):
    theta = {}
    equations = [(expression1, expression2)]

    while equations:

        s, t = equations.pop(0)

        s = apply_substitution(s, theta)
        t = apply_substitution(t, theta)

        if s == t:
            continue

        elif is_variable(s):

            if occurs(s, t, theta):
                return None

            theta[s] = t

        elif is_variable(t):

            if occurs(t, s, theta):
                return None

            theta[t] = s

        else:
            name1, args1 = parse(s)
            name2, args2 = parse(t)

            if not args1 and not args2:
                return None

            if name1 != name2 or len(args1) != len(args2):
                return None

            for a, b in zip(args1, args2):
                equations.append((a, b))

    for key in theta:
        theta[key] = apply_substitution(theta[key], theta)

    return theta


def run_test_case(number, title, exp1, exp2, note=""):
    print("\n========================================")
    print("TEST CASE", number, ":", title)
    print("Expression 1:", exp1)
    print("Expression 2:", exp2)

    result = unify(exp1, exp2)

    if result is None:
        print("MGU: FAILURE")
        print("Result: Unification failed.")
    else:
        print("MGU:", result)
        print("Result: Unification successful.")

    if note:
        print(note)


run_test_case(
    1,
    "Successful Unification with Two Variables",
    "P(x, a)",
    "P(b, y)"
)


run_test_case(
    2,
    "Successful Unification with Predicate Arguments",
    "Knows(John, x)",
    "Knows(y, Mary)"
)


run_test_case(
    3,
    "Successful Unification with Compound Terms",
    "f(x, g(a))",
    "f(g(y), g(a))",
    "Variable y remains unbound."
)


run_test_case(
    4,
    "Failure Due to Inconsistent Variable Substitution",
    "Loves(x, x)",
    "Loves(John, Mary)"
)


run_test_case(
    5,
    "Failure Due to Occurs Check",
    "x",
    "f(x)"
)

print("\n========================================")
print("ALL TEST CASES COMPLETED")
