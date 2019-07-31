total = 8


def take_one_step(total, step_list):
    for i in range(total, 0, -1):
        step_list.append('1')

    return step_list


for i in range(0, int(total/2)+1):
    step_list = []
    remaining_steps = total

    for i in range(0, i):
        remaining_steps = remaining_steps - 2
        step_list.append('2')

    print(take_one_step(remaining_steps, step_list))
