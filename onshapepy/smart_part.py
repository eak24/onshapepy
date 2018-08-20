from sympy import *
import sympy.physics.units as u
init_printing(pretty_printer=True)

L, w, h = symbols('L, w, h')

v = L*w*h

conf={L: 1, w: 3, h: 1}

print(v.subs(conf))

print(v.subs({L: 1, w: 3}).atoms(Symbol))

