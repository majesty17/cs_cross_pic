# -*- coding: utf-8 -*-
import logging
import random
import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

import numpy as np


class game:
    m = 10  # row
    n = 10  # colomn
    label_m = []  # 左侧标签
    label_n = []  # 右侧标签
    map = []
    started = False

    def new_game(self, m, n):
        logging.info("new random game (%d,%d)" % (m, n))
        random.seed(time.time())
        self.m = m
        self.n = n
        # 生成map
        self.map = np.random.randint(low=0, high=2, size=(m, n))
        # 生成label
        for i in range(m):
            self.label_m.append(self.get_label(self.map[i]))
        for j in range(n):
            self.label_n.append(self.get_label(self.map[..., j]))
        self.started = True

    def input_game(self, m, n, label_m, label_n):
        logging.info()
        self.map = np.array(size=(m, n))
        self.label_m = label_m
        self.label_n = label_n

    def print_game(self):
        logging.info("print game.")
        if not self.started:
            print "game not started!"
            return
        # map
        print "-----> map"
        print self.map
        # label
        print "-----> label_m"
        for i in self.label_m:
            print i
        print "-----> label_n"
        for j in self.label_n:
            print j

    def show_game(self):
        logging.info("show game!")
        if not self.started:
            print "game not started!"
            return
        max_len_m = 0
        for i in self.label_m:
            if len(i) > max_len_m:
                max_len_m = len(i)
        max_len_n = 0
        for i in self.label_n:
            if len(i) > max_len_n:
                max_len_n = len(i)
        # print max_len_m, max_len_n
        for i in range(max_len_n):
            print " " * (max_len_m + 1), "|",
            for j in range(self.n):
                if len(self.label_n[j]) > i:
                    print self.label_n[j][i],
                else:
                    print " ",
            print ""

        print "-" * (max_len_m + 1), "|", "--" * self.n
        for i in range(self.m):
            row = self.map[i]
            row = ['▇' if j == 1 else '　' for j in row]
            print self.label_m[i], " " * (max_len_m - len(self.label_m[i])), "|", "".join(row)

    @staticmethod
    def get_label(line):
        a = [str(x) for x in line]
        string = "".join(a)
        spi = string.split('0')
        spi = filter(lambda x: x, spi)
        # print string
        ret = [str(len(x)) for x in spi]
        ret = ",".join(ret)
        # print ret
        return ret


if __name__ == "__main__":
    game = game()
    game.new_game(10, 6)
    # game.print_game()
    #    print game.map[0]
    # print game.get_label([1, 1, 0, 1, 0, 1])
    game.show_game()
