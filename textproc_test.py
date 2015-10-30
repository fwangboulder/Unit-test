#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    # Add Your Test Cases Here...
#question 1
    def test_string(self):
        text = "123"
# without double quote it will give an error that the processor requires a sring
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")
##question 2
    def test_count(self):
        text = "ABCdef"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 6, "'text' does not match input")
# add A-Z
##question 3
    def test_count_alpha(self):
        text = "123ABC"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 3, "'text' does not match input")
##question 4
    def test_count_numeric(self):

        text = "aA0123"
#add 0
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 4, "'text' does not match input")
###question 5
    def test_count_vowels(self):
        text = "123aoeiuA"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 6, "'text' does not match input")
#miss i 
##question 6
    def test_is_phonenumber(self):
        text = "480-559-2055"
        p = textproc.Processor(text)
        self.assertTrue(p.is_phonenumber(), "'text' does not match input")
#Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
