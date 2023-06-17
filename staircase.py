def staircase(n):
    for step in range(1, n + 1):
        step_string = ""

        for space in range(n - (step)):
            step_string += " "

        for solid in range(step):
            step_string += "#"

        print(step_string)

staircase(4)