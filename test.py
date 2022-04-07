import unittest

from BasicTask import *

class TestIncome(unittest.TestCase):
	# test 3 random life images
	def test_life_image(self):
		"""
		Test that the image is equal to the correct life
		"""
		life = "200"
		image = cv2.imread("LifeTest200.png")
		answer = readLife(0,0,0,0,image)
		self.assertEqual(answer,life)

	def test_life_image2(self):
		"""
		Test that the image is equal to the correct life
		"""
		life = "170"
		image = cv2.imread("LifeTest170.png")
		answer = readLife(0,0,0,0,image)
		self.assertEqual(answer,life)
	
	def test_life_image3(self):
		"""
		Test that the image is equal to the correct life
		"""
		life = "135"
		image = cv2.imread("LifeTest135.png")
		answer = readLife(0,0,0,0,image)
		self.assertEqual(answer,life)


	# Test 3 random income images
	def test_income_image1(self):
		"""
		Test that the image is equal to the number
		"""
		number = "650"
		image = cv2.imread('IncomeTest650.png')
		answer = readIncome(0,0,0,0,image)
		self.assertEqual(answer,number)

	def test_income_image2(self):
		"""
		Test that the image is equal to the number
		"""
		number = "1156"
		image = cv2.imread('Income1156.png')
		answer = readIncome(0,0,0,0,image)
		self.assertEqual(answer,number)

	def test_income_image3(self):
		"""
		Test that the image is equal to the number
		"""
		number = "36582"
		image = cv2.imread('Income36582.png')
		answer = readIncome(0,0,0,0,image)
		self.assertEqual(answer,number)


	# Test 3 random rounds images
	def test_round_image1(self):
		"""
		Test that the image is equal to the round
		"""
		round = "1"
		image = cv2.imread('Round1.png')
		answer = readRound(0,0,0,0,image)
		self.assertEqual(answer,round)

	def test_round_image2(self):
		"""
		Test that the image is equal to the round
		"""
		round = "16"
		image = cv2.imread('Round16.png')
		answer = readRound(0,0,0,0,image)
		self.assertEqual(answer,round)

	def test_round_image3(self):
		"""
		Test that the image is equal to the round
		"""
		round = "38"
		image = cv2.imread('Round38.png')
		answer = readRound(0,0,0,0,image)
		self.assertEqual(answer,round)

if __name__ == '__main__':
	unittest.main()
