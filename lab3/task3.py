#!/usr/bin/env python

# lab 3 - task 3
# simulate spring-mass-damper system


from smd import *
import matplotlib.pyplot as plt

if __name__ == "__main__":
	s = SpringMassDamper(m=10.0, k=10.0, c=1.0)
	state,t = s.simulate(0.0, 1.0)

	position = [pos[0] for pos in state]
	velocity = [vel[1] for vel in state]

	plt.figure(1)
	plt.plot(t, position, 'r-', label = 'position')
	plt.plot(t, velocity, 'b-', label = 'velocity')
	plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=1.)
	#plt.plot(t, state)
	plt.title('Simulation of spring-mass-damper system')
	plt.xlabel('time')
	plt.ylabel('position and velocity')
	plt.show()
