# Copyright © 2022 AlgoExpert LLC. All rights reserved.

import threading


class WordCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.word_counts = {}

    def process_text(self, text):
        words = text.split(" ")
        for word in words:
            self._increment_word_count(word)

    def get_word_count(self, word):
        self.lock.acquire()
        count = self.word_counts.get(word, 0)
        self.lock.release()
        return count

    def _increment_word_count(self, word):
        self.lock.acquire()
        self.word_counts[word] = self.word_counts.get(word, 0) + 1
        self.lock.release()


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