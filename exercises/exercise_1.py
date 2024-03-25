# Exercise 1
def newNum(n):
  n = str(n)
  if len(n) != 5:
    return -1
  return int(f"{sum([int(n[0]),int(n[2]),int(n[4])])}{sum([int(n[1]),int(n[3])])}")

print(newNum(12345))
# Your solution comes here
