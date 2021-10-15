# write your code here
class CodeAnalyzer:


    def long_code_check(self, line_code, line_count):
        """ This function check if the code line
            is longer than 79 character"""

        error_code = 'S001'
        message = error_code + ' Too long'

        try:
            line_code = line_code.rstrip()
            assert len(line_code) <= 79, f'Line {line_count}: ' + message
        except AssertionError as err:
            print(err)

    def indentation_check(self, line_code, line_count):
        """ This function check if the indentation
                is a multiple of four"""
        error_code = 'S002'
        message = error_code + ' Indentation is not a multiple of four'
        count_indent = 0
        line_code = list(line_code)
        for character in line_code:
            if character == ' ':
                count_indent += 1
            if character != ' ':
                break
        try:
            assert count_indent % 4 == 0, f'Line {line_count}: ' + message
        except AssertionError as err:
            print(err)

    def semicolon_check(self, line_code, line_count):
        """ This function check if there is an unnecessary semicolon
                after a statement (but are acceptable in comments)"""
        error_code = 'S003'
        message = error_code + ' Unnecessary semicolon'
        semicolon = False
        if len(line_code) > 0:
            if line_code[-1] == ';':
                semicolon = True
        try:
            assert semicolon == False, f'Line {line_count}: ' + message
        except AssertionError as err:
            print(err)

    def spaces_check(self, line_code, line_count):
        """ This function check if in the line code there are
            Less than two spaces before inline comments"""
        error_code = 'S004'
        message = error_code + 'At least two spaces required before inline comments'
        count_space = 0
        comments = False
        for character in line_code:
            if character == ' ':
                count_space += 1
            if character != ' ' and character != '#':
                count_space = 0
            if character == '#':
                comments = True
                break
        if comments == True and count_space <= 1:
            print(f'Line {line_count}: ' + message)


def main():

    count_line = 1
    checker = CodeAnalyzer()
    file = open(input(), 'r')
    for line in file:
        line = line.rstrip()
        checker.long_code_check(line, count_line)
        checker.indentation_check(line, count_line)
        checker.semicolon_check(line, count_line)
        checker.spaces_check(line, count_line)
        count_line += 1

if __name__ == "__main__":

    main()

