'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math
    # test test is this actually syncing
    # john pls delete if yes

def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)

def dot(v1,v2):
    # Returns dot product of 2 vectors stored as a dictionary
    # Assumes v1 and v2 have same length
    dot_prod = 0.0
    for word, count in v1.items():
        for word2, count2 in v2.items():
            if word == word2:
                dot_prod += count*count2
    return dot_prod

def cosine_similarity(vec1, vec2):
    return (dot(vec1,vec2))/(norm(vec1)*norm(vec2))

def build_semantic_descriptors(sentences):
    dict_dict = {} # Dict containing dictionaries
    # inefficient ahh implementation
    for sentence in sentences:
        for word in sentence:
            if word not in dict_dict: # Create a new dict in dict dict if word is not in dict dict
                dict_dict[word] = {}
            for word2 in sentence: # Loop through every word in sentence again
                if word2 != word: 
                    if word2 not in dict_dict[word]:
                        dict_dict[word][word2] = 0
                    dict_dict[word][word2] += 1
    return dict_dict

def build_semantic_descriptors_from_files(filenames):
    # This function takes in a list containing lists of strings (words) representing sentences 
    # returns a dictionary d: for every word w that appears in at least one of the sentences
    d = {}
    for i in range(len(filenames)):
       text = open(filenames[i], "r", encoding="latin-1").read()
       text = text.replace("!", ".")
       text = text.replace("?", ".") # make everything a period so we can split on periods
       sentences = text.split(".") # split on periods to get sentences
       build_semantic_descriptors([sentence.split() for sentence in sentences]) # apply build_semantic_descriptors to the list of sentences
    return d

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    similar_list = []
    for choice in choices:
        if word not in semantic_descriptors or choice not in semantic_descriptors:
            similar_list.append(-1)
        similar_list.append(similarity_fn(semantic_descriptors[word],semantic_descriptors[choice]))
    
    return choices[similar_list.index(max(similar_list))]
    

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    # takes in a string filename which is the name of a file in the same format as test.txt
    # returns the percentage (i.e., float between 0.0 and 100.0) of questions on which most_similar_word() guesses the answer correctly 
        # using the semantic descriptors stored in semantic_descriptors and the similarity function similarity_fn.
    f = open(filename, "r", encoding="latin-1")
    f = f.replace(",", "\n")
    f = f.replace("—", "\n")
    f = f.replace(":", "\n")
    f = f.replace(";", "\n")
    f = f.replace("(", "\n")    
    f = f.replace(")", "\n")
    f = f.replace("'", "\n")
    f = f.replace('"', "\n")
    f = f.replace("-", "\n")
    f = f.replace("!", "\n")
    f = f.replace("?", "\n")
    f = f.replace(".", "\n")
    total_words = f.split("\n")

    word_dict = build_semantic_descriptors(total_words)
    word_count = 0
    correct_count = 0
    for word in total_words:
        word_count += 1
        correct_word = word_dict[word][0] # the first word has the highest freq so it's correct
        if most_similar_word(total_words[word], choices, semantic_descriptors, similarity_fn) == correct_word:
            correct_count += 1
        else:
            continue
    percentage_correct = float((correct_count/word_count)*100)
    return percentage_correct

if __name__ == "__main__":
    print(cosine_similarity({"a": 1, "b": 2, "c": 3},
 {"b": 4, "c": 5, "d": 6})) # Works First Try!
    sentences = [
        ["i", "am", "a", "sick", "man"],
        ["i", "am", "a", "spiteful", "man"],
        ["i", "am", "an", "unattractive", "man"]
    ]

    d = build_semantic_descriptors(sentences)

    print(d["i"])
    
    