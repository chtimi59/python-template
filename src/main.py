import sys
import camelcase
from mypackage.fibo import *

if __name__ == "__main__":
    print(sys.argv[1:])
    fib(10)
    c = camelcase.CamelCase()
    txt = "hello world"
    print(c.hump(txt))
