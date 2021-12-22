import pytest

import day3

def test_gamma_and_epsilon_rate():
    with open("inputs1.txt") as f:
        binary_numbers = day3.get_inputs_as_matrix(f.readlines())
        gamma_rate = day3.get_gamma_rate(binary_numbers)
        epsilon_rate = day3.get_epsilon_rate(binary_numbers)

        assert gamma_rate * epsilon_rate == 198

    with open("inputs2.txt") as f:
        binary_numbers = day3.get_inputs_as_matrix(f.readlines())
        gamma_rate = day3.get_gamma_rate(binary_numbers)
        epsilon_rate = day3.get_epsilon_rate(binary_numbers)

        assert gamma_rate * epsilon_rate == 4139586

def test_oxygen_c02_rate():
    with open("inputs1.txt") as f:
        binary_numbers = day3.get_inputs_as_matrix(f.readlines())
        oxygen_rate = day3.get_oxygen_rate(binary_numbers)
        co2_rate = day3.get_co2_rate(binary_numbers)

        assert oxygen_rate * co2_rate == 230

    with open("inputs2.txt") as f:
        binary_numbers = day3.get_inputs_as_matrix(f.readlines())
        oxygen_rate = day3.get_oxygen_rate(binary_numbers)
        co2_rate = day3.get_co2_rate(binary_numbers)

        assert oxygen_rate * co2_rate == 1800151

