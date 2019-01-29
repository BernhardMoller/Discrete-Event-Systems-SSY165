# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:04:09 2018

@author: Fredrik Möller
"""
import helper
def reach(events, trans, start_states, forbidden):
    """
    Returns the forward reachable states of a transition set
     
    :param events: set of events
    :param trans: set of transitions
    :param start_states: set of states
    :param forbidden: set of forbidden states
    """
    start_states=init
    #Q_prev = set() # Declare the reachable states variable
    reachable_states = ({start_states}.difference({forbidden})).copy() # Copy init-states excluding the forbidden states
     
    print('rs', reachable_states)
    if trans == set():
        print(reachable_states)
        return reachable_states # If no transitions remain return the set of reachable states
     
    trans_w_reach = helper.filter_trans_by_source(trans, reachable_states)
     
    if trans_w_reach == set():
        print('no source')
        return reachable_states
         
     
    cur_trans = trans_w_reach.pop()
    print('ct', cur_trans, 'forbidden source', cur_trans.source in forbidden, 'forbidden target', cur_trans.target in forbidden)
     
    if (cur_trans.source in forbidden) or (cur_trans.target in forbidden):
        trans.discard(cur_trans)
        print('forbidden')
        return reach(events, trans, reachable_states, forbidden)
         
    if (cur_trans.event in events):
        print('adding', cur_trans.target)
        reachable_states.add(cur_trans.target)
        trans.discard(cur_trans)
        return reach(events, trans, reachable_states, forbidden)
    else:
        trans.discard(cur_trans)
        print('else')
        return reach(events, trans, reachable_states, forbidden)
    
a1 = Automaton(states={1, 2},
               init=1,
               events={'a'},
               trans={Transition(1, 'a', 2)},
               forbidden={2})
reach_a1=reach(a1.events,a1.trans,{a1.init},a1.forbidden)