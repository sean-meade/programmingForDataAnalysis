# Greatest common devisor

a = 50
b = 20

# old way
while b > 0:
  tmp = a
  a = b
  b = tmp % b

print(a)


c = 50
d = 20

# python way
while d > 0:
  c, d = d, c % d

print(c)