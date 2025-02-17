import random
class Environment:
    def __init__(self):
        self.vulnerabilities = ["Safe", "Low Risk Vulnerable", "High Risk Vulnerable"];

        self.component = {chr(65+i): random.choice(self.vulnerabilities) for i in range(9)};
        
        
    def display(self):
        for x, y in self.component.items():
            print(f"Component: {x}: {y}")
        

class SystemScan:
    def __init(self):
        pass;
        
    def scan(self, components):
        for x, y in components.items():
            if(y == "Safe"):
                print(f"The component {x} is logged in")
            else:
                print(f"The component {x} is:  {y}")
        
        
e = Environment()

e.display()
