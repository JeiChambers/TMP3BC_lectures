class Pet:

    allowed = ['cat', 'dog', 'fish', 'ferret']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Korra", "dog")

