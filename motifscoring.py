import pandas as pd
import numpy as np

def scoreMotif(template, result):
	bestScore = float('inf')

	if(template.shape[0] > result.shape[0]):
		larger = template
		smaller = result
	else:
		larger = result
		smaller = template
	longLen = larger.shape[0]
	shortLen = smaller.shape[0]
	difference = longLen - shortLen

	# Loop through all short rightshift alignments
	for i in range(difference, longLen):
		string1 = larger
		smaller.index = range(i,(i+shortLen))
		string2 = smaller
		# print(i)
		# print(string1)
		# print(string2)
		score = scoreAlignment(string1, string2)
		score[0:i] = abs(larger[0:i] - 0.25)
		score[longLen:longLen+i] = abs(smaller[longLen-i:] - 0.25)
		# print("SCORE")
		# print(score)
		# print(np.sum(score))
		print(np.sum(score.to_numpy()))
	return bestScore

def scoreAlignment(template, result):
	difference = abs(template - result)
	# result = np.sum(difference)
	return difference

def main():
	with open('long_motif/motif.json') as f:
		template = pd.read_json(f)
	with open('long_motif/memeBad.json') as f:
		meme = pd.read_json(f)
	# print(template)
	# print(meme)
	score = scoreMotif(template, meme)
	print(score)

if __name__ == "__main__":
	main()