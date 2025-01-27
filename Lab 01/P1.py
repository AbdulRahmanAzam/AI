# Reflex agent (vacuum cleaner)

class Environment:
    def __init__(self, state = "Dirty"):
        self.state = state
        
    def get_percept(self):
        return self.state
        
    def clean_room(self):
        self.state = "Clean"
        
class SimpleReflexAgent:
    def __init__(self):
        pass
    
    def act(self, percept):
        if percept == "Dirty":
            return "Clean the room"
        else:
            return "Room is Already Cleaned"
            
def run_agent( agent, environment, steps):
    for steps in range(steps):
        percept = environment.get_percept()
        act = agent.act(percept)
        print(f"Step: {steps + 1}, Percept: {percept}, Act: {act}")
        
        if percept == "Dirty":
            environment.clean_room()
            
            
            
agent = SimpleReflexAgent()
environment = Environment()

run_agent(agent, environment, 10)
