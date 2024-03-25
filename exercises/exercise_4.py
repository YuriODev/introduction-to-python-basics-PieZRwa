# Exercise 4
def solution1():
  def ifSymmetric(n):
    return int(str(n) == str(n)[::-1])
  
  print(ifSymmetric(2002))
  print(ifSymmetric(1234))
  print(ifSymmetric(1221))
# Your solution comes here
