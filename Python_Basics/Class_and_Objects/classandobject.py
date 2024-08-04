class Human:
    def __init__(self, n, o):
        #  properties
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "Cricketer":
            print(f"{self.name} plays Cricket")

        elif self.occupation == "Singer":
            print(f"{self.name} sings really well")

    def speaks(self):
        print(f"{self.name} says hello to you")

Virat = Human("Virat Kohli","Cricketer")
Virat.do_work()
Virat.speaks()

Arijit = Human("Arijit Singh", "Singer")
Arijit.do_work()
Arijit.speaks()