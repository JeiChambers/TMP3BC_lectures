class Robot:
    def __init__(self, name, battery=100, skills=[]):
        self.name = name        
        self.battery = battery
        self.skills = skills

    def charge(self):
        self.battery = 100
        return self
    
    def say_name(self):
        if self.battery > 0:
            self.battery -= 1
            return f"I herald the destruction of the Avengers! I'm {self.name.upper()}"
        return "Low Power. Please charge and try again."

    def learn_skill(self, new_skill, cost_to_learn):
        if self.battery >= cost_to_learn:
            self.battery -= cost_to_learn
            self.skills.append(new_skill)
            return f"Woot! I know {new_skill.upper()}"  
        return "Insufficient Battery. Please charge the battery and try again." 