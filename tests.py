#!/usr/bin/env python
# -*- coding: latin-1 -*-

from compression import *
import unittest
import string


class CompressionTests(unittest.TestCase):
	def setUp(self):
		# { 'originalText' : 'compressedText' }
		self.testData = { 
			'A' : 'A',
			'AA' : 'AA0',
			'AAA' : 'AA1',
			'AAB' : 'AA0B',
			'AABB' : 'AA0BB0',
			'ABAC' : 'ABAC',
			'AAAAAAAAAAAAA' : 'AA9AA0',
			'AAACBBC' : 'AA1CBB0C',
			'AAANBC' : 'AA1NBC',
			'AAAnBC' : 'Invalid', 	# Non-capital English letter
			'AAA1BC' : 'Invalid', 	# Number in string
			'Olé' : 'Invalid',			# Unicode
			'Hooray!' : 'Invalid',	# Punctuation mark
		}

	def testCompression(self):
		for (input, output) in self.testData.iteritems():
			if output is 'Invalid':
				self.assertRaises(ValueError, compress, input)
			else:
				compressed = compress(input)
				self.assertTrue(output == compressed)

	def testDecompression(self):
		invalidators = ('é', 'e')
		for (input, output) in self.testData.iteritems():
			if output is not 'Invalid':
				decompressed = decompress(output)
				self.assertTrue(input == decompressed)

				for invalidator in invalidators:
					# Append a non-capital or non-ASCII character to valid input
					badInput = input + invalidator
					self.assertRaises(ValueError, decompress, badInput)

	def testInverse(self):
		for (input, output) in self.testData.iteritems():
			if output is not 'Invalid':
				self.assertTrue(input == decompress(compress(input)))

if __name__ == '__main__':
	unittest.main()
