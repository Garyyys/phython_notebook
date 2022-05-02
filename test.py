class ExceptionPrintData(Exception):
    """Класс исключение при отправке данных принтеру"""

    def __int__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка: {self.message}'


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'печать: {str(data)}')

    def send_data(self, data):
        if not self.send_data_to_print(data):
            raise ExceptionPrintData('Принтер не отвечает')

    def send_data_to_print(self, data):
        return False

p = PrintData()
p.print('123')
# try:
#     p.print('123')
# except Exception:
#     print('Принтер не отвечает')
