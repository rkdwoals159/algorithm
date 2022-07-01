#스택과 레지스터 이용 계산기	
# stack (STL 사용불가),case_work, implementation	
# Silver III

STACK_SIZE = 8
FAIL_MESSAGE = {
    "empty": "EMPTY",
    "full": "OVERFLOW",
    "not_initialized": "ERROR",
    "not_supported": "UNKNOWN"
}


def validate_command(command, commands):
    return command in commands


def validate_register(registers, register_name):
    return registers[register_name] is not None


def validate_stack_full(stack):
    return len(stack) >= STACK_SIZE


def validate_stack_empty(stack):
    return len(stack) == 0


def stack_pop(stack, registers, register_name):
    if validate_stack_empty(stack):
        return FAIL_MESSAGE["empty"]

    registers[register_name] = stack.pop()


def stack_add(stack, registers, register_param1, register_param2):
    if validate_register(registers, register_param1) == False or validate_register(registers, register_param2) == False:
        return FAIL_MESSAGE["not_initialized"]

    if validate_stack_full(stack):
        return FAIL_MESSAGE["full"]

    stack.append(registers[register_param1] + registers[register_param2])


def stack_sub(stack, registers, register_param1, register_param2):
    if validate_register(registers, register_param1) == False or validate_register(registers, register_param2) == False:
        return FAIL_MESSAGE["not_initialized"]

    if validate_stack_full(stack):
        return FAIL_MESSAGE["full"]

    stack.append(registers[register_param1] - registers[register_param2])


def stack_push(stack, value):
    if validate_stack_full(stack):
        return FAIL_MESSAGE["full"]

    stack.append(value)


def swap_register(registers, register_param1, register_param2):
    registers[register_param1], registers[register_param2] = registers[register_param2], registers[register_param1]


def print_stack(stack):
    if validate_stack_empty(stack):
        return FAIL_MESSAGE["empty"]
    else:
        return str(stack.pop())


def solution(params):
    # POPA: pop from stack and set to register A. if stack is empty, "EMPTY".
    # POPB: pop from stack and set to register B. if stack is empty, "EMPTY".
    # ADD: push to stack value of sum of register A, B. (A+B)
    # SUB: push to stack value of sub of register A, B. (A-B)
    # PUSH0...3: push 0...3 to stack.
    # SWAP: swap register A and B.
    # PRINT: pop and print stack value. if stack is empty, "EMPTY".
    commands = {"POPA", "POPB", "ADD", "SUB", "PUSH0", "PUSH1", "PUSH2", "PUSH3", "SWAP", "PRINT"}
    registers = {"A": None, "B": None}

    stack = []
    output_stream = []
    for param in params:
        if validate_command(param, commands) == False:
            output_stream.append(FAIL_MESSAGE["not_supported"])
            continue

        result = None
        if param.startswith("POP"):
            result = stack_pop(stack, registers, param[3])                
        elif param.startswith("PUSH"):
            result = stack_push(stack, int(param[4]))               
        elif param == "ADD":
            result = stack_add(stack, registers, "A", "B")              
        elif param == "SUB":
            result = stack_sub(stack, registers, "A", "B")               
        elif param == "SWAP":
            result = swap_register(registers, "A", "B")              
        elif param == "PRINT":
            result = print_stack(stack)  

        if result is not None:
            output_stream.append(result)

    return output_stream
#문자열을 받아서 주어진 대로 작업을 수행해야 하는 문제였다. 
# 기능별로 필요한 제약사항과 행동 메서드를 구현하여 사용하는 단순한 문제였다.