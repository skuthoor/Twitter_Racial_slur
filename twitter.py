import re
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *
stemmer = PorterStemmer()

def remove_pattern(input_txt, pattern):  
  r = re.findall(pattern, input_txt)
  for i in r:
    input_txt = re.sub(i, '', input_txt)

  return input_txt

t_file = open('twitter.txt')                        # Opening Twitter tweet file

racial_slur = {"paki","whitey"}                            # set of words that indicate racial slurs

#racial_slur = list(stemmer.stem(i) for i in racial_slur)    #stemmming racial slur words

lines = t_file.readlines()
c =0
for line in lines:   
    line = line.lower() 
    line = remove_pattern(line,"@[\w]*")            #removing Twitter handles

    line = re.sub(r"[^a-zA-Z0-9]"," ",line)         # Remove special characters, numbers, punctuation

    line = word_tokenize(line)                      # Tokenization

#   line = list(stemmer.stem(i) for i in line)      #Stemming(use only if the racial slur words are stemmed)

    #degree_of_profanity of that line
    degree_of_profanity = sum(1 for t in line if t in racial_slur)/ len(line)
    print("line",c,":",degree_of_profanity)             
    c +=1
