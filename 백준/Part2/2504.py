def is_OK(Bracket_list):
  stack = []
  for Bracket in Bracket_list:
    if Bracket in ['(', '[']:
      stack.append(Bracket)
    elif Bracket == ')':
      if 0 < len(stack):
        if stack[-1] == '(':
          stack.pop()
        else:
          return False
      else:
        return False
    elif Bracket == ']':
      if 0 < len(stack):
        if stack[-1] == '[':
          stack.pop()
        else:
          return False
      else:
        return False
  if len(stack) == 0:
    return True
  else:
    return False

def calc(Bracket_list):
  stack = []
  for Bracket in Bracket_list:
    if Bracket in ['(', '[']:
      stack.append(Bracket)
    elif Bracket == ')':
      # (
      if stack[-1] == '(':
        stack.pop()
        stack.append(2)
      # ( num 
      else:
        tmp = stack.pop() * 2
        stack.pop()
        stack.append(tmp)
    elif Bracket == ']':
      # [
      if stack[-1] == '[':
        stack.pop()
        stack.append(3)
      # [ num
      else:
        tmp = stack.pop() * 3
        stack.pop()
        stack.append(tmp)
    # add two adj number
    if 1 < len(stack):
      if type(stack[-1]) == int and type(stack[-2]) == int:
        tmp = stack.pop() + stack.pop()
        stack.append(tmp)
  return stack[0]

# 첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 
# 단 그 길이는 1 이상, 30 이하이다.
Bracket_list = [Bracket for Bracket in input().strip()]
if is_OK(Bracket_list):
  print(calc(Bracket_list))
else:
  print(0)