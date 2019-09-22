digits=[1,5,4]
def min_value(digits):
  digits = Remove(digits)
  digits = sorted(digits)
  min = ''
  for i in digits:
    min += str(i)
  return int(min) 
  print(min_value(digits))  