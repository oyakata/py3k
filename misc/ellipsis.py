# -*- coding:utf-8 -*-
from contextlib import contextmanager
import time


class Pizza(object):
    def __init__(self, dough, sauce, toppings):
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def __next__(self):
        if self.dough:
            d, self.dough = self.dough, None
            return d

        if self.sauce:
            s, self.sauce = self.sauce, None
            return s

        if self.toppings:
            ts, self.toppings = self.toppings, None
            return ts

    @property
    def ready(self):
        return not any((self.dough, self.sauce, self.toppings))


class PizzaOven(object):
    HOT_ENOUGH = 185

    def __init__(self, temp=0):
        self.temp = temp  # temp(erature)
        self.pizza = None

    def push(self, pizza):
        self.pizza = pizza

    @contextmanager
    def heat(self):
        while not self.ready:
            time.sleep(0.2)
            self.temp += 1
            print("heating...({})".format(self.temp), flush=True, end='=> ')
        print('ready!')
        yield

    def bake(self, ms):
        assert self.pizza and not self.pizza.ready
        p = self.pizza

        with self.heat():
            print('生地は?> {}'.format(next(p)))
            time.sleep(ms)
            print('ソースは?> {}'.format(next(p)))
            time.sleep(ms)
            print('トッピングは?> {}'.format(', '.join(next(p))))
            time.sleep(ms)
        print('\t\t\t<チン!>')

    @property
    def ready(self):
        return self.temp > self.HOT_ENOUGH


def sample():
    ...


def main():
    pizza = Pizza('クリスプ', 'トマトソース', ['チーズ', 'ペパロニ', 'サラミ', 'Green pepper'])
    oven = PizzaOven(180)
    oven.push(pizza)
    oven.bake(0.2)


if __name__ == '__main__':
    main()
