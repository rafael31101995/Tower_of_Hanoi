"""
    Hanoi tower
    Basic case: When steps reach 1
    Total steps : (2**discos)-1

    Basic step: A ['1'] ----> C['1']
    Print: 1 para C
"""


def hanoi_logic(A, B, C, steps):
    print(A, B, C, steps)
    if steps < 1:
        return 1
    else:
        if steps % 2 == 0:
            hanoi_logic(A, B, C, steps - 1)
        else:
            hanoi_logic(A, B, C, steps - 1)
        # Montar o diagrama e ver se consegue tirar algo dele. x'


def setting_steps_quantity(discos):
    total_steps = (2 ** discos) - 1
    A = [3, 2, 1]
    B = []
    C = []
    hanoi_logic(A, B, C, total_steps)


if __name__ == '__main__':
    setting_steps_quantity(3)
