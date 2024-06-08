import pulp


# Maximize beverage production
def drinks_production():
    model = pulp.LpProblem("Drinks_production", pulp.LpMaximize)

    # Definition of variables
    A = pulp.LpVariable("A", lowBound=0, cat="Integer")  # Amount of Lemonade
    B = pulp.LpVariable("B", lowBound=0, cat="Integer")  # Amount of fruit juice

    # Maximize profits
    model += A + B, "Profit"

    model += 2 * A + 1 * B <= 100  # Water limitations
    model += 1 * A <= 50  # Limitations for sugar
    model += 1 * A <= 30  # Limitations for lemon juice
    model += 2 * B <= 40  # Limitations for fruit puree

    model.solve()

    print("Status:", pulp.LpStatus[model.status])
    print("Lemonade:", A.varValue)
    print("Fruit juice:", B.varValue)
    print("Total volume:", pulp.value(model.objective))


if __name__ == "__main__":
    drinks_production()
