#str[start:stop:step]
trial="reversal"
new_trial= trial[::-1]
print(new_trial)

def str_reverse(str):
    if len(str) == 0:
      return str
    str_reverse(str[1:])+str[0]  #traverse from the front skipping the first char then append the first char 
    