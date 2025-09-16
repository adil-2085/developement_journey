class Superhero:

    universe_name:str

    name:str

    powers:str


    def set_superhero(self,universe_name,name,powers):

        self.universe_name = universe_name

        self.name = name

        self.powers = powers

    def display_superheros(self):

        print(self.universe_name,self.name,self.powers)


batman_instance = Superhero()

batman_instance.set_superhero('DC','Batman','rich,driving skill')

batman_instance.display_superheros()

minnal_murali_instance = Superhero()

minnal_murali_instance.set_superhero('Basil universe','Minnal murali','strength,fly,run')

minnal_murali_instance.display_superheros()