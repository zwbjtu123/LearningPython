def add(a, b):
     return a + b

def multiply(a, b):
     return a*b

def subtraction(a, b):
     return  a - b

# 测试函数
def testfunction(a, b):
     c = subtraction(a, b)
     d = multiply(a, b)
     return c + d


if __name__ == "__main__":
     c = add(2, 3)
     f = testfunction(44, 5)
     print(c)
     print(f)
     print("Test main")


