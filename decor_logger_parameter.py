import os
import datetime


def decor_logger_parameter(path):
    def decor_logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(path, 'a') as log_f:
                log_f.write(f"Name_function: {old_function.__name__}\n")
                log_f.write(f"Currente date and time: {datetime.datetime.now().strftime('%d/%m/%Y %H/:%M:%S')}\n")
                log_f.write(f"Arguments: {args} and {kwargs}\n")
                log_f.write(f"Result: {result}\n")

                return result

        return new_function

        return new_function

    return decor_logger()


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @decor_logger_parameter(path)
        def hello_world():
            return 'Hello World'

        @decor_logger_parameter(path)
        def summator(a, b=0):
            return a + b

        @decor_logger_parameter(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()
