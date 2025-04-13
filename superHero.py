class Superhero:
    def __init__(self, name, secret_identity, powers, weakness, origin_story):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # This should be a list
        self.weakness = weakness
        self.origin_story = origin_story
        self.energy_level = 100
        
    def use_power(self, power_index):
        if power_index < len(self.powers):
            power = self.powers[power_index]
            print(f"{self.name} uses {power}!")
            self.energy_level -= 10
        else:
            print("Power not available!")
            
    def rest(self):
        print(f"{self.name} takes a well-deserved rest.")
        self.energy_level = min(100, self.energy_level + 30)
        
    def describe(self):
        print(f"Superhero: {self.name}")
        print(f"Secret Identity: {self.secret_identity}")
        print("Powers:")
        for power in self.powers:
            print(f"- {power}")
        print(f"Weakness: {self.weakness}")
        print(f"Current Energy: {self.energy_level}%")
        
    def encounter_weakness(self):
        print(f"Oh no! {self.name} encounters {self.weakness}!")
        self.energy_level -= 30
        if self.energy_level <= 0:
            print(f"{self.name} is defeated!")
        else:
            print(f"{self.name} struggles but continues to fight!")

# Inheritance example
class CosmicHero(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, origin_story, home_planet):
        super().__init__(name, secret_identity, powers, weakness, origin_story)
        self.home_planet = home_planet
        self.cosmic_energy = 200  # Cosmic heroes have more energy
        
    def use_power(self, power_index):
        if power_index < len(self.powers):
            power = self.powers[power_index]
            print(f"{self.name} channels cosmic energy to use {power}! 🌌")
            self.cosmic_energy -= 15
        else:
            print("Power not available!")
            
    def describe(self):
        super().describe()
        print(f"Home Planet: {self.home_planet}")
        print(f"Cosmic Energy: {self.cosmic_energy}")

# Example usage
if __name__ == "__main__":
    spider_man = Superhero(
        name="Spider-Man",
        secret_identity="Peter Parker",
        powers=["Web-slinging", "Spider-sense", "Wall-crawling"],
        weakness="Ethyl chloride (anti-venom)",
        origin_story="Bitten by a radioactive spider"
    )
    
    silver_surfer = CosmicHero(
        name="Silver Surfer",
        secret_identity="Norrin Radd",
        powers=["Cosmic Power", "Space Travel", "Energy Manipulation"],
        weakness="Galactus' will",
        origin_story="Chosen to be Galactus' herald",
        home_planet="Zenn-La"
    )
    
    spider_man.describe()
    spider_man.use_power(0)
    spider_man.encounter_weakness()
    
    print("\n")
    
    silver_surfer.describe()
    silver_surfer.use_power(1)