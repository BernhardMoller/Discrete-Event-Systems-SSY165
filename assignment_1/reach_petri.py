# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:10:37 2018

@author: Fredrik Möller
"""
 
import synch1_1 as synch
import Automaton as auto


p1 = auto.Automaton(states={'p11', 'p12'},
               init='p11',
               events={'a','b'},
               trans={auto.Transition('p11', 'a', 'p12'),
                      auto.Transition('p12', 'b', 'p11')},
               marked={})

p2 = auto.Automaton(states={'p21', 'p22'},
               init='p21',
               events={'e','d','c'},
               trans={auto.Transition('p22', 'd', 'p21'),
                      auto.Transition('p22', 'e', 'p21'),
                      auto.Transition('p21', 'c', 'p22')},
               marked={})

sp1 = auto.Automaton(states={'sp11', 'sp12'},
               init='sp11',
               events={'c','b'},
               trans={auto.Transition('sp11', 'b', 'sp12'),
                      auto.Transition('sp12', 'c', 'sp11')},
               marked={'sp11'})

sp2 = auto.Automaton(states={'sp21', 'sp22'},
               init='sp21',
               events={'d','c'},
               trans={auto.Transition('sp22', 'd', 'sp21'),
                      auto.Transition('sp21', 'c', 'sp22')},
               marked={'sp21'})


print(p1.states, p1.events, p1.trans)


p1p2 = synch.synch(p1,p2)
print('synch')
print(p1.states, p1.events, p1.trans)
sp1sp2 = synch.synch(sp1,sp2)

tot = synch.synch(p1p2,sp1sp2)











#
# reachable_states = (start_states.difference(forbidden)).copy() # Copy init-states excluding the forbidden states
#     
#    print('rs', reachable_states)
#    if trans == set():
#        print(reachable_states)
#        return reachable_states # If no transitions remain return the set of reachable states
#     
#        trans_w_reach = helper.filter_trans_by_source(trans, reachable_states)
#     
#    if trans_w_reach == set():
#        print('no source')
#        return reachable_states
#         
#     
#    cur_trans = trans_w_reach.pop()
#    print('ct', cur_trans, 'forbidden source', cur_trans.source in forbidden, 'forbidden target', cur_trans.target in forbidden)
#     
#    if (cur_trans.source in forbidden) or (cur_trans.target in forbidden):
#        trans.discard(cur_trans)
#        print('forbidden')
#        return reach(events, trans, reachable_states, forbidden)
#         
#    if (cur_trans.event in events):
#        print('adding', cur_trans.target)
#        reachable_states.add(cur_trans.target)
#        trans.discard(cur_trans)
#        return reach(events, trans, reachable_states, forbidden)
#    else:
#        trans.discard(cur_trans)
#        print('else')
#        return reach(events, trans, reachable_states, forbidden)







