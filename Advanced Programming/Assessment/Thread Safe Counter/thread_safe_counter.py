"""
Thread Safe Counter

Write a WordCounter class that is meant to be able to count words in large texts,
so that a user of that class can quickly calculate how many times a specific word 
occurs in a string.

WordCounter should implement the following methods:
 - process_text(text) should take in a string, text, and update the internal 
 attributes of WordCounter in a thread-safe manner. You may assume naively that
 text.split(" ") is good enough to return the list of words in the passed text.
 - get_word_count(word) should take a string, word, and check how many times 
 that word has been seen in all the texts that this WordCounter has processed.
 If this word has never been seen, you should return 0.

 NOTE: This class must be thread-safe, meaning that many threads should be able 
 to use the WordCounter at the same time, and the calculations must remain accurate
 as if only a single thread was using the instance of WordCounter
 NOTE: You may not use the Counter class of the collections standard library
"""

import threading

class WordCounter:
    def __init__(self):
        # I'm going to need a dictionary and a lock
        # Thread safety will need to be ensured whenever adding 
        # or checking word in dictionary
        self.wordDic = {}
        self.lock = threading.Lock()

    def process_text(self, text):
        wordList = text.split()
        for word in wordList:
            self.lock.acquire()
            if word in self.wordDic:
                self.wordDic[word] += 1
            else:
                self.wordDic[word] = 1
            self.lock.release()

    def get_word_count(self, word):
        self.lock.acquire()
        if word in self.wordDic:
            return self.wordDic
        else:
            return 0
        self.lock.release()