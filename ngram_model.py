from nltk.model.ngram import NgramModel
from nltk.probability import LidstoneProbDist
import re,string

def build_model(word_string):
	words = word_string.replace('\n',' ').replace('\t',' ')
	#split_delim = "|".join(["\%s" % s for s in string.punctuation + " "])
	#words = re.split(split_delim,words)
	words = re.findall('[a-zA-Z]+|[%s]+' % string.punctuation, words)
	words = [w.strip() for w in words]
	est = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
	model = NgramModel(6, words, estimator=est)
	return model



if __name__ == "__main__":
	with open("enronsent/enronsent00",'r') as email_file:
		word_string = email_file.read()
		model = build_model(word_string)
	