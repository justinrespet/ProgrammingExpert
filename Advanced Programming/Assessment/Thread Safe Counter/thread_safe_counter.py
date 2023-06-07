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
        self.lock.acquire()
        wordList = text.split()
        for word in wordList:
            if word in self.wordDic:
                self.wordDic[word] += 1
            else:
                self.wordDic[word] = 1
        self.lock.release()

    def get_word_count(self, word):
        self.lock.acquire()
        if word in self.wordDic:
            count = self.wordDic[word]
        else:
            count = 0
        self.lock.release()
        return count


TEST_TEXT_1 = """
The Ares Program. Mankind reaching out to Mars to send people 
to another planet for the very first time and expand the horizons 
of humanity blah, blah, blah. The Ares 1 crew did their thing and 
came back heroes. They got the parades and fame and love of the world.

Ares 2 did the same thing, in a different location on Mars. They got 
a firm handshake and a hot cup of coffee when they got home.

Ares 3. Well, that was my mission. Okay, not mine per se. Commander 
Lewis was in charge. I was just one of her crew. Actually, I was the 
very lowest ranked member of the crew. I would only be “in command” of 
the mission if I were the only remaining person.
""".strip()

TEST_TEXT_2 = " ".join(["dog"] * 50000)

wc = WordCounter()
wc.process_text(TEST_TEXT_1)

# threads = []
# for _ in range(10):
#     thread = threading.Thread(target=wc.process_text, args=(TEST_TEXT_1,))
#     threads.append(thread)

# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

print(wc.get_word_count("the"))
print(wc.get_word_count("I"))
print(wc.get_word_count("and"))