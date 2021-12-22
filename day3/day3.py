def get_inputs_as_matrix(binary_inputs: list[str]) -> list[list[int]]:
    return [[int(x) for x in split.rstrip("\n")] for split in binary_inputs]


def get_gamma_rate(binary_numbers: list[list[int]]) -> int:
    if len(binary_numbers) == 0:
        return 0

    ret_repr = []

    for j in range(0, len(binary_numbers[0])):
        one_count = 0
        zero_count = 0
        for i in range(0, len(binary_numbers)):
            if binary_numbers[i][j] == 0:
                zero_count += 1
            else:
                one_count += 1

        if one_count > zero_count:
            ret_repr.append(1)
        else:
            ret_repr.append(0)

    ret = 0
    power = 0

    for i in range(0, len(ret_repr)):
        ret += (2 ** power) * ret_repr[len(ret_repr) - 1 - i]
        power += 1

    return ret

def get_epsilon_rate(binary_numbers: list[list[int]]) -> int:
    if len(binary_numbers) == 0:
        return 0

    ret_repr = []

    for j in range(0, len(binary_numbers[0])):
        one_count = 0
        zero_count = 0
        for i in range(0, len(binary_numbers)):
            if binary_numbers[i][j] == 0:
                zero_count += 1
            else:
                one_count += 1

        if one_count > zero_count:
            ret_repr.append(0)
        else:
            ret_repr.append(1)

    ret = 0
    power = 0

    for i in range(0, len(ret_repr)):
        ret += (2 ** power) * ret_repr[len(ret_repr) - 1 - i]
        power += 1

    return ret

def get_oxygen_rate(binary_numbers: list[list[int]]) -> int:
    if len(binary_numbers) == 0:
        return 0

    rows_filtered_out = []

    for j in range(0, len(binary_numbers[0])):
        rows_with_one = []
        rows_with_zero = []
        for i in range(0, len(binary_numbers)):
            if i in rows_filtered_out:
                continue

            if binary_numbers[i][j] == 0:
                rows_with_zero.append(i)
            else:
                rows_with_one.append(i)

        if len(rows_with_zero) <= len(rows_with_one):
            rows_filtered_out.extend(rows_with_zero)
        else:
            rows_filtered_out.extend(rows_with_one)

        if len(rows_filtered_out) == len(binary_numbers) - 1:
            break


    # technically there should only be 1 left
    remaining_rows = [i for i in range(0, len(binary_numbers)) if i not in rows_filtered_out]
    if len(remaining_rows) != 1:
        raise Exception("There should only be 1 row remaining after oxygen rate filtering")

    ret = 0
    power = 0

    for i in range(0, len(binary_numbers[remaining_rows[0]])):
        ret += (2 ** power) * binary_numbers[remaining_rows[0]][len(binary_numbers[remaining_rows[0]]) - 1 - i]
        power += 1

    return ret

def get_co2_rate(binary_numbers: list[list[int]]) -> int:
    if len(binary_numbers) == 0:
        return 0

    rows_filtered_out = []

    for j in range(0, len(binary_numbers[0])):
        rows_with_one = []
        rows_with_zero = []
        for i in range(0, len(binary_numbers)):
            if i in rows_filtered_out:
                continue

            if binary_numbers[i][j] == 0:
                rows_with_zero.append(i)
            else:
                rows_with_one.append(i)

        if len(rows_with_zero) <= len(rows_with_one):
            rows_filtered_out.extend(rows_with_one)
        else:
            rows_filtered_out.extend(rows_with_zero)

        if len(rows_filtered_out) == len(binary_numbers) - 1:
            break

    # technically there should only be 1 left
    remaining_rows = [i for i in range(0, len(binary_numbers)) if i not in rows_filtered_out]
    if len(remaining_rows) != 1:
        raise Exception("There should only be 1 row remaining after oxygen rate filtering")

    ret = 0
    power = 0

    for i in range(0, len(binary_numbers[remaining_rows[0]])):
        ret += (2 ** power) * binary_numbers[remaining_rows[0]][len(binary_numbers[remaining_rows[0]]) - 1 - i]
        power += 1

    return ret

