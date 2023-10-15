w1 = 'aa'

class FiniteAutomata:
    def __init__(self, transitions, start_state, final_states):
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def accepts(self, w0):
        w = w0 + w1
        state = self.start_state

        for symbol in w:
            if (state, symbol) in self.transitions:
                state = self.transitions[(state, symbol)]
            else:
                return False

        return state in self.final_states


def read_automaton(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    start_state = lines[1].strip()
    final_states = set(lines[2].split()[1:])

    transitions = {}
    for line in lines[3:]:
        state, symbol, next_state = line.strip().split()
        transitions[(state, symbol)] = next_state

    return FiniteAutomata(transitions, start_state, final_states)


def main():
    finite_automata = read_automaton('text.txt')
    print(finite_automata.accepts('cca'))
    # print(finite_automata.accepts('aab'))


if __name__ == '__main__':
    main()
