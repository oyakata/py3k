# -*- coding:utf-8 -*-
import time
import unittest


def iterable1(obj):
    return hasattr(obj, '__iter__')


def iterable2(obj):
    import collections
    return isinstance(obj, collections.Iterable)


def iterable3(obj):
    return hasattr(obj, '__next__')


def iterable4(obj):
    return hasattr(obj, 'next')


def check(obj):
    '''iterable, sequenceであるか調べる。

    参考: 単に__iter__を持っているだけではiterableと評価されてもイテレータと評価されない。
          __next__を持っていることが必要。

    >>> hasattr('', '__next__')
    False

    >>> hasattr(iter(''), '__next__')
    True

    >>> hasattr((1 for x in range(0)), '__next__')
    True

    >>> def func():
    ...     while True:
    ...         yield 0
    ...

    >>> hasattr(func, '__next__')
    False

    >>> hasattr(func(), '__next__')
    True
    '''
    return (
        iterable1(obj),
        iterable2(obj),
        iterable3(obj),
        iterable4(obj),
    )


class TestAllIterableChecker(unittest.TestCase):
    def call_FUT(self, obj):
        return check(obj)

    def test(self):

        def fn():
            while True:
                yield 0

        items = (
            # iterableなオブジェクト
            (range(1), True, True, False, False),
            (range(0), True, True, False, False),
            ('', True, True, False, False),
            (tuple(), True, True, False, False),
            (list(), True, True, False, False),
            (dict(), True, True, False, False),
            (set(), True, True, False, False),
            # __next__も持っているオブジェクト
            (iter(''), True, True, True, False),
            ((1 for x in range(0)), True, True, True, False),
            (fn(), True, True, True, False),
            # その他
            (fn, False, False, False, False),
        )

        for item in items:
            obj, expects = item[0], item[1:]
            with self.subTest(obj=obj):
                self.assertEqual(check(obj), expects)


def main():
    E = (
        "\033[2J\033[G\n\n"
        "次のオブジェクトが以下1〜3で評価された場合の真偽をTrue/Falseのカンマ区切りで入力してください。\n\n"
        "例:\n"
        "    obj = 10\n"
        "    x = hasattr(obj, '__iter__')\n"
        "    y = isinstance(obj, collections.Iterable)\n"
        "    z = hasattr(obj, '__next__')\n"
        "    x, y, z ? => False, False, False\n"
    )
    print(E)

    items = (
        "{'a': 10, 'b': 'Hello'}",
        "range(1)",
        "iter('yes')",
    )

    for i, raw in enumerate(items, 1):
        Q = (
            "[Q{:02d}]\n"
            "obj = {}\n"
            "hasattr(obj, '__iter__'), isinstance(obj, collections.Iterable), hasattr(obj, '__next__')\n"
            "これらの真偽は? > "
        )
        xs = input(Q.format(i, raw))

        try:
            inputs = eval(xs)
            if not isinstance(inputs, (list, tuple)):
                inputs = (inputs,)
            inputs = tuple(inputs)
            inputs = tuple(bool(x) for x in inputs)
        except:
            print('\033[2J\033[G\n構文エラー: 終了します')
            break
        else:
            time.sleep(0.3)
            print('\033[2J\033[G')

        result = check(eval(raw))[:-1]
        if inputs == result:
            time.sleep(0.3)
            print('\n*****正解!*****')
            time.sleep(0.3)
        else:
            time.sleep(0.3)
            print('\n*****残念... {} != {}'.format(inputs, result))
            time.sleep(0.3)


if __name__ == '__main__':
    main()
