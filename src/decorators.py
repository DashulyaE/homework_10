from datetime import datetime


def log(filename=None):
    def my_decorator(func):
        """Декоратор, который логирует время выполнения функции, ее результаты и возникшие ошибки"""

        def wrapper(*args, **kwargs):
            time_start = datetime.now()
            try:
                result = func(*args, **kwargs)
                message_in_log = f"{func.__name__} ok"
            except Exception as e:
                message_in_log = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}"
            finally:
                time_end = datetime.now()
                message_in_log += f" Lead time: {time_end - time_start}"
                if filename:
                    with open("log.txt", "a") as file:
                        file.write(message_in_log + "\n")
                else:
                    print(message_in_log)
            return result

        return wrapper

    return my_decorator
