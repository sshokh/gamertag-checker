from colorama import Fore, Style
from threading import Lock


class Logger(object):
    def __init__(self):
        self.color_table = {
            "success": Style.BRIGHT + Fore.GREEN,
            "warn": Style.BRIGHT + Fore.YELLOW,
            "error": Style.BRIGHT + Fore.RED,
            "debug": Style.BRIGHT + Fore.CYAN,
            "input": Style.BRIGHT + Fore.MAGENTA,
        }
        self.lock = Lock()

    def lprint(self, message):
        with self.lock:
            print(message)

    def success(self, message):
        message = f"{self.color_table['success']}SUCCESS{Fore.RESET} ~ {message}{Style.RESET_ALL}"
        self.lprint(message)

    def error(self, message):
        message = (
            f"{self.color_table['error']}ERROR{Fore.RESET} ~ {message}{Style.RESET_ALL}"
        )
        self.lprint(message)

    def warn(self, message):
        message = (
            f"{self.color_table['warn']}WARN{Fore.RESET} ~ {message}{Style.RESET_ALL}"
        )
        self.lprint(message)

    def debug(self, message):
        message = (
            f"{self.color_table['debug']}DEBUG{Fore.RESET} ~ {message}{Style.RESET_ALL}"
        )
        self.lprint(message)

    def input(self, message):
        answer = input(
            f"{self.color_table['input']}INPUT{Fore.RESET} ~ {message}{Style.RESET_ALL}"
        )
        return answer


logger = Logger()
