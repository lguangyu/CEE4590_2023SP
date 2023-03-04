#!/usr/bin/env python3

import matplotlib.pyplot
import numpy
import scipy.integrate


def hetero_org(y, t):
	S, X = y  # S = subtrate conc., X = MLVSS conc.

	# constants
	S_in = 400  # 400mg COD/L subtrate input
	HRT = 4  # 4d of HRT
	Y = 0.63  # sludge yield
	mu = 4.0  # specific growth rate, 4.0/d
	b = 0.4  # specific death rate, 0.4/d
	K_s = 10   # COD half-saturation constant

	monod = S / (S + K_s)
	dS_dt = S_in / HRT - mu * monod * X - S / HRT
	dX_dt = (Y * mu * monod - b - 1 / HRT) * X
	return [dS_dt, dX_dt]


# initial condition, 50mg COD/L substrate and 150mg COD/L sludge
y_init = [50, 150]

t = numpy.linspace(0, 5, 1000)  # timepoints to resolve S and X values
y = scipy.integrate.odeint(hetero_org, y_init, t)


# plot
ax = matplotlib.pyplot.gca()
handles = ax.plot(t, y, label=["sCOD", "MLVSS"])
ax.set_ylim(0, None)
ax.set_xlabel("time (day)")
ax.set_ylabel("MLVSS (mgCOD/L)\nsoluble COD (mgCOD/L)")
ax.legend(handles=handles, loc=4, frameon=False)

matplotlib.pyplot.show()
matplotlib.pyplot.close()
