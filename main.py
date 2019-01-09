import numpy as np
import random
import sys
import time


class Eight_queens:
    def __init__(self):
        pass

    def calculate_max_queens_size(self, height, width, queen_size,
                                  start_queen_size=1, max_step=100, exec_all=False, power=None):

        max_queen_size = 0

        for current_queen_size in range(start_queen_size, queen_size + 1):
            for step in range(max_step):
                queen_positions = self.generate_queen_positions(
                    height, width, current_queen_size)

                if self.is_valid_board(height, width, current_queen_size, queen_positions, power=power):
                    max_queen_size = len(queen_positions)
                    print(queen_positions)
                    break

            if step == (max_step - 1) and exec_all == False:
                return max_queen_size

        return max_queen_size

    def generate_queen_positions(self, height, width, queen_size):
        positions = set()

        for _ in range(queen_size):
            x = random.randint(0, width)
            y = random.randint(0, height)
            positions.add((x, y))

        return positions

    def is_valid_board(self, height, width, queen_size,
                       queen_positions, power):
        '''
            power default is min(height, width)
        '''

        if len(queen_positions) != queen_size:
            return False

        if power is None:
            power = min([height, width])

        invalid_positions = set(
            self.get_influence_positions(queen_positions, power))

        x = 0
        y = 1
        for queen_pos in queen_positions:
            if (queen_pos[x], queen_pos[y]) in invalid_positions:
                return False

        return True

    def get_influence_positions(self, positions, power):
        influence_positions = set()

        for i in positions:
            point = i
            for p in self.get_queen_influence_positions(point, power):
                influence_positions.add(p)

        return influence_positions

    def get_queen_influence_positions(self, point, power):
        x = 0
        y = 1

        influence_positions = []

        for p in range(1, power + 1):
            influence_left = (point[x] - p, point[y])
            influence_right = (point[x] - p, point[y])
            influence_top = (point[x], point[y] + p)
            influence_bottom = (point[x], point[y] - p)
            influence_skew_left_up = (point[x] - p, point[y] + p)
            influence_skew_left_down = (point[x] + p, point[y] - p)
            influence_skew_right_up = (point[x] + p, point[y] + p)
            influence_skew_right_down = (point[x] - p, point[y] - p)

            influence_positions.append(influence_left)
            influence_positions.append(influence_right)
            influence_positions.append(influence_top)
            influence_positions.append(influence_bottom)
            influence_positions.append(influence_skew_left_up)
            influence_positions.append(influence_skew_left_down)
            influence_positions.append(influence_skew_right_up)
            influence_positions.append(influence_skew_right_down)

        return influence_positions


if __name__ == '__main__':
    print('starting')
    eq = Eight_queens()
    start_time = time.time()

    print(eq.calculate_max_queens_size(6, 6, 7, max_step=10000,
                                       power=None, exec_all=True))
    elapsed_time = time.time() - start_time
    print(elapsed_time)