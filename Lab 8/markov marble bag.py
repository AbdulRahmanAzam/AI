# Markov Model Example: The Marble Bag Problem

import numpy as np

states = ['red', "blue"]
transition_matrix = np.array([
    [0.5,0.5],
    [0.5,0.5]
])

def simulate_markov_chain(initial_state, transition_matrix, num_steps):
    current_state = initial_state
    state_sequence = [current_state]

    for _ in range(num_steps):
        if current_state == 'red':
            next_state = np.random.choice(states, p=transition_matrix[0])
        else:
            next_state = np.random.choice(states, p=transition_matrix[1])

        state_sequence.append(next_state)
        current_state = next_state

    return state_sequence

initial_state = 'red'
num_steps = 10

state_sequence = simulate_markov_chain(initial_state, transition_matrix, num_steps)
print(f"Simulated state sequence: " + " -> ".join(state_sequence))


