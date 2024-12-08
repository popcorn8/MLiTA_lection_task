
class Parser:
    def __init__(self, input_string):
        self.L_brackets = {'(', '[', '{'}
        self.L_operations = {'+', '-', '*', '/'}
        self.L_variables = set('abcdefghijklmnopqrstuvwxyz')
        self.string = input_string
        self.ch = None
        self.iterator = -1
        self.read()

    def read(self):
        self.iterator += 1
        if self.iterator >= len(self.string):
            self.ch = None
        else:
            self.ch = self.string[self.iterator]

    def run(self) -> bool:
        try:
            self.correct_exception()
            if self.iterator == len(self.string) and self.ch is None:
                return True
            else:
                return self.error()
        except ValueError as e:
            print(e)
            return False

    def correct_exception(self):
        if self.ch in self.L_brackets:
            self.bracket_writing()
        elif self.ch in self.L_variables:
            self.variable()
        else:
            self.error()

    def unscripted_writing(self):
        self.variable()
        self.operation()
        self.variable()

    def bracket_writing(self):
        if self.ch == '{':
            self.read()
            self.curly_brackets()
            if self.ch == '}':
                self.read()
            else:
                self.error()
        elif self.ch == '[':
            self.read()
            self.square_brackets()
            if self.ch == ']':
                self.read()
            else:
                self.error()
        elif self.ch == '(':
            self.read()
            self.square_brackets()
            if self.ch == ')':
                self.read()
            else:
                self.error()
        else:
            self.error()

    def curly_brackets(self):
        if self.ch in self.L_variables:
            self.variable()
            self.operation()
            self.tail_fs1()
        elif self.ch == '[':
            self.read()
            self.square_brackets()
            if self.ch == ']':
                self.read()
            else:
                self.error()
            self.tail_fs()
        else:
            self.error()

    def tail_fs(self):
        if self.ch in self.L_operations:
            self.operation()
            self.tail_fs1()

    def tail_fs1(self):
        if self.ch == '[':
            self.read()
            self.square_brackets()
            if self.ch == ']':
                self.read()
            else:
                self.error()
        elif self.ch in self.L_variables:
            self.variable()
        else:
            self.error()

    def square_brackets(self):
        if self.ch in self.L_variables:
            self.variable()
            self.operation()
            self.tail_kvs1()
        elif self.ch == '(':
            self.read()
            self.round_brackets()
            if self.ch == ')':
                self.read()
            else:
                self.error()
            self.tail_kvs()
        else:
            self.error()

    def tail_kvs(self):
        if self.ch in self.L_operations:
            self.operation()
            self.tail_kvs1()

    def tail_kvs1(self):
        if self.ch == '(':
            self.read()
            self.round_brackets()
            if self.ch == ')':
                self.read()
            else:
                self.error()
        elif self.ch in self.L_variables:
            self.variable()
        else:
            self.error()

    def round_brackets(self):
        if self.ch in self.L_variables:
            self.variable()
            self.operation()
            self.tail_krs1()
        elif self.ch == '{':
            self.read()
            self.curly_brackets()
            if self.ch == '}':
                self.read()
            else:
                self.error()
            self.tail_krs()
        else:
            self.error()

    def tail_krs(self):
        if self.ch in self.L_operations:
            self.operation()
            self.tail_krs1()

    def tail_krs1(self):
        if self.ch == '{':
            self.read()
            self.curly_brackets()
            if self.ch == '}':
                self.read()
            else:
                self.error()
        elif self.ch in self.L_variables:
            self.variable()
        else:
            self.error()

    def operation(self):
        if self.ch in self.L_operations:
            self.read()
        else:
            self.error()

    def variable(self):
        if self.ch in self.L_variables:
            self.read()
        else:
            self.error()

    def error(self):
        raise ValueError("Получена ошибка!")


if __name__ == "__main__":
    print("Добро пожаловать!")
    print("- Введите exit для выхода из программы.")
    print()
    print("Введите правильное скобочное выражение, соответствующее следующему описанию:")
    print("""   Правильная скобочная запись арифметических выражений с тремя видами скобок.
    При вложенности скобок должно соблюдаться правило чередования: фигурные-квадратные-круглые-фигурные-... 
    Каждая бинарная операция вместе с операндами берется в скобки.
    В правильной записи могут присутствовать “лишние” (двойные) скобки,
    но одна буква не может браться в скобки.

        Пример. 	
        Правильная запись: [({[a+b]*[(a-b)/(a+b)]})-({[a-a]*b}/{[(b+c)*(b-c)]})]
        Неправильная запись: [{a-b}/(c)]+([d-b*c]*[b+c])""")
    print()

    while True:
        input_str = input("> ").strip()
        if input_str == "exit":
            break
        parser = Parser(input_str)
        if parser.run():
            print("Подходящее выражение 0u0")
            print()
        else:
            print("Выражение не подходит -_-")
            print()
    print("Программа завершена!")
