"""
    Hanoi tower
    Basic case: When steps reach 1
    Total steps : (2**discos)-1

    Basic step: A ['1'] ----> C['1']
    Print: 1 para C
"""


def hanoi_logic(disc, fr, to, spare):
    if disc == 1:
        print(fr, to)
    else:
        hanoi_logic(disc - 1, fr, spare, to)
        hanoi_logic(1, fr, to, spare)
        hanoi_logic(disc - 1, spare, to, fr)
    # Montar o diagrama e ver se consegue tirar algo dele. x'


def setting_steps_quantity(disc):
    total_steps = (2 ** disc) - 1
    hanoi_logic(disc, 'A', 'C', 'B')


if __name__ == '__main__':
    setting_steps_quantity(3)
