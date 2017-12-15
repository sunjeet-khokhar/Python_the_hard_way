def universe_age():
    while True:
        try:
            age = int(input("Type in the age of the universe in years"))
            if (age <= 0):
                print("Please enter a non-negative integer")
                universe_age()
            else:
                print(age)
                break
        except ValueError:
            print("Please enter a numeric value")
        except: # a blanket catch all to handle what might not e handled by exisitng handlers 
            print("Some weird has happened here")
        finally: # this will always be executed
            print("this will always get executed")
            
universe_age()
