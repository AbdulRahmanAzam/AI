import random


class Environment:
    def __init__(self):
        self.components = {}
        self.initialize_system()
    
    def initialize_system(self):
    
        for i in range(9):
            component = chr(65 + i)  # A through I
            status = random.choices(
                ['Safe', 'Low Risk', 'High Risk'],
                weights=[0.4, 0.4, 0.2],
                k=1
            )[0]
            self.components[component] = status
    
    def display_system_state(self, message="Current System State"):
        
        print(f"\n{message}:")
        print("-" * 30)
        for component, status in self.components.items():
            print(f"Component {component}: {status}")
        print("-" * 30)


class SecurityAgent:
    def __init__(self, environment):
        self.environment = environment
        self.premium_service_available = False
    
    def scan_system(self):
        
        print("\nScanning System Components:")
        print("-" * 30)
        for component, status in self.environment.components.items():
            if status == 'Safe':
                print(f"Component {component} is secure")
            else:
                print(f" Component {component} has {status} vulnerabilities")
        print("-" * 30)
    
    def patch_vulnerabilities(self):
        
        print("\nPatching Vulnerabilities:")
        print("-" * 30)
        for component, status in self.environment.components.items():
            if status == 'Low Risk':
                self.environment.components[component] = 'Safe'
                print(f" Patched Low Risk vulnerability in Component {component}")
            elif status == 'High Risk':
                if self.premium_service_available:
                    self.environment.components[component] = 'Safe'
                    print(f" Patched High Risk vulnerability in Component {component} using premium service")
                else:
                    print(f" High Risk vulnerability in Component {component} requires premium service")
        print("-" * 30)


env = Environment()

agent = SecurityAgent(env)

env.display_system_state("Initial System State")

agent.scan_system()    

agent.patch_vulnerabilities()

env.display_system_state("Final System State")

