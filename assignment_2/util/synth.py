# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 08:53:30 2018

@author: Fredrik Möller
"""
"""
 Generates a nonblocking and controllable supervisor for the synchronized system P||Sp.
    
    :param P: automaton of the plant
    :param Sp: automaton of the specification
    :param sigma_u: set of uncontrollable events
    """
import ass1 as a1
import helper_functions as help
import Automaton as auto 

def supervisor(P, Sp, sigma_u):

    
    S0 = a1.synch(P,Sp)
    S0_states = S0.states.copy()
    S0_events = S0.events.copy()
    S0_trans = S0.trans.copy()
    S0_mark = S0.marked.copy()
    S0_forb = S0.forbidden.copy()
    
    prev_unsafe = S0_forb
    unsafe = set()
    flag = True
    
    while flag:
        prev_unsafe = unsafe
        Q_prim = a1.coreach(S0_events, S0_trans, S0_mark, prev_unsafe)
        Q_bis = a1.coreach(sigma_u, S0_trans, (S0_states - Q_prim), set())
        unsafe = prev_unsafe | Q_bis # Union
        
        if unsafe == prev_unsafe:
            flag = False
    
    S_states = S0_states - unsafe
    
    if S_states == set(): # There exist no supervisor that can fulfill the specification
        raise ValueError
    
    S_state= S_states.copy()
    for k in S_states:
        if help.is_defined_for_p(P.trans, k, sigma_u) or help.is_defined_for_q(Sp.trans, k, sigma_u):
            S_state.discard(k)
                   
    S_trans = help.filter_trans_by_target(S0_trans, S_state)
    S_trans2 = help.filter_trans_by_source(S_trans, S_state)
    
    S = auto.Automaton(S_state, S0.init, S0_events ,S_trans2)
    
    return S



    S0 = a1.synch(P,Sp)
    S0_states = S0.states.copy()
    S0_events = S0.events.copy()
    S0_trans = S0.trans.copy()
    S0_mark = S0.marked.copy()
    S0_forb = S0.forbidden.copy()
    

