# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:03:51 2018

@author: Fredrik Möller
"""

import Helperfunctions as help
import Automaton as auto 
import Inlamning1 as inl
import numpy as n
import itertools


# Implement reachfunction ############3
def reach(events, trans, start_states, forbidden):
    """
    Returns the forward reachable states of a transition set

    :param events: set of events
    :param trans: set of transitions
    :param start_states: set of states
    :param forbidden: set of forbidden states
    """
    check_start_state=set()
    start_states= init 
    states_to_keep= states.difference(forbidden)
    transitions_w_reach=help.filter_trans_by_source(trans,states_to_keep)
    trans_sources=help.extract_elems_from_trans(Transitions_w_reach,'source')
    trans_events=help.extract_elems_from_trans(Transitions_w_reach,'event')
    
    if trans_sources.issubset(states_to_keep) and events.issubset(trans_events):  
        reach_states=states_to_keep
    else:  
         check_start_state = trans_sources.pop()    

    
    return reach_states







