class Star:
    def __init__(self,name,constellation):
        self.name = name
        self.constellation = constellation
    def print_name(self):
        print("The name of this star is {self.name} ")  
    def constellation(self):
        Print(f"The start {self.name} belongs to the {self.constellation} constellation")
def main():
    newly_discovered_star = Star('silver_wolf','orion')
    newly_discovered_star.print_name()
    newly_discovered_start.constellation()
if __name__ == '__main__':
    main()



