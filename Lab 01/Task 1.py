import random

class Environment:
    def __init__(self):
        self.components = {
            'A': random.choice(['safe', 'vulnerable']),
            'B':random.choice(['safe', 'vulnerable']),
            'C':random.choice(['safe', 'vulnerable']),
            'D':random.choice(['safe', 'vulnerable']),
            'E':random.choice(['safe', 'vulnerable']),
            'F':random.choice(['safe', 'vulnerable']),
            'G':random.choice(['safe', 'vulnerable']),
            'H':random.choice(['safe', 'vulnerable']),
            'I':random.choice(['safe', 'vulnerable'])
        }

    def display(self):
        print("The current system")

        for component, status in self.components.items():
            print(f"Component: {component}: {status}")

        print("\n")

class SecurityAgent:
    def __init__(self):
        self.vulnerabilites = []

    def scan(self, components):

        for component, status in components.items():
            if status == 'vulnerable':
                self.vulnerabilites.append(component)
                print(f"Warning COmponent {component} is vulnerable")
            else:
                print(f"Success, COmponent : {component} is secured")

        print("\n")
    
    def patch(self, components):
        for comp in self.vulnerabilites:
            components[comp] = "safe"
            print(f"Component: {comp} have been patched")

        print("\n")

    def check(self, components):
        if all(status == 'safe' for status in components.values()):
            print("All components are secured")
        else:
            print("Some components are still vulnerable")



env = Environment()
comp = env.components

env.display()

sec = SecurityAgent()
sec.scan(comp)
sec.patch(comp)
sec.check(comp)




