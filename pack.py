import mainpack as mp
import mainpack.subpack1 as ms1
import mainpack.subpack2 as ms2
from mainpack.subpack1 import addsub as a1
from mainpack.subpack2 import muldiv as a2
print(mp.main)
print(mp.mainpackdemo())

print(ms1.sub)
print(ms1.subpackdemo1())
print(ms2.sub)
print(ms2.subpackdemo2())

print(a1.add(4,5))
print(a1.sub(10,5))
print(a2.mul(10,5))
print(a2.div(10,5))