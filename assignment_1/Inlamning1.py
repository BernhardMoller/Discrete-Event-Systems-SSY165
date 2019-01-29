# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 15:20:37 2018

@author: Fredrik Möller
"""
#imports 
import Automaton as auto 

states = {'p11', 'p12'}
init = 'p11'
events = {'a', 'b'}
trans = {auto.Transition('p11', 'a', 'p12'),
         auto.Transition('p12', 'b', 'p11')}
marked = {'p11', 'p12'}

start_states= states

p1 = auto.Automaton(states, init, events, trans, marked)

#coreachable_states = co_reach.coreach(events, trans,start_states, forbidden)
#print(coreachable_states)