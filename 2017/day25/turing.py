"""Contains a Turing machine class, and not much else."""

class Turing:
    "Represents a Turing machine."
    def __init__(self, start, states):
        """Creates a Turing machine.

        Creates a Turing machine with the given starting state and state transitions.
        States should look like this:
        {
            'State1': [
                {'write': value_to_write, 'move': <1 or -1>, 'next': next_state},
                {'write': value_to_write, 'move': <1 or -1>, 'next': next_state}
            ],
            'State2': [...],
            ...
        }

        Arguments:
            start {str} -- The Turing Machine's starting state.
            steps {int} -- Number of steps to run
            states {dict} -- State transitions

        """
        self.current = start
        self.states = states
        self.cursor = 0
        self.tape = {}

    def run(self):
        """Runs the Turing Maching for one step."""
        value = self.tape.get(self.cursor, 0)
        state = self.states[self.current][value]
        self.tape[self.cursor] = state['write'] # write to the tape
        self.cursor += state['move']            # move the cursor
        self.current = state['next']            # go to next state

    def checksum(self):
        "Returns the number of ones on the tape."
        return sum(self.tape.values())
