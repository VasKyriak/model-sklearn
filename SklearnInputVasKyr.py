fo = open ('tm_alpha_beta_3state.txt', 'r')

#window size optional input
win = int(input('Type your odd number window size: '))

#number of zeros added next to window at the beginning and the end of the sequence
win_extra = int(win/2 - 0.5)

#create list of ID, aminoacids, structures
list_ID = []
list_amino = []
list_struct = []
list_word = []

#create list of my txt
list_all = list()

#remove line breaks
for line in fo:
    newline = line.replace('\n', '')
    list_all.append(newline)

#print(list_all)

#For all lists we are appending, we have a pattern from our dataset where the first line is the ID, the second line is
#the seq and the third line are the features. So we append the lists according to that pattern. We tell the program to
#put in each list the first, second, or third line and then the line we need is every third line after that.

for i in range (0, len(list_all), 3):
    list_ID.append(list_all[i])

#Appending the aminoacid list. We always need the middle residue in order to associate the window with a feature,
#so we put zeros in the beginning and the end of the seq to fill in the gaps for the first and last residues in the seq

for i in range (1, len(list_all), 3):
	seq = '0'*win_extra + list_all[i] + '0'*win_extra 
	list_amino.append(seq)
	for j in range(win_extra,len(seq)-win_extra):
		win_new = seq[j-win_extra:j+win_extra+1]
		list_word.append(win_new)
#print (win_new)

for i in range (2, len(list_all), 3):
    list_struct.append(list_all[i])

#Mapping our features to numbers
map = {'G': 1, 'M': 2, 'I':3, 'O':4}
features = ''.join(list_struct)
features = [char for char in features]
features = [map[i] for i in features]
#print (features)

#Mapping the aminoacids to numbers
map = {'A': 1, 'C':2, 'D':3, 'E':4,'F':5, 'G':6, 'H':7, 'I':8, 'K':9, 'L':10, 'M':11, 'N':12, 'P':13, 'Q':14, 'R':15, 'S':16, 'T':17, 'V':18, 'W':19, 'Y':20, 'X':21, '0':0}

#Appending windows with features
windfeat = []
for element in list_word:
	temp = []
	for char in element:
		feat = map[char]
		temp.append(feat)
	windfeat.append(temp)

#print (len(windfeat))

#One hot encoding
from sklearn import preprocessing 
enc= preprocessing.OneHotEncoder()
enc.fit(windfeat)
windfeat = enc.transform(windfeat).toarray()

#print (len(features))
#print (len(windfeat))

from sklearn import svm
lin_clf = svm.LinearSVC()
lin_clf.fit(windfeat, features)