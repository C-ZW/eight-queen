import sys
import time
import random
import numpy as np


class Eight_queens:
    def calculate_max_queen_size(self, height, width, power, max_step):
        max_size = 0
        queen_pos = None
        board = self.init_board(height, width)

        for _ in range(max_step):
            queen_positions = self.generate_queen_positions(board, power)

            if len(queen_positions) > max_size:
                max_size = len(queen_positions)
                queen_pos = queen_positions

            if len(queen_pos) == height * width:
                break

        return queen_pos

    def init_board(self, height, width):
        board = []

        for x in range(width):
            for y in range(height):
                board.append((x, y))

        return set(board)

    def generate_queen_positions(self, board, power):
        positions = set()

        while len(board) != 0:
            choiced = random.sample(board, 1)
            queen_position = choiced[0]  # random.sample return array

            influence_positions = self.get_queen_influence_positions(
                queen_position, power)
            board = board.difference(influence_positions)
            positions.add(queen_position)

        return positions

    def get_queen_influence_positions(self, point, power):
        x = 0
        y = 1

        influence_positions = []
        for i in range(-power, power + 1):
            row = (point[x] + i, point[y])
            column = (point[x], point[y] + i)
            right_skew = (point[x] - i, point[y] + i)
            left_skew = (point[x] + i, point[y] + i)

            influence_positions.append(row)
            influence_positions.append(column)
            influence_positions.append(right_skew)
            influence_positions.append(left_skew)

        return influence_positions


if __name__ == '__main__':
    BOARD_HEIGHT = 8
    BOARD_WIDTH = 8
    POWER = 7
    MAX_STEP = 100

    print('Board size: ' + str(BOARD_HEIGHT) + ' * ' + str(BOARD_WIDTH))
    print('Power: ' + str(POWER))
    print('Max step: ' + str(MAX_STEP))

    eq = Eight_queens()
    start_time = time.time()

    queen_pos = eq.calculate_max_queen_size(
        BOARD_HEIGHT, BOARD_WIDTH, POWER, MAX_STEP)

    elapsed_time = time.time() - start_time

    print()
    print('Execute time: ' + str(elapsed_time))
    print('Result max size: ' + str(len(queen_pos)))
    print(sorted(list(queen_pos)))
