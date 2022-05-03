from copy import deepcopy

# 좌측 우선 연산.
def solution(expression):
    # parse expression
    exp_list = []
    int_buffer = ""
    for char in expression:
        if char in "1234567890":
            int_buffer += char
        else:
            exp_list.append(int_buffer)
            int_buffer = ""
            exp_list.append(char)
    exp_list.append(int_buffer)

    # calculate expression
    return allcase(exp_list)

def allcase(exp_list):
    # if execution all done return abs
    if len(exp_list) == 1:
        return abs(int(exp_list[0]))
    
    # collect all results
    results = []
    # execute all +
    if "+" in exp_list:
        exp_executed = []
        idx = 0
        while 1:
            if exp_list[idx] == "+":
                exp_executed.append(str(int(exp_executed.pop()) + int(exp_list[idx + 1])))
                idx += 2
            else:
                exp_executed.append(exp_list[idx])
                idx += 1
            if idx == len(exp_list):
                break
        results.append(allcase(exp_executed))
    # execute all -
    if "-" in exp_list:
        exp_executed = []
        idx = 0
        while 1:
            if exp_list[idx] == "-":
                exp_executed.append(str(int(exp_executed.pop()) - int(exp_list[idx + 1])))
                idx += 2
            else:
                exp_executed.append(exp_list[idx])
                idx += 1
            if idx == len(exp_list):
                break
        results.append(allcase(exp_executed))
    # execute all *
    if "*" in exp_list:
        exp_executed = []
        idx = 0
        while 1:
            if exp_list[idx] == "*":
                exp_executed.append(str(int(exp_executed.pop()) * int(exp_list[idx + 1])))
                idx += 2
            else:
                exp_executed.append(exp_list[idx])
                idx += 1
            if idx == len(exp_list):
                break
        results.append(allcase(exp_executed))
    
    # chose max reslut
    return max(results)

print(solution("100-200*300-500+20"))  #60420
print(solution("50*6-3*2"))            #300