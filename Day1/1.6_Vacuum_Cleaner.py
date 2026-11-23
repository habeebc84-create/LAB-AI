"""Vacuum Cleaner Problem (CO3)

Simple reflex agent vacuum cleaner in a 2-room world (A, B).
"""

LOCATIONS = ["A", "B"]


def run(initial_state, steps=10):
    state = dict(initial_state["rooms"])
    agent = initial_state["agent"]
    history = []
    for _ in range(steps):
        status = state[agent]
        if status == "Dirty":
            action = "Suck"
            state[agent] = "Clean"
        else:
            action = "Move to " + ("B" if agent == "A" else "A")
            agent = "B" if agent == "A" else "A"
        history.append((agent, action, dict(state)))
    return history


if __name__ == "__main__":
    init = {"rooms": {"A": "Dirty", "B": "Dirty"}, "agent": "A"}
    hist = run(init, steps=6)
    for i, (loc, action, st) in enumerate(hist, 1):
        print(f"Step {i}: agent@{loc} action={action} rooms={st}")
