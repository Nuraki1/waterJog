def water_jug_problem(x, y, z):
    # Initial states of the jugs
    jug1 = 0
    jug2 = 0

    # Lists to store the solution steps
    solution_steps = []
    visited_states = set()

    def pour_jug1_to_jug2():
        nonlocal jug1, jug2
        if jug1 > 0 and jug2 < y:
            amount_poured = min(jug1, y - jug2)
            jug1 -= amount_poured
            jug2 += amount_poured
            return True
        return False

    def pour_jug2_to_jug1():
        nonlocal jug1, jug2
        if jug2 > 0 and jug1 < x:
            amount_poured = min(jug2, x - jug1)
            jug2 -= amount_poured
            jug1 += amount_poured
            return True
        return False

    def empty_jug1():
        nonlocal jug1
        if jug1 > 0:
            jug1 = 0
            return True
        return False

    def empty_jug2():
        nonlocal jug2
        if jug2 > 0:
            jug2 = 0
            return True
        return False

    def fill_jug1():
        nonlocal jug1
        if jug1 < x:
            jug1 = x
            return True
        return False

    def fill_jug2():
        nonlocal jug2
        if jug2 < y:
            jug2 = y
            return True
        return False

    def is_goal_state():
        return jug1 == z or jug2 == z

    def is_valid_state():
        return (jug1, jug2) not in visited_states

    def record_state():
        visited_states.add((jug1, jug2))

    def print_solution():
        print("Solution Steps:")
        for step in solution_steps:
            print(step)

    def solve():
        while not is_goal_state():
            if is_valid_state():
                record_state()
                if pour_jug1_to_jug2():
                    solution_steps.append(f"Pour water from jug 1 to jug 2: {jug1}L, {jug2}L")
                elif pour_jug2_to_jug1():
                    solution_steps.append(f"Pour water from jug 2 to jug 1: {jug1}L, {jug2}L")
                elif empty_jug1():
                    solution_steps.append(f"Empty jug 1: {jug1}L, {jug2}L")
                elif empty_jug2():
                    solution_steps.append(f"Empty jug 2: {jug1}L, {jug2}L")
                elif fill_jug1():
                    solution_steps.append(f"Fill jug 1: {jug1}L, {jug2}L")
                elif fill_jug2():
                    solution_steps.append(f"Fill jug 2: {jug1}L, {jug2}L")
            else:
                return False

        print_solution()
        return True


# Taking user input for jug capacities and desired liters
x = int(input("Enter the capacity of jug 1 (in liters): "))
y = int(input("Enter the capacity of jug 2 (in liters): "))
z = int(input("Enter the desired liters (to be measured): "))

# Solving the water jug problem
if water_jug_problem(x, y, z):
    print("Goal state reached!")
else:
    print("No solution found!")