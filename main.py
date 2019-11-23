from pulp import LpProblem, lpSum, LpMinimize, LpVariable, LpInteger, LpStatus, value


def main(p1, p2, printResult=True):

    prob = LpProblem("Line Equation from 2 points", LpMinimize)

    coef = LpVariable("coef",
                      None,
                      None,
                      )

    z = LpVariable("z",
                   None,
                   None,
                   )

    prob += 0, "arbitrary objective"

    prob += (coef * p1[0]) + z == p1[1]
    prob += (coef * p2[0]) + z == p2[1]

    prob.solve()

    if printResult:
        print("Status:", LpStatus[prob.status])

        if LpStatus[prob.status] == "Optimal":
            for v in prob.variables():
                print(v.name, "=", v.varValue)
            print("OBJECTIVE = ", value(prob.objective))

    return coef.value(), z.value()


if __name__ == "__main__":
    p1 = (1, 1)
    p2 = (2, 7)
    coef, z = main(p1, p2)
    print("With points ", p1, "and ", p2,
          " , the line equation is ", coef, "x + ", z)
