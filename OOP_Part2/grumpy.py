class GrumpyDict(dict):
    def __repr__(self):
        print("None of your business!")
        return super().__repr__()

    def __missing__(self, key):
        print(f"You want {key}?! Welp! It ain't here!") 

    def __setitem__(self, key, value):
        print("YOU WANNA CHANGE THE DICTIONARY NOW?!")
        print("FINE, FOOL!")
        super().__setitem__(key, value)


data = GrumpyDict({"first": "Thomas", "last": "cat"})
print(data)
data['city'] = "Tokyo"
print(data)