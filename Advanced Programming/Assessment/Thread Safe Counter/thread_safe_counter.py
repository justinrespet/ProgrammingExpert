"""
Thread Safe Counter

Write a WordCounter class that is meant to be able to count words in large texts,
so that a user of that class can quickly calculate how many times a specific word 
occurs in a string.

WordCounter should implement the following methods:
 - process_text(text) should take in a string, text, and update the internal 
 attributes of WordCounter in a thread-safe manner
"""

import threading

lock = threading.Lock()