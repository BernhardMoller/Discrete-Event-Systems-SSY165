# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:05:17 2018

@author: Fredrik Möller
"""

def trim(aut12):
        aut12.states = reach(aut12.events,aut12.trans,{aut12.init},aut12.forbidden)
        aut12.forbidden &= aut12.states
        aut12.marked &= aut12.states
        aut12.trans = set(filter( lambda x: extract_elems_from_trans({x},'source').issubset(aut12.states), aut12.trans ))
        return aut12

    events12 = extract_elems_from_trans(aut1.trans,'event') | extract_elems_from_trans(aut2.trans,'event')
    trans12 = set()        
    for ev in events12:
        if ev not in aut1.events:
            aut1.trans = aut1.trans | {Transition(st1, ev, st1) for st1 in aut1.states }
        if ev not in aut2.events:
            aut2.trans = aut2.trans | {Transition(st2, ev, st2) for st2 in aut2.states }
        for tr1 in filter_trans_by_events( aut1.trans, {ev} ):
            for tr2 in filter_trans_by_events( aut2.trans, {ev} ):
                origin = merge_label( extract_elems_from_trans({tr1},'source').pop(), extract_elems_from_trans({tr2},'source').pop() )
                target = merge_label( extract_elems_from_trans({tr1},'target').pop(), extract_elems_from_trans({tr2},'target').pop() )
                trans12.add( Transition( origin, ev, target ) )
 
    init12      = merge_label(aut1.init, aut2.init)
    states12    = extract_elems_from_trans(trans12,'source') | extract_elems_from_trans(trans12,'target') | {init12}
    forbidden12 = cross_product(aut1.forbidden, aut2.states) | cross_product(aut1.states, aut2.forbidden) & states12
    marked12    = cross_product( aut1.marked if aut1.marked else aut1.states, aut2.marked if aut2.marked else aut2.states) & states12    
    return trim(Automaton( states=states12, init=init12, events=events12, trans=trans12, forbidden=forbidden12, marked=marked12 ))



a1 = Automaton(states={1, 2},
               init=1,
               events={'a', 'b'},
               trans={Transition(1, 'a', 2)},
               marked={2})
a2 = Automaton(states={3, 4},
               init=3,
               events={'b'},
               trans={Transition(3, 'b', 4)})
a1a2 = synch(a1, a2)

print(a1a2