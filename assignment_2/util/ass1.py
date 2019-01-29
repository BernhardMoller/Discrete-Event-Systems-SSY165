# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:36:26 2018

@author: Fredrik Möller
"""



def reach(events, trans, start_states, forbidden):
    """
    Returns the forward reachable states of a transition set
    
    :param events: set of events
    :param trans: set of transitions
    :param start_states: set of states
    :param forbidden: set of forbidden states
    """
    reach_states = start_states - forbidden
    last_reach_states = set()
    while not reach_states == last_reach_states:
        last_reach_states = reach_states.copy()
        t = filter_trans_by_source(trans, reach_states)
        t = filter_trans_by_events(t, events)
        reach_states |= (extract_elems_from_trans(t, 'target') - forbidden)
    return reach_states


def coreach(events, trans, start_states, forbidden):
    """
    Returns the coreachable (backward reachable) states of a transition set
    
    :param events: set of events
    :param trans: set of transitions
    :param start_states: set of states
    :param forbidden: set of forbidden states
    """
    return reach(events, flip_trans(trans), start_states, forbidden)


def synch(aut1, aut2):
    """
    Returns the synchronous composition of two automata.
    
    :param aut1: Automaton
    :param aut2: Automaton
    """
    states = cross_product(aut1.states, aut2.states)
    init = merge_label(aut1.init, aut2.init)
    events = aut1.events | aut2.events
    
    # Add self loops
    trans1 = aut1.trans.copy()
    for event in aut2.events - aut1.events:
        for state in aut1.states:
            trans1.add(Transition(state, event, state))
    
    trans2 = aut2.trans.copy()
    for event in aut1.events - aut2.events:
        for state in aut2.states:
            trans2.add(Transition(state, event, state))
    
    # Transitions
    trans = set()
    for t1 in trans1:
        for t2 in trans2:
            if t1.event == t2.event:
                trans.add(Transition(merge_label(t1.source, t2.source),
                                     t1.event,
                                     merge_label(t1.target, t2.target)))
    
    # Marked states
    m1 = aut1.marked if aut1.marked else aut1.states
    m2 = aut2.marked if aut2.marked else aut2.states
    marked = cross_product(m1,m2)
    
    # Forbidden states
    forbidden = cross_product(aut1.forbidden, aut2.states) | cross_product(aut1.states, aut2.forbidden)
    
    # Removing unreachable states
    reachable = reach(events, trans, {init}, set())
    marked &= reachable
    forbidden &= reachable
    trans = filter_trans_by_source(trans, reachable)
    
    # Create synchronized automaton
    return Automaton(reachable, init, events, trans, marked, forbidden)