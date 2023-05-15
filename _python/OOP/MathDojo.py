class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
        self.result += num
        for self.a in nums:        
            self.result += self.a
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for self.a in nums:        
            self.result -= self.a
        return self
# create an instance:
md = MathDojo()

#Write the add method and test it by calling it 3 times, with different numbers of arguments each time
first = MathDojo()
second= MathDojo()
third = MathDojo()
a = first.add(9,5,7,8).result
print(a)
y = second.add(10,4,7).result
print(y)
z = third.add(2,8).result
print(z)

#Write the subtract method and test it by calling it 3 times, with different numbers of arguments each time
one = MathDojo()
two= MathDojo()
three = MathDojo()
a = one.subtract(9,5,7,8).result
print(a)
y = two.subtract(10,4,7).result
print(y)
z = three.subtract(2,8).result
print(z)

#Make sure you are able to chain methods as demonstrated above
test = MathDojo()
h = test.add(9,5,7,8).subtract(2,5,1).result
print(h)

# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

