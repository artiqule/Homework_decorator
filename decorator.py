from datetime import datetime


def decor_logger(old_func):
    def foo(*args, **qwargs):
        res = old_func(*args, **qwargs)
        with open('log_file.txt', 'w', encoding='utf-8') as file:
            file.write(
                f'Дата и время вызова: {datetime.now()}\n'
                f'Имя функции: {old_func.__name__}\n'
                f'Aргументы: {args, qwargs}\n'
                f'Возвращаемое значение: {res}'
        )
        return res
    return foo
