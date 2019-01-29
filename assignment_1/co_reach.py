# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:08:20 2018

@author: Fredrik Möller
"""
import Reach
import helper
#def coreach(events, trans, marked, forbidden):
    # returns backwards reachable states 
    

    coreach= Reach.reach( events, helper.flip_trans(trans), marked, forbidden)
    return coreach(events, trans, marked, forbidden)  





