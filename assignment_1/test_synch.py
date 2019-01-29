# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:05:39 2018

@author: Fredrik Möller
"""
import Automaton as auto


b1 = auto.Automaton(states={'a', 'b'},
               init='a',
               events={1},
               trans={auto.Transition('a', 1, 'b')},
               marked={'b'})
b2 = auto.Automaton(states={'c', 'd', 'e'},
               init='c',
               events={1, 2},
               forbidden={},
               trans={auto.Transition('c', 1, 'd'), auto.Transition('d', 2, 'e'), auto.Transition('e', 1, 'c')})


aut1=b1
aut2=b2