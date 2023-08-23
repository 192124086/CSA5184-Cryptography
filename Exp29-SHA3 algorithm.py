import random

STATE_SIZE = 25
CAPACITY_LANES = 16
LANE_SIZE = 64

class InternalState:
    def __init__(self):
        self.state = [0] * STATE_SIZE

def initialize_state(state):
    for i in range(STATE_SIZE):
        state.state[i] = 0

def all_capacity_lanes_nonzero(state):
    for i in range(CAPACITY_LANES):
        if state.state[i] == 0:
            return False
    return True

def main():
    state = InternalState()
    initialize_state(state)

    random.seed()

    steps = 0
    while not all_capacity_lanes_nonzero(state):
        lane_to_update = random.randint(0, CAPACITY_LANES - 1)
        bit_position = random.randint(0, LANE_SIZE - 1)

        state.state[lane_to_update] |= 1 << bit_position

        steps += 1

    print(f"All capacity lanes have at least one nonzero bit after {steps} steps.")

if __name__ == "__main__":
    main()
