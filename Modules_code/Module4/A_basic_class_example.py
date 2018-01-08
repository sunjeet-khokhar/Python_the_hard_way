# We are defining a blueprint/class for a Shark , it has two attributes in the constructor (__init__) a) name b) color
# and two methods 
class Shark:
    
    def __init__(self,name,color):
        self.name = name
        self.color = color
        print(f"Congrats, you have a new pet shark, it goes by the name {self.name} ")    
    
    def does_it_swim(self):
        print("Sharks can not only swim but are torpedos in the sea!")
        
    def whats_the_color(self):
        if self.color == 'white':
            print("OMG.... you have a great white as a pet !!!! \n")
        else:
            print("Phew....lets relax you dont have a great white as a pet  \n")
                
            
def main():
    # here we are instantiating our class , note that the code under __init__ would be called here 
    phoebe = Shark('Pheobe','white')
    # calling the first method for the shark object 
    phoebe.does_it_swim()
    #calling another method
    phoebe.whats_the_color()

    # here is creating another with a name and a different color
    nathan = Shark('Nathan','bright orange')
    nathan.whats_the_color()
            
if __name__ == '__main__':
    main()
    

    

