#운영체제 레지스터 명령어	
# bitmask, case_work, parsing, implementation	
# Silver III



def boost_bin2hex(binary_string):
    decimal = 0
    for index, binary in enumerate(binary_string[::-1]):
        decimal += (2 ** index) * int(binary)

    return boost_dec2hex(decimal)


def boost_dec2hex(decimal):
    decimal = int(decimal)

    hexs = {
        0:"0", 1:"1", 2:"2", 3:"3", 4:"4",
        5:"5", 6:"6", 7:"7", 8:"8", 9:"9",
        10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"
    }

    hexademicals = []
    while decimal > 15:
        hexademicals.append(hexs[decimal % 16])
        decimal = decimal // 16

    hexademicals.append(hexs[decimal])
    return "".join(hexademicals[::-1])


def validate_instruction(instruction, registers):
    # command should starts with "L"
    if instruction[0] != "L":
        return False

    # only "LD", "LN" command available.
    if instruction[1] != "D" and instruction[1] != "N":
        return False

    # command and parameter should be divided with whitespace.
    if instruction[2] != " ":
        return False

    # only 'A', 'B', 'C', 'D', 'E', 'H', 'L' registers available.
    if instruction[3] not in registers:
        return False

    # parameter should be divided with comma.
    if instruction[4] != ",":
        return False

def convert_to_hex(command, param1, param2, commands, registers):
    strings = []
    strings.append(commands[command]) # 00, 01
    strings.append(registers[param1]) # 111, 110, ...

    if command == "LD":
        strings.append(registers[param2]) # 111, 110, ...
        return boost_bin2hex("".join(strings))
    elif command == "LN":
        strings.append("110") # 110
        return f'{boost_bin2hex("".join(strings))} {boost_dec2hex(param2)}'


def solution(param0):
    # LD dst, src: load src register value to destination register.
    # load to destination from source.
    # 2bit(01) + 3bit(register) + 3bit(register) = 1byte

    # LD dst, value: load value to destination register.
    # load to destination as value.
    # 2bit(00) + 3bit(register) + 3bit(padding) + 1byte(value) = 2byte

    commands = {
        "LD": "01",
        "LN": "00"
    }

    registers = {
        "A":"111",
        "B":"000",
        "C":"001",
        "D":"010",
        "E":"011",
        "H":"100",
        "L":"101"
    }

    index = 0
    if validate_instruction(param0, registers) == False:
        return "ERROR"

    command = param0[:2]
    destination = param0[3]
    source = param0[5:]

    if source == destination:
        return "NOOP"

    output = convert_to_hex(command, destination, source, commands, registers).replace(" ", "").upper()
    return f'0x{output}'


# 부스트캠프 코딩테스트 후기를 보면 특정 내장 메서드를 사용하지 않고 직접 구현하라는 문제가 나온다고 하던데 
# 그게 이런 문제였던 것 같다. 진법 변환은 까다로우면서도 원리만 알면 어렵지 않게 구현할 수 있는 것 같다.

# 다른 요구사항으로 메서드를 호출할 때 메인 함수 외부에 따로 구현해서 사용하라는 것이 있었다. 
# 문제는 기본적으로 문자열 파싱이었기 때문에 위의 코드처럼 검증 메서드를 별도로 분리해서 작성하였다.