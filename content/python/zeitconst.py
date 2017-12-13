import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

U1, t1 = np.genfromtxt('content/values/aufladung.txt',unpack=True)
U2, t2 = np.genfromtxt('content/values/entladung.txt',unpack=True)
t1/=1000
t2/=1000

t1 -= t1[0]
#U1 -= U1[0]
#U2 -= U2[len(U2)-1]
U1+=10
U2+=10


print(U1, U2, t1)
def f1(x, a, b):
    return b*(1-np.exp(x/(-a)))
def f2(x,a,b):
    return b*np.exp(-x/a)
parameters2, pcov2 = curve_fit(f2, t2, U2,p0=(0.001, 1))
parameters1, pcov1 = curve_fit(f1, t1, U1)
errors1 = np.sqrt(np.diag(pcov1))
errors2 = np.sqrt(np.diag(pcov2))

print('RC= ',parameters1[0],'pm',errors1[0])
print('U_0= ',parameters1[1],'pm',errors1[1])
print('RC= ',parameters2[0],'pm',errors2[0])
print('U_0= ',parameters2[1],'pm',errors2[1])
ln = np.linspace(t1[0],t1[len(t1)-1],5000)

plt.plot(ln, f1(ln, *parameters1), 'r-', label='Fit Aufladung')
plt.plot(ln, f2(ln, *parameters2), 'b-', label='Fit Entladung')
plt.plot(t1, U1,'rx',label='Werte Aufladung')
plt.plot(t2, U2,'bx',label='Werte Entladung')
plt.xlabel(r'$t/[s]$')
plt.ylabel(r'$U/[V]$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/zeitconst.pdf')
print('------------------')
