# Install necessary packages if not already installed
if (!require("tm")) install.packages("tm")
if (!require("SnowballC")) install.packages("SnowballC")
if (!require("wordcloud")) install.packages("wordcloud")
if (!require("RColorBrewer")) install.packages("RColorBrewer")

library(tm)
library(SnowballC)
library(wordcloud)
library(RColorBrewer)

# Set working directory and read text file
setwd("C:/Users/Khushi/OneDrive/Desktop/data+codes") 
text <- readLines(file.choose())

# Create corpus and preprocess text
# Corpus are collections of documents containing (natural language) text
docs <- Corpus(VectorSource(text))

# Apply transformations
docs <- tm_map(docs, content_transformer(tolower))
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, stripWhitespace)
inspect(docs) 

# Create Document-Term Matrix
dtm <- TermDocumentMatrix(docs) # algorithm for NLP
inspect(dtm)

# Convert DTM to matrix and get word frequencies
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing <- TRUE)
d <- data.frame(word<-names(v),freq<-v)

# View the top 10 words by frequency
head(d,10) 

# Display the word cloud
set.seed(1234)
wordcloud(words = d$word, freq = d$freq, min.freq = 1, max.words = 200, random.order = FALSE, rot.per = 0.35, colors = brewer.pal(8, "Dark2"))
