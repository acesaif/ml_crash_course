import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
from scipy import optimize as opt

style.use('ggplot')

def func(X):
	"""Given a scalar `X`, return some a value `y` (real number)."""
	Y = (X - 1.5)**2 + 0.5
	print("X : {}, Y : {}".format(X, Y)) # for tracing how values change by the optimizer
	return Y

def test_run():
	"""Returns the optimization summary and final result."""
	Xguess = float(np.random.randint(0, 3))
	min_result = opt.minimize(
		func,
		Xguess,
		method='SLSQP', # Sequential Least SQuares Programming
		options={'disp': True})
	print('\nMinima found at: ')
	print('X : {} Y : {}\n\n'.format(min_result.x, min_result.fun))

	# Plot function values and mark minima
	Xplot = np.linspace(0.5, 2.5, 21)
	Yplot = func(Xplot)
	print("\n{}".format(min(Yplot)))

	plt.plot(Xplot, Yplot, label='Objective Function')
	plt.plot(min_result.x, min_result.fun, 'go', label='minima')
	plt.title('Minima of an Objective Function')
	plt.legend()
	# plt.tight_layout()
	plt.show()

if __name__ == '__main__':
	test_run()
