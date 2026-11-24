
def resolve(c1, c2):
    resolvents = set()

    for literal in c1:
        complement = "~" + literal if not literal.startswith("~") else literal[1:]

        if complement in c2:
            new_clause = (c1 - {literal}) | (c2 - {complement})

            tautology = False

            for item in new_clause:
                opposite = "~" + item if not item.startswith("~") else item[1:]

                if opposite in new_clause:
                    tautology = True
                    break

            if not tautology:
                resolvents.add(frozenset(new_clause))

    return resolvents


def resolution_prove(kb, query):
    clauses = set(frozenset(c) for c in kb)

    negated_query = "~" + query if not query.startswith("~") else query[1:]
    clauses.add(frozenset([negated_query]))

    print("\nInitial Clauses:")
    for clause in clauses:
        print(clause)

    step = 1

    while True:
        new_clauses = set()
        clause_list = list(clauses)

        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):

                resolvents = resolve(clause_list[i], clause_list[j])

                for resolvent in resolvents:

                    if len(resolvent) == 0:
                        print("Step", step, ": Empty clause derived (□)")
                        print("Final Result: PROVED")
                        return True

                    if resolvent not in clauses:
                        new_clauses.add(resolvent)
                        print("Step", step, ":", resolvent)
                        step += 1

        if not new_clauses:
            print("Final Result: NOT PROVED")
            return False

        clauses.update(new_clauses)



print("\n===================================")
print("TEST CASE 1: Direct Fact")
print("KB: {P}")
print("Query: P")

resolution_prove(
    [{"P"}],
    "P"
)


print("\n===================================")
print("TEST CASE 2: One Implication")
print("KB: {P -> Q, P}")
print("Query: Q")

resolution_prove(
    [{"~P", "Q"}, {"P"}],
    "Q"
)


print("\n===================================")
print("TEST CASE 3: Chain of Implications")
print("KB: {P -> Q, Q -> R, P}")
print("Query: R")

resolution_prove(
    [{"~P", "Q"}, {"~Q", "R"}, {"P"}],
    "R"
)


print("\n===================================")
print("TEST CASE 4: Disjunctive Knowledge")
print("KB: {P OR Q, ~P}")
print("Query: Q")

resolution_prove(
    [{"P", "Q"}, {"~P"}],
    "Q"
)


print("\n===================================")
print("TEST CASE 5: Query Not Entailed")
print("KB: {P -> Q}")
print("Query: P")

resolution_prove(
    [{"~P", "Q"}],
    "P"
)

print("\n===================================")
print("ALL TEST CASES COMPLETED")
