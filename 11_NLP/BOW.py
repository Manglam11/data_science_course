import nltk
# we imported our module

paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""
# the text in which we will perform vector embedding
import re
# re libray will use for regular expression
from nltk.corpus import stopwords
# through this we will identify different stops words like is an the etc present in senetence.
from nltk.stem.porter import PorterStemmer
# for stemming we will use PorterStemer (the default stemer fo renlgish language
from nltk.stem import WordNetLemmatizer
# this will use for lemmetization means for converting a word in its' root form doest matter if verb 2nd 3rd or 4th form is used it will covert all smartly

ps = PorterStemmer()
# we created the instance of PorteStemer class
wordnet = WordNetLemmatizer()
# same instance of lemmatization class
sentences = nltk.sent_tokenize(paragraph)
# sentences is holding sent_kenize output. means our paragraph got seprated with '.'

corpus = []
# i don't understand this naming convention but however if we have created a empty list earlier means if future we will append something on it.

for i in range(len(sentences)):
    # we run for loop on how many sentences present in our paragraph.
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    # i don't know this re.sub method actually i m weak in regrular expresiion module it will be your responisiblity to explain this for furute use cases as well.
    review = review.lower()
    # i think now review is kind of string means that's why we are able to perform .lower() method.
    review = review.split()
    # what is this split method? does it split our strin gtext with space.
    #   review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    # i did't commendte this line sir commented and we also never run thsi, why this line is here?
    review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    # omg list compreshension. this line you have make me clear end to end. let me tell why i understand. we are running loop for each sentence ie review presnet every sentece. variabl eword is the word prent in sentence. and we are going than lemmetization on that word using our above defined object and appedning into review. and i think this whole process will only happend if that particular word is not present in stops word list of enlgish language. pls say i m right this time 🙏🏻😅
    review = ' '.join(review)
    #  joining means each review sentence joing one by one? means review is a list now na? so list joining happening?
    corpus.append(review)
    # then that list is we are appening again in our above list.


from sklearn.feature_extraction.text import CountVectorizer
# this code will use to call our countvecotizer class. but that hierachy is amzing pls explain

cv = CountVectorizer()
# we created the object
X_bow = cv.fit_transform(corpus).toarray()
# we are stoing the result inside X_bow var. fit_transform means fit + tranform. first the model will run all the corpus data then it will transform? what is this transformations should happend before model running ? and why toarray()
from sklearn.feature_extraction.text import TfidfVectorizer

tf = TfidfVectorizer()
X_tf = tf.fit_transform(corpus).toarray()
# same code for tfidf method.