# Exercise 3
def time(s):
  h = (s//3600)%24
  m = (s%3600)//60
  s = s%60
  return f"{h}:{'0' if m < 10 else ''}{m}:{'0' if s < 10 else ''}{s}"

print(
  time(3602)
)
print(
  time(4556789)
)
print(
  time(4568)
)
# Your solution comes here
