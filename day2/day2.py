from typing import Tuple
from enum import Enum
import re


class MoveAction(Enum):
    FORWARD = 1
    UP = 2
    DOWN = 3


def get_move_distance_pairs(inputs: list[str]) -> list[Tuple[MoveAction, int]]:
    ret = []
    regex = re.compile("^([fud].*) ([0-9]+)")

    for el in inputs:
        match = regex.match(el)

        if match:
            move_action = MoveAction[match.group(1).upper()]
            distance = int(match.group(2))
            ret.append((move_action, distance))

    return ret


def get_total_moved(moves: list[Tuple[MoveAction, int]]) -> Tuple[int, int]:
    ret_hor = 0
    ret_vert = 0

    for action, distance in moves:
        if action == MoveAction.UP:
            ret_vert -= distance
        elif action == MoveAction.DOWN:
            ret_vert += distance
        elif action == MoveAction.FORWARD:
            ret_hor += distance
        else:
            raise Exception("A MoveAction can only be UP, DOWN, or FORWARD")

    return ret_hor, ret_vert


def get_total_moved_with_aim(moves: list[Tuple[MoveAction, int]]) -> Tuple[int, int]:
    ret_hor = 0
    ret_vert = 0
    aim = 0

    for action, distance in moves:
        if action == MoveAction.UP:
            aim -= distance
        elif action == MoveAction.DOWN:
            aim += distance
        elif action == MoveAction.FORWARD:
            ret_hor += distance
            ret_vert += aim*distance

    return ret_hor, ret_vert
