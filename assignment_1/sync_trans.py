# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 16:51:55 2018

@author: Fredrik Möller
"""
from test_sync import *
import self_loop
def sync_trans(aut1,aut2): 

    Events_1= aut1.events.intersection(aut2.events)
    Events_2= aut1.events.difference(aut2.events)
    Events_3= aut2.events.difference(aut1.events)
    
    union_events= aut1.events.union(aut2.events)
    
    #add the self loops to the transitions 
    #aut1= self_loop.(aut1, Events_3)
    
    
    return sync_trans(aut1,aut2)




