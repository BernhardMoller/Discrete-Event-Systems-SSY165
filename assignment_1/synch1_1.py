# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:52:11 2018

@author: Fredrik Möller
"""
import Automaton as auto
import helper
def synch(aut1, aut2):
    """
    Returns the synchronous composition of two automata.
    
    :param aut1: Automaton
    :param aut2: Automaton
    """
    import helper as help
    import automaton as auto 

    sync_events=help.extract_elems_from_trans(aut1.trans,'event').union(help.extract_elems_from_trans(aut2.trans,'event')) 
    sync_trans= set()
    for event in sync_events:
        if event not in aut1.events:
            for y in aut1.states:
                aut1.trans= aut1.trans.union({auto.Transition(y , event, y) })#for y in aut1.states
                
        if event not in aut2.events:
            for y in aut2.states:
                aut2.trans= aut2.trans.union({auto.Transition(y , event, y) }) #for y in aut1.states
    
    for event in sync_events:            
        for transition1 in help.filter_trans_by_events( aut1.trans, {event} ):
            for transition2 in help.filter_trans_by_events( aut2.trans, {event} ):
                source = help.merge_label( help.extract_elems_from_trans({transition1},'source').pop(), help.extract_elems_from_trans({transition2},'source').pop() )
                target = help.merge_label( help.extract_elems_from_trans({transition1},'target').pop(), help.extract_elems_from_trans({transition2},'target').pop() )
                sync_trans.add( auto.Transition( source, event, target ) )
    
    
    # initial states, as a "label" not set 
    sync_init= help.merge_label(aut1.init,aut2.init)
    # states to be synchronized
    #sync_states=helper.cross_product(aut1.states,aut2.states)
    sync_states=help.cross_product(aut1.states,aut2.states)
    #sync_states=help.extract_elems_from_trans(sync_trans,'source').union(help.extract_elems_from_trans(sync_trans,'target'),{sync_init})
     # marked states, if no marked states in set --> all states are marked 
    if len(aut1.marked)==0:
        aut1.marked=aut1.states.copy() 
    if len(aut2.marked)==0:
        aut2.marked=aut2.states.copy()
    sync_marked=help.cross_product(aut1.marked,aut2.marked)
    sync_marked= sync_marked.intersection(sync_states) 
        
    # forbidden states, forbidden states according to lecture notes 
    sync_forbidden= help.cross_product(aut1.forbidden,aut2.states).union(help.cross_product(aut1.states,aut2.forbidden)) & sync_states
    
    reach_sync_states = reach(sync_events, sync_trans, {sync_init}, sync_forbidden)
    reach_sync_marked = sync_marked.intersection(reach_sync_states)
    reach_sync_states.update({sync_init})

    
    reach_trans=set()
    for element in sync_trans:
        if element.source.issubset(reach_sync_states) and element.target.issubset(reach_sync_states):
            reach_trans.update({element})
        
    return auto.Automaton(states=reach_sync_states,init=sync_init,events=sync_events,trans=reach_trans,forbidden= sync_forbidden , marked=reach_sync_marked)
    
    """
    Returns the synchronous composition of two automata.
    
    :param aut1: Automaton
    :param aut2: Automaton
    
    def trim_unreach(aut12):
        aut12.states = reach(aut12.events,aut12.trans,{aut12.init},set())
        aut12.forbidden &= aut12.states
        aut12.marked &= aut12.states
        aut12.trans = set(filter(lambda x: helper.extract_elems_from_trans({x},'source').issubset(aut12.states), aut12.trans))
        return aut12
    
    events12 = helper.extract_elems_from_trans(aut1.trans,'event') | helper.extract_elems_from_trans(aut2.trans,'event')
    trans12 = set()
    for ev in events12:
        aut1.trans |= {auto.Transition(st1, ev, st1) for st1 in aut1.states if ev not in aut1.events}
        aut2.trans |= {auto.Transition(st1, ev, st1) for st1 in aut2.states if ev not in aut2.events}
        for tr1 in helper.filter_trans_by_events( aut1.trans, {ev} ):
            for tr2 in helper.filter_trans_by_events( aut2.trans, {ev} ):
                origin = helper.merge_label( helper.extract_elems_from_trans({tr1},'source').pop(), helper.extract_elems_from_trans({tr2},'source').pop() )
                target = helper.merge_label( helper.extract_elems_from_trans({tr1},'target').pop(), helper.extract_elems_from_trans({tr2},'target').pop() )
                trans12.add( auto.Transition( origin, ev, target ) )
 
    init12      = helper.merge_label(aut1.init, aut2.init)
    states12    = helper.extract_elems_from_trans(trans12,'source') | helper.extract_elems_from_trans(trans12,'target') | {init12}
    forbidden12 = helper.cross_product(aut1.forbidden, aut2.states) | helper.cross_product(aut1.states, aut2.forbidden) & states12
    marked12    = helper.cross_product( aut1.marked if aut1.marked else aut1.states, aut2.marked if aut2.marked else aut2.states) & states12    
    return trim_unreach(auto.Automaton( states=states12, init=init12, events=events12, trans=trans12, forbidden=forbidden12, marked=marked12 ))
    
    """