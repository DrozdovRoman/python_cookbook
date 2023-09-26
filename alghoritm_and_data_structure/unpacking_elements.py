# Problem
# You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

data = ['ACME', 50, 90.1, (1, 2, 3)]

#Example 1
name, share, price, date = data
print(name, date)

#Example 2
name, share, price, (year, mon, day) = data
print(year, mon, day)

#Example 3
s = 'Hello'
a, b, c, d, e = s
print(a,b,c,d,e)

#Example 4
_, share, price, _ = data # _ unused var
print(share, price)


