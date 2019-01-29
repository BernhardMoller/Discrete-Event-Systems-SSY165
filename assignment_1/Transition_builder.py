# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:40:37 2018

@author: Fredrik Möller
"""
import helper
import Automaton as auto

# building the transitions from definitions (lectures)
sync_trans=set()
def sync_trans(aut1, aut2, syc_events):
    
    sync_events=helper.extract_elems_from_trans(aut1.trans,'event').union(helper.extract_elems_from_trans(aut2.trans,'event')) 
    sync_trans= set()
    for event in sync_events:
        if event not in aut1.events:
            for x in aut1.states:
                aut1.trans= aut1.trans | {auto.Transition(x , event,x)}
        if event not in aut2.events:
            for x in aut2.states:
                aut2.trans= aut2.trans | {auto.Transition(x , event,x)}
        for transition1 in auto.filter_trans_by_events( aut1.trans, {event} ):
            for transition2 in auto.filter_trans_by_events( aut2.trans, {event} ):
                source = merge_label( helper.extract_elems_from_trans({transition1},'source').pop(), helper.extract_elems_from_trans({tr2},'source').pop() )
                target = merge_label( helper.extract_elems_from_trans({transition1},'target').pop(), helper.extract_elems_from_trans({tr2},'target').pop() )
                sync_trans.add( auto.Transition( source, event, target ) )
                
                    
    return sync_trans