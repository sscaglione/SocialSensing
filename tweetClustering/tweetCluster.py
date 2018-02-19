#!/usr/bin/env python2.7
# coding: utf-8

# Samantha Scaglione
# Social Sensing
# 19 February 2018
# tweetCluster.py
#	this program implements a tweet clustering function
#	using the Jaccard Distance metric and K-means
#	clustering  algortithm to cluster redundant/repeated
#	tweets into the same cluster

import sys
import json
import string
import copy

class kMean():

	def __init__(self, seeds, tweets):
		self.seeds = seeds
		self.tweets = tweets
		self.max_iterations = 1000
		self.k = len(seeds)
		
		self.clusters = {}
		self.revClusters = {}
		self.jaccard = {}
	
		self.initializeClusters()
		self.initializeMatrix()

	def jaccardDistance(self, setA, setB):
		try:
			return 1 - float(len(setA.intersection(setB)))/float(len(setA.union(setB)))
		except TypeError:
			print 'Invalid type. Type set expected.'

	def initializeClusters(self):
		for ID in self.tweets:
			self.revClusters[ID] = -1
		for k in range(self.k):
			self.clusters[k] = set([self.seeds[k]])
			self.revClusters[self.seeds[k]] = k

	def initializeMatrix(self):
		for ID1 in self.tweets:
			self.jaccard[ID1] = {}
			wordSet1 = set(self.getWords(self.tweets[ID1]['text']))
			for ID2 in self.tweets:
				if ID2 not in self.jaccard:
					self.jaccard[ID2] = {}
				wordSet2 = set(self.getWords(self.tweets[ID2]['text']))
				distance = self.jaccardDistance(wordSet1, wordSet2)
				self.jaccard[ID1][ID2] = distance
				self.jaccard[ID2][ID1] = distance

	def getWords(self, string):
		words = string.lower().strip().split(' ')
		for word in words:
			word = word.rstrip().lstrip()
			yield word

	def newClusterCalc(self):
		newClusters = {}
		newRevClusters = {}
		for k in range(self.k):
			newClusters[k] = set()
		for ID in self.tweets:
			minDist = float("inf")
			minClust = self.revClusters[ID]
			for k in self.clusters:
				dist = 0
				count = 0
				for ID2 in self.clusters[k]:
					dist += self.jaccard[ID][ID2]
					count += 1
				if count > 0:
					meanDist = dist/float(count)
					if minDist > meanDist:
						minDist = meanDist
						minCluster = k
			newClusters[minCluster].add(ID)
			newRevClusters[ID] = minCluster
		return newClusters, newRevClusters

	def converge(self):
		newClusters, newRevClusters = self.newClusterCalc()
		self.clusters = copy.deepcopy(newClusters)
		self.revClusters = copy.deepcopy(newRevClusters)
		iterations = 1
		while iterations < self.max_iterations:
			newClusters, newRevClusters = self.newClusterCalc()
			iterations += 1
			if self.revClusters != newRevClusters:
				self.clusters = copy.deepcopy(newClusters)
				self.revClusters = copy.deepcopy(newRevClusters)
			else:
				return

	def writeClusters(self):
		f = open("clusterOutput.txt", "w")
		for k in self.clusters:
			f.write(str(k) + ':' + ','.join(map(str, self.clusters[k])))
			f.write('\n\n')

def main():
	if len(sys.argv) != 3:
		print >> sys.stderr, 'Usage: python %s [dataset json] [initial seeds file]' % (sys.argv[0])
		exit(-1)
	tweets = {}
	with open(sys.argv[1], 'r') as f:
		for line in f:
			tweet = json.loads(line)
			tweets[tweet['id']] = tweet
	f = open(sys.argv[2])
	seeds = [int(line.rstrip(',\n')) for line in f.readlines()]
	f.close()
	kmeans = kMean(seeds, tweets)
	kmeans.converge()
	kmeans.writeClusters()

if __name__ == '__main__':
	main()
