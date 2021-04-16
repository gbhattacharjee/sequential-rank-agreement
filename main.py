# Author: Gitanjali Bhattacharjee
# Purpose: Compute the Sequential Rank Agreement (SRA) of items in lists per Ekstrom et al. 2019, "Sequential rank agreement
# for comparison of ranked lists." Variable names in the code match those in the paper.

import csv
import numpy as np
from itertools import chain
import matplotlib.pyplot as plt


def get_ranking(Xp, list):

	return list.index(Xp)

def get_average_ranking(Xp, listOfLists): # R-bar in paper

	L = len(listOfLists)
	rBar = np.average([get_ranking(Xp, listOfLists[l]) for l in range(0,L)])

	return rBar

def get_variance(Xp, listOfLists): # this is A-hat-sub-L in paper

	L = len(listOfLists)

	rBar = get_average_ranking(Xp, listOfLists)

	sum = 0
	for l in range(0,L):
		sum += (get_ranking(Xp, listOfLists[l]) - rBar)**2

	sum = sum/(L - 1)

	return sum

def get_sHat(d, listOfLists, epsilon = 0, verbose = False):

	# Get the set of unique items ranked less than or equal to d in an of the L lists.

	sHat = []

	L = len(listOfLists)

	# Abbreviate lists to length d. #TODO check indexing of d -- starting at 0 or 1?

	shortLists = []

	for l in range(0, L):

		shortLists.append(listOfLists[l][0:d])

	# Get the unique items in shortLists.
	listTuple = (shortLists[0])

	for l in range(1,L):
		listTuple = listTuple + (shortLists[1])

	# Combine all the lists into one
	super_list = list(chain(*shortLists))
	super_set = set(super_list)

	if verbose:
		print(d, super_set)

	sHat = super_set

	return sHat

def compute_sra(d, listOfLists, verbose = False): # d is a particular rank


	L = len(listOfLists)

	sHat = get_sHat(d, listOfLists, verbose=verbose)

	sra = 0

	for p in sHat:
		sra += (L - 1) * get_variance(p, listOfLists)

	sra = sra/((L-1)*len(sHat))

	return sra

def verification_problem(): # compare to Table 1(c) in Ekstrom et al. 2019

	listOfLists = [['A', 'B', 'C', 'D', 'E'], ['A', 'C', 'D', 'B', 'E'], ['B', 'A', 'E', 'C', 'D']]

	for i in range(1, 6):
		sra = compute_sra(i, listOfLists, verbose=True)

	print(sra)

def import_listOfLists(csv_filepath, nCols):

	# fp = 'Bridges ranked - test.csv'
	listOfLists = []
	for col in range(0,nCols):
		ranking = np.loadtxt(csv_filepath,dtype=str,delimiter=',',skiprows=1,usecols=(col,))
		listOfLists.append(list(ranking))

	return listOfLists

def plot_sra(csv_filepath, nCols):

	listOfLists = import_listOfLists(csv_filepath, nCols)

	depth = []
	sra = []
	nElements = len(listOfLists[0])

	for i in range(1, nElements + 1):

		temp = compute_sra(i, listOfLists)
		sra.append(temp)
		depth.append(i)

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(depth, sra)
	ax.set_xlabel('Depth of list')
	ax.set_ylabel('Sequential rank agreement')
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')
	plt.savefig('sra.png', bbox_inches='tight')

verification_problem()