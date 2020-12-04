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
	offset = longer.shape[0]
	length = smaller.shape[0]
	difference = offset - length

	for i in range(difference):
		string1 = larger.loc[offset:(offset+length), :]
		string2 = smaller.loc[]
	return test

def scoreAlignment(template, result):
	difference = abs(template - result)
	return difference

def main():
	with open('long_motif/motif.json') as f:
		template = pd.read_json(f)
	with open('long_motif/meme.json') as f:
		meme = pd.read_json(f)
	print(template)
	print(meme)
	score = scoreMotif(template, meme)
	print(score)

if __name__ == "__main__":
	main()