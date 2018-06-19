"""Fit a ploynomial to a given set of data points using optimization."""

import numpy as np
import pandas as pd
from matplotlib import style
from matplotlib import pyplot as plt
from scipy import optimize as opt

style.use('ggplot')

def error_poly(C, data):
	"""Compute error between given polynomial and observed data.

	Parameters
	----------
	`C`: numpy.poly1d object or equivalent array representation polynomial coefficients
	`data`: 2D array where each row is a point (x, y)

	Returns error as a single real value.
	"""
	# Metric: Sum of squared Y-axis differences
	err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
	return err

##########################################################

def fit_poly(data, error_func, degree=4):
	"""Fit a polynomial to given data, using supplied error function.

	Parameters
	----------
	`data`: 2D array where each row is a point (x, y)
	`error_func`: function that computes the error between a polynomial and observed degree

	Returns polynomial that minimizes the error function.
	"""
	# Generates initial guess for polynomial model (all coeffs = 1)
	Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))

	# Plot initial guess (optional)
	x = np.linspace(-5, 5, 21)
	plt.plot(x,
		np.polyval(Cguess, x),
		'm--',
		linewidth=2.0,
		label='Initial guess')

	# Call optimizer to minimize error function
	result = opt.minimize(
		fun=error_func,
		x0=Cguess,
		args=(data,),
		method='SLSQP',
		options={'disp': True})
	return np.poly1d(result.x)

##########################################################

def test_run():
	# Define original line
	poly_orig = np.poly1d(np.float32([1.5, -10, 5.0, 60, 50]))
	print 'Original polynomial: '
	print '{}'.format(np.poly1d(poly_orig))

	Xorig = np.linspace(-5, 5, 21)
	Yorig = np.polyval(poly_orig, Xorig)

	plt.plot(
		Xorig,
		Yorig,
		color='r',
		linewidth=2.0,
		label='Original Polynomial')

	# Generate noisy data points
	noise_sigma = 3.0
	noise = np.random.normal(0, noise_sigma, Yorig.shape)
	data = np.asarray([Xorig, Yorig + noise]).T

	plt.plot(
		data[:, 0],
		data[:, 1],
		'bo',
		label='Data points')

	# Try to fit a polynomial to this data
	p_fit = fit_poly(data, error_poly)
	print 'Fitted polynomial: '
	print '{}'.format(np.poly1d(p_fit))

	plt.plot(
		data[:, 0],
		np.polyval(p_fit, data[:, 0]),
		color='g',
		linewidth=2.0,
		label='Fitted polynomial')

	plt.title('Fitting Polynomial')
	plt.legend()
	plt.show()

if __name__ == '__main__':
	test_run()
