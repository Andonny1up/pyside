class Madre:
    def __init__(self):
        print("Soy Madre")

class Padre:
    def __init__(self):
        print("Soy padre")

class Hijo(Madre, Padre):
    def __init__(self):
        Madre.__init__(self)
        Padre.__init__(self)
        print("soy hijo")


hijo = Hijo()