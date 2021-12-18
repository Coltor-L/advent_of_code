import pytest
import day1


def clean_test_inputs(inputs: list[str]) -> list[int]:
    return [int(x.rstrip("\n")) for x in inputs]


def test_get_increasing_inputs_count():
    with open("inputs1.txt") as f:
        cleaned_inputs = clean_test_inputs(f.readlines())
        assert day1.get_increasing_inputs_count(cleaned_inputs) == 7

    with open("inputs2.txt") as f:
        cleaned_inputs = clean_test_inputs(f.readlines())
        assert day1.get_increasing_inputs_count(cleaned_inputs) == 1548


def test_get_increasing_sums_count():
    with open("inputs1.txt") as f:
        cleaned_inputs = clean_test_inputs(f.readlines())
        assert day1.get_increasing_sums_count(cleaned_inputs, 3) == 5

    with open("inputs2.txt") as f:
        cleaned_inputs = clean_test_inputs(f.readlines())
        ret = day1.get_increasing_sums_count(cleaned_inputs, 3)

        assert ret > 0



