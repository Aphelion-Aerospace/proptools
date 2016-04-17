''' Unit conversions.
'''

from __future__ import division


def meter2inch(x):
	return x / 0.0254


def inch2meter(x):
	return x * 0.0254

def psi2pascal(x):
	return x * 6895

def pascal2psi(x):
	return x / 6895