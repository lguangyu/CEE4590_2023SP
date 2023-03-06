#!/usr/bin/env python3

import matplotlib.pyplot
import numpy
import scipy.integrate


def kermack_sir(y, t):
	S, I, R = y  # S = susceptible, I = infected, R = removed (recovered)

	# constants
	beta = 2.0
	gamma = 0.5

	dS_dt = -beta * S * I  # new infects when S and I contact with prob. beta
	dR_dt = gamma * I  # infects removed with prob. gamma
	dI_dt = -dS_dt - dR_dt  # infects net change ((S>I) - (I>R))

	return [dS_dt, dI_dt, dR_dt]


# initial condition,
# seed with 0.001% infection
infect_init = 0.00001
y_init = [1.0 - infect_init, infect_init, 0.0]

t_max = 30
t = numpy.linspace(0, t_max, 1000)  # timepoints to resolve
y = scipy.integrate.odeint(kermack_sir, y_init, t)

# plot
ax = matplotlib.pyplot.gca()
label = ["susceptible", "infected", "removed"]

handles = list()
base_y = numpy.zeros(t.shape, dtype=float)
for curr_y, l in zip(y.T, label):
	p = ax.fill_between(t, base_y, base_y + curr_y, edgecolor="none", label=l)
	handles.append(p)
	base_y += curr_y

ax.legend(handles=handles, loc=1, frameon=True)
ax.set_xlim(0, t_max)
ax.set_ylim(0, 1)
ax.set_xlabel("time (day)")
ax.set_ylabel("population")

matplotlib.pyplot.show()
matplotlib.pyplot.close()
