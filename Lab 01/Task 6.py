import numpy as np

class Environment:
    def __init__(self):
        self.path = [chr(65+i) for i in range(9)]
        
        self.path_states = {
            "A": 'safe',
            "B": 'safe',
            "C": 'fire',
            "D": 'safe',
            'E': 'fire',
            'F': 'safe',
            'G': 'safe',
            "H": 'safe',
            'I': 'fire'
        }
        
        self.grid = np.array([f"{key}: {self.path_states[key]}" for key in self.path]).reshape(3,3)
        
        print(grid)
        
    # def display(self):
        
        
        
        
        
        
e = Environment()

