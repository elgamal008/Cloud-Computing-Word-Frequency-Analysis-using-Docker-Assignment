import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Download the necessary NLTK packages
nltk.download('punkt')
nltk.download('stopwords')

with open(r"random_paragraphs.txt", 'r') as file:
    # Read the contents of the file
    paragraph = file.read()
    #print(paragraph)

stop_words = set(stopwords.words('english'))

# Tokenize the paragraph into words
paragraph_tokens = word_tokenize(paragraph)

# Now, word_tokens contains the words in the paragraph
#print(paragraph_tokens)
# Filter out the stop words
filtered_paragraph = [word for word in paragraph_tokens if not word in stop_words]

# Now, filtered_words contains the words in the paragraph after removing the stop words
#print(filtered_paragraph)
word_freq = Counter(filtered_paragraph)
print(word_freq)

