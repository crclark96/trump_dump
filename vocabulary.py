import cPickle as pkl

FILENAME = 'vocabulary.pkl'

def updateVocabulary(wordList, file=FILENAME):
    '''
    input: list of strings
    return: null
    update vocabulary dictionary stored in file
    '''
    try:
        f = open(file, 'r+')
        vocabulary = pkl.load(f)
    except IOError, e:
        print e
        f = open(file, 'w')
        vocabulary = {}
        
    for word in wordList:
        if word in vocabulary.keys():
            vocabulary[word] = vocabulary[word]+1
        else:
            vocabulary[word] = 1
    f.close()
    pkl.dump(vocabulary, open(file,'w'))

def queryVocabulary(wordList, file=FILENAME):
    '''
    input: list of strings
    return: list of ints
    read word counts stored in vocabulary dictionary in file
    '''
    try:
        f = open(file, 'r+')
        vocabulary = pkl.load(f)
    except IOError, e:
        print e
        f = open(file, 'w')
        vocabulary = {}
    freqs = []
    for word in wordList:
        if word in vocabulary.keys():
            freqs.append(vocabulary[word])
        else:
            freqs.append(0)

    f.close()
    return freqs
