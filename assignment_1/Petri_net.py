# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 17:31:37 2018

@author: Fredrik Möller
"""

from util import plot_petrinet
from collections import namedtuple

from string import ascii_lowercase



PetriNet = namedtuple(typename='PetriNet', field_names=['places', 'transitions', 'arcs'])
Place = namedtuple('Place', ['label', 'marking'])
Arc = namedtuple('Arc', ['source', 'target', 'weight'])

# You can use the ploting function to plot your petri net for S
def make_synchronized_petri_net_S():

    places_with_dot={Place('P1_1', 1),
                     Place('P2_1', 1),
                     Place('Sp1_1', 1),
                     Place('Sp2_1',1)}   
    
    places_no_dot={Place('P1_2', 0),
                   Place('P2_2', 0),
                   Place('Sp1_2', 0),
                   Place('Sp2_2', 0)}
    places=places_with_dot.union(places_no_dot)
    
    transitions=set()
    for letter in ascii_lowercase: 
        if letter != 'f': # change the 'letter' to the letter after the last wanted
            #print(letter)
            transitions.update({letter})
        else: 
            break 
           
    arcs={Arc('P1_1', 'a', 1),   Arc('a', 'P1_2', 1), 
          Arc('P1_2', 'b', 1),   Arc('b', 'P1_1', 1),
          Arc('Sp1_1', 'b', 1),  Arc('b', 'Sp1_2', 1),
          Arc('P2_1', 'c', 1),   Arc('c', 'P2_2', 1), 
          Arc('Sp1_2', 'c', 1),  Arc('c', 'Sp1_1', 1),
          Arc('Sp2_1', 'c', 1),  Arc('c', 'Sp2_2', 1),
          Arc('P2_2', 'd', 1),   Arc('d', 'P2_1', 1),
          Arc('Sp2_2','d', 1),   Arc('d', 'Sp2_1', 1),
          Arc('P2_2', 'e', 1),   Arc('e', 'P2_1', 1)}

#            
        
    sync_petri= PetriNet(places, transitions , arcs)
        
    return sync_petri
        
synced_petri = make_synchronized_petri_net_S()
plot_petrinet(synced_petri , 'synced_petri ')

#source= helper.extract_elems_from_trans(build.sync_trans, 'source')
#transition=helper.extract_elems_from_trans(trans, 'event')
#target= helper.extract_elems_from_trans(trans, 'target')
#
#
## bygger upp "variabeln" places baserat det inmatade setet med "states" 
##samt markerar med 1 eller 0 beroende på om de är marked eller inte
#places= set()
#for element in states: 
#    if element in marked_states:
#     places.add(Place(element,1))
#    else:
#         places.add(Place(element,0))
#     
        
        