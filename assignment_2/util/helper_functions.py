from .datastructures import Transition


def filter_trans_by_source(trans, states_to_keep):
    """Returns a new set containing all transitions where the source is in states_to_keep"""
    return {t for t in trans if t.source in states_to_keep}


def filter_trans_by_events(trans, events_to_keep):
    """Returns a new set containing all transitions where the event is in events_to_keep"""
    return {t for t in trans if t.event in events_to_keep}


def filter_trans_by_target(trans, states_to_keep):
    """Returns a new set containing all transitions where the target is in states_to_keep"""
    return {t for t in trans if t.target in states_to_keep}


def extract_elems_from_trans(trans, field):
    """
    Returns a new set with just the elements in a field of all transitions.
    E.g. field='source' for all source states
    or field='event' or field='target'
    """
    return {getattr(t, field) for t in trans}


def flip_trans(trans):
    """ Flips the direction of the transitions in the set"""
    return {Transition(t.target, t.event, t.source) for t in trans}


def merge_label(label1, label2):
    """Creates a new label based on two labels"""
    return '{}.{}'.format(label1, label2)


def cross_product(setA, setB):
    """Computes the crossproduct of two sets"""
    return {merge_label(a, b) for b in setB for a in setA}

def is_defined_for_p(p_trans, merged_source, shared_sigma_u):
    """
    Boolean check whether there is an uncontrollable transition defined in P
    with the merged_source as start state.
    
    :param p_trans: Set of transitions in automaton P
    :param merged_source: String label of the merged state in P||Q
    :param shared_sigma_u: Set of uncontrollable events shared between P and Q.
    """
    validate_inputs(p_trans, merged_source, shared_sigma_u)
    uncontrollable_trans = filter_trans_by_events(p_trans, shared_sigma_u)
    u_trans_from_merged_source = {t for t in uncontrollable_trans 
                                  if merged_source.startswith(str(t.source))}
    return u_trans_from_merged_source != set()

def is_defined_for_q(q_trans, merged_source, shared_sigma_u):
    """
    Boolean check whether there is an uncontrollable transition defined in Q
    with the merged_source as start state.
    
    :param q_trans: Set of transitions in automaton Q
    :param merged_source: String label of the merged state in P||Q
    :param shared_sigma_u: Set of uncontrollable events shared between P and Q.
    """
    validate_inputs(q_trans, merged_source, shared_sigma_u)
    uncontrollable_trans = filter_trans_by_events(q_trans, shared_sigma_u)
    u_trans_from_merged_source = {t for t in uncontrollable_trans 
                                  if merged_source.endswith(str(t.source))}
    return u_trans_from_merged_source != set()