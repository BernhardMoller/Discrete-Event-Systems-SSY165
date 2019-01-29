# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:24:03 2018

@author: Fredrik Möller
"""
import helper as help

def reach_1(events, trans, start_states, forbidden):

    start_states=start_states.difference(forbidden)
    Q_old=start_states.copy()
    Q_new=set()
    Q_plus=set()
    
    while Q_old !=Q_new:
        Q_old=Q_old.union(Q_plus).difference(forbidden)
        Q_plus=set()
        
        Q_plus= help.extract_elems_from_trans(help.filter_trans_by_source(help.filter_trans_by_events(trans,events),Q_old,'target')
        
        Q_new = Q_old.union(Q_plus).difference(forbidden)
        
        reach_states=Q_new.copy()
        
    return reach_states 

reach_tot1=reach_1(tot.events,tot.trans,{tot.init},tot.forbidden)

