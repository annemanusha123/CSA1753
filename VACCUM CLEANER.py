def vacuum(state, pos):
    for room in state:
        if state[room] == 'Dirty':
            print(f"Cleaned {room}")
            state[room] = 'Clean'
    print("Final State:", state)

# Input
rooms = {'A':'Dirty', 'B':'Dirty'}
start_pos = 'A'

# Run
vacuum(rooms, start_pos)
