import random

class Agent: 
    def __init__(self, grid_width, grid_height):
        self.x = random.randint(1, grid_width)
        self.y = random.randint(1, grid_height)

    
    def move(self, grid_width, grid_height):
        new_x = random.randint(1, grid_width)
        new_y = random.randint(1, grid_height)

        self.x = new_x
        self.y = new_y 

grid_width = 10
grid_height = 10 

agents = [Agent(grid_width, grid_height), Agent(grid_width, grid_height), Agent(grid_width, grid_height)]

num_steps = 100

for step in range(num_steps): 
    for agent in agents:
        agent.move(grid_width, grid_height)

for i, agent in enumerate(agents): 
    print(f"Agent {i + 1}'s final position: ({agent.x}, {agent.y})")
