import copy
import random
class Hat:
    def __init__(self, **hats):
        self.contents = list()
        for key, val in hats.items():
            for i in range(val):
                self.contents.append(key)
    def draw(self, num):
        if num >= len(self.contents):
            return self.contents
        else:
            drawn_list = list()
            for draw_time in range(num):
                drawn = random.sample(self.contents, 1)
                drawn_list += drawn
            for item in drawn_list:
                if item in self.contents:
                    self.contents.remove(item)
        return drawn_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    event = 0
    for experiment in range(num_experiments):
        expected_list = list()
        for c, n in expected_balls.items():
            for t_val in range(n):
                expected_list.append(c)
        new_hat = copy.deepcopy(hat)
        sample_list = new_hat.draw(num_balls_drawn)
        for color in sample_list:
            if color in expected_list:
                expected_list.remove(color)
        if len(expected_list) == 0:
            event += 1
        probablility = event / num_experiments
    return probablility