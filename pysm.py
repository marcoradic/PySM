"""
Finite State Machine implementation using pure Python 3
"""

class TransitionNotPossibleException(Exception):
    pass


class FSM(object):
    """
    Represents a Finite State Machine which can can characterized as a 5-tuple

    M = (S, Sigma, delta, z_0, E)

    - S: States
    - Sigma: Alphabet
    - delta: transition function
    - z_0: start state
    - E: set of terminal states
    """


    def __init__(self, states, start_state, terminal_states):
        """
        Arguments:
            states {dict} -- dictionary containing all states and transitions
            start_state {str} -- single start state
            terminal_states {str} -- set of terminal states
        """

        self.states = states # states, transition-function and transitions all in one
        self.start_state = start_state
        self.terminal_states = terminal_states
        self.current_state = self.start_state
        self.state_history = [self.current] # store old states
        self.transition_history = []
        #self._validate() TODO validate the FSM


    def _validate(self,):
        raise NotImplementedError
    
    def step(self, transition):
        if self.can(transition):
            possible_transitions = self.states.get(self.current)
            # we choose the first transition we can make
            for possible_transition in possible_transitions:
                if possible_transition[0] == transition:
                    self.state_history.append(possible_transition[1])
                    self.transition_history.append(possible_transition[0])
                    self.current_state = possible_transition[1]
                    return self.current
        else:
            raise TransitionNotPossibleException
        return None

    def can(self, transition):
        possible_transitions = self.states.get(self.current)
        return bool(len([x[0] for x in possible_transitions if x[0] == transition]))

    def can_terminate(self,):
        return self.current in self.terminal_states
    
    @property
    def current(self,):
        return self.current_state

    def history(self,):
        return 'FSM History:\tStates visited: {} Transitions made: {}'.format(self.state_history, self.transition_history)

def test():
    states = {
        'q0' : {('a', 'q1'), ('b', 'q1')},
        'q1' : {('a', 'q1')}
    }
    fsm = FSM(states, 'q0', {'q1'})
    print(fsm.can('a'))
    print(fsm.can('c'))
    print(fsm.can_terminate())
    print(fsm.step('a'))
    print(fsm.current)
    print(fsm.can_terminate())
    print(fsm.history())

if __name__ == '__main__':
    test()