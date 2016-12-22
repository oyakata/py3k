# -*- coding:utf-8 -*-


def main():
    '''整数で入力を求めるプロンプトを出す。

    但し、evalするので整数リテラルを入力すればok。

    整数「で」入力してください> 10
    ok> 10: <type 'int'>

    整数「で」入力してください> '10'
    ng> 10: <type 'str'>

    整数「で」入力してください> int('10')
    ok> 10: <type 'int'>

    整数「で」入力してください> foo
    Traceback (most recent call last):
      File "chap4.py", line 27, in <module>
        main()
      File "chap4.py", line 18, in main
        i = eval(raw_input('整数「で」入力してください> '))
      File "<string>", line 1, in <module>
    NameError: name 'foo' is not defined
    '''
    i = eval(raw_input('整数「で」入力してください> '))
    
    if isinstance(i, int):
        print('ok> {}: {}'.format(i, type(i)))
    else:
        print('ng> {}: {}'.format(i, type(i)))


if __name__ == '__main__':
    main()
