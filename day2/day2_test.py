import pytest

import day2


def test_get_move_distance_pairs():
    test_input = ["forward 23", "down 12", "up 777"]
    test_output = day2.get_move_distance_pairs(test_input)

    out_m, out_d = test_output[0]
    assert out_m == day2.MoveAction.FORWARD and out_d == 23

    out_m, out_d = test_output[1]
    assert out_m == day2.MoveAction.DOWN and out_d == 12

    out_m, out_d = test_output[2]
    assert out_m == day2.MoveAction.UP and out_d == 777


def test_get_total_moved():
    with open("inputs1.txt") as f:
        moves = day2.get_move_distance_pairs(f.readlines())
        hor, vert = day2.get_total_moved(moves)
        assert hor * vert == 150

    with open("inputs2.txt") as f:
        moves = day2.get_move_distance_pairs(f.readlines())
        hor, vert = day2.get_total_moved(moves)
        assert hor * vert == 1427868


def test_get_total_moved_with_aim():
    with open("inputs1.txt") as f:
        moves = day2.get_move_distance_pairs(f.readlines())
        hor, vert = day2.get_total_moved_with_aim(moves)
        assert hor * vert == 900

    with open("inputs2.txt") as f:
        moves = day2.get_move_distance_pairs(f.readlines())
        hor, vert = day2.get_total_moved_with_aim(moves)
        assert hor * vert == 1568138742
