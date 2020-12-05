import pandas as pd
import numpy as np

def scoreMotif(template, result, weightA, weightC, weightG, weightT):
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

	# Loop through all fully overlapping alignments
	for i in range(difference + 1):
		string1 = larger
		smaller.index = range(i,(i+shortLen))
		string2 = smaller
		score = scoreAlignment(string1, string2)
		score.loc[0:i - 1, 'A'] = abs(larger[0:i]['A'] - weightA)
		score.loc[0:i - 1, 'C'] = abs(larger[0:i]['C'] - weightC)
		score.loc[0:i - 1, 'G'] = abs(larger[0:i]['G'] - weightG)
		score.loc[0:i - 1, 'T'] = abs(larger[0:i]['T'] - weightT)
		score.loc[shortLen + i:, 'A'] = abs(larger[shortLen + i:]['A'] - weightA)
		score.loc[shortLen + i:, 'C'] = abs(larger[shortLen + i:]['C'] - weightC)
		score.loc[shortLen + i:, 'G'] = abs(larger[shortLen + i:]['G'] - weightG)
		score.loc[shortLen + i:, 'T'] = abs(larger[shortLen + i:]['T'] - weightT)
		currentScore = np.sum(score.to_numpy())
		if(currentScore < bestScore):
			bestScore = currentScore

	# Loop through all short rightshift alignments
	for i in range(difference, longLen):
		string1 = larger
		smaller.index = range(i,(i+shortLen))
		string2 = smaller
		score = scoreAlignment(string1, string2)
		score.loc[0:i - 1, 'A'] = abs(larger[0:i]['A'] - weightA)
		score.loc[0:i - 1, 'C'] = abs(larger[0:i]['C'] - weightC)
		score.loc[0:i - 1, 'G'] = abs(larger[0:i]['G'] - weightG)
		score.loc[0:i - 1, 'T'] = abs(larger[0:i]['T'] - weightT)
		score.loc[longLen:longLen+i, 'A'] = abs(smaller[longLen-i:]['A'] - weightA)
		score.loc[longLen:longLen+i, 'C'] = abs(smaller[longLen-i:]['C'] - weightC)
		score.loc[longLen:longLen+i, 'G'] = abs(smaller[longLen-i:]['G'] - weightG)
		score.loc[longLen:longLen+i, 'T'] = abs(smaller[longLen-i:]['T'] - weightT)
		currentScore = np.sum(score.to_numpy())
		if(currentScore < bestScore):
			bestScore = currentScore

	# Loop through all long rightshift alignments (aka short leftshift alignments)
	smaller.index = range(0,shortLen)
	for i in range(1, shortLen):
		string1 = smaller
		larger.index = range(i,(i+longLen))
		string2 = larger
		score = scoreAlignment(string1, string2)
		score.loc[0:i - 1, 'A'] = abs(smaller[0:i]['A'] - weightA)
		score.loc[0:i - 1, 'C'] = abs(smaller[0:i]['C'] - weightC)
		score.loc[0:i - 1, 'G'] = abs(smaller[0:i]['G'] - weightG)
		score.loc[0:i - 1, 'T'] = abs(smaller[0:i]['T'] - weightT)
		score.loc[shortLen:shortLen+i+difference, 'A'] = abs(larger[shortLen-i:]['A'] - weightA)
		score.loc[shortLen:shortLen+i+difference, 'C'] = abs(larger[shortLen-i:]['C'] - weightC)
		score.loc[shortLen:shortLen+i+difference, 'G'] = abs(larger[shortLen-i:]['G'] - weightG)
		score.loc[shortLen:shortLen+i+difference, 'T'] = abs(larger[shortLen-i:]['T'] - weightT)
		currentScore = np.sum(score.to_numpy())
		if(currentScore < bestScore):
			bestScore = currentScore

	return bestScore

def scoreAlignment(template, result):
	difference = abs(template - result)
	return difference

def main():
	with open('long_motif/motif.json') as f:
		template = pd.read_json(f)
	with open('long_motif/meme.json') as f:
		meme = pd.read_json(f)
	score = scoreMotif(template, meme, 0.25, 0.25, 0.25, 0.25)
	print(score)

if __name__ == "__main__":
	main()