"""Fit a line to a given set of data points using optimization."""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
from scipy import optimize as opt

style.use('ggplot')

def error(line, data):
	"""Compute error between given line model and observed data.
	
	Parameters
	----------
	`line`: tuple/list/array (C0, C1) where C0 is slope and C1 is Y-intercept\n
	`data`: 2D array where each row is a point (x, y)

	Returns error as a single real value.
	"""
	# Metric: Sum of squared Y-axis difference
	err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)
	return err

##########################################################

def fit_line(data, error_func):
	"""Fit a line to given data, using a supplied error function.

	Parameters
	----------
	`data`: 2D array where each row is a point (X0, Y)\n
	`error_func`: function that computes the error between a line and observed data

	Returns line that minimizes the error function.
	"""
	# Generate initial guess for line model
	l = np.float32([0, np.mean(data[:, 1])]) # slope = 0, intercept = mean(y values)

	# Plot initial guess (optional)
	x_ends = np.float32([-5, 5])
	plt.plot(
		x_ends,
		l[0] * x_ends + l[1],
		'm--',
		linewidth=2.0,
		label='Initial guess')

	# Call optimizer to minimize error function
	result = opt.minimize(
		fun=error_func,
		x0=l,
		args=(data,),
		method='SLSQP',
		options={'disp': True})
	return result.x

##########################################################

def test_run():
	# Define original line
	l_orig = np.float32([4, 2])
	print "Original line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1])
	Xorig = np.linspace(0, 10, 21)
	Yorig = l_orig[0] * Xorig + l_orig[1]
	plt.plot(
		Xorig,
		Yorig,
		color='r',
		linewidth=2.0,
		label='Original line')

	# Generate noisy data points
	noise_sigma = 3.0
	noise = np.random.normal(0, noise_sigma, Yorig.shape)
	data = np.asarray([Xorig, Yorig + noise]).T
	plt.plot(
		data[:, 0],
		data[:, 1],
		'bo',
		label='Data points')

	# Try to fit a line to this data
	l_fit = fit_line(data, error)
	print "Fitted line: C0 = {}, C1 = {}".format(l_fit[0], l_fit[1])
	plt.plot(
		data[:, 0],
		l_fit[0] * data[:, 0] + l_fit[1],
		color='g',
		linewidth=2.0,
		label='Fitted line')
	
	plt.title('Fitting Line')
	plt.legend()
	plt.show()

if __name__ == '__main__':
	test_run()
