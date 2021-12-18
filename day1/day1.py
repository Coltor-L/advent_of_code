
def get_increasing_inputs_count(inputs : list[int]) -> int:
    if len(inputs) == 0:
        return 0

    ret = 0
    previous = inputs[0]

    for i in range(1, len(inputs)):
        if inputs[i] > previous:
            ret += 1
        previous = inputs[i]

    return ret


def get_increasing_sums_count(inputs : list[int], sliding_sum_len : int) -> int:
    if len(inputs) < sliding_sum_len:
        return 0

    ret = 0
    previous_sum = sum([x for x in inputs[0:sliding_sum_len]])

    for i in range(sliding_sum_len, len(inputs)):
        current_sum = sum([x for x in inputs[i: i + sliding_sum_len]])

        if current_sum > previous_sum:
            ret += 1

        previous_sum = current_sum

    return ret


