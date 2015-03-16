import pyio
import numpy

def constant(n, value):
    return numpy.array([value for i in xrange(n)])

def step(n, x_0):
    return numpy.array([0.5*(numpy.sign(l*i - x_0)+1) for i in xrange(n)])
    
def gaussian(n, a, w, x_0):
    return numpy.array([a*numpy.exp(-(2.0*(l*i - x_0)/(w))**2) for i in xrange(n)])

def gaussian_deriv(n, a, w, x_0):
    return numpy.array([-4.0*((l*i - x_0)/(w))*a*numpy.exp(-(2.0*(l*i - x_0)/(w))**2) for i in xrange(n)])

format = 1
find_energy = True
sets = 10
set_size = 10
sparse = 1000
integrator = 3
iolevel = 1
n = 100
g = 9.82
length = 1.0
time = 3.33

l = length / float(n)
dt = time / float(sets*set_size*sparse)
#theta = gaussian_deriv(n, 0.1, 0.4, 0.2)
theta = constant(n, 1.7)
theta_d = gaussian_deriv(n, 2.0, 0.4, 0.2)
#theta = constant(n, 1.57)+constant(n, 1.57)*step(n, 0.5)
#theta_d = constant(n, -0.1)
theta_dd = constant(n, 0.0)

file_out = pyio.pyio("initalization.dat")
file_out.initalize("initalization.dat", format, find_energy, sets, set_size, integrator, iolevel, sparse, l, g, dt, theta, theta_d, theta_dd)
