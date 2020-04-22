#Ataberk TÜRKOĞLU 180401021 https://github.com/ataberkdw/Programlama_lab
import sympy as sym
from sympy import Symbol
from sympy import pprint
from sympy import factorial
import matplotlib.pyplot as plt
p = Symbol("p")
x = Symbol("x")
n = Symbol("n")
part_1 = factorial(n)/(factorial(x)*factorial(n-x))
part_2 = (p**x)*((1-p)**(n-x))
binomial_dist = part_1*part_2
pprint(binomial_dist)
sym.plot(binomial_dist.subs({p:0.4,n:20}),(x,0,20),title="Binomial Distribution")

x_values = []
y_values = []
for value in range(0,20):
    x_values.append(value)
    y_values.append(binomial_dist.subs({n:20,p:0.4,x:value}).evalf())
plt.plot(x_values,y_values)
plt.show()
#Binomial Distribution n sayıda iki kategori sonucu veren denemelere uygulanır
#Araştırıcının ilgi gösterdiği kategori başarı olarak adlandırılır ve olasılığın p olduğu bilinir.
