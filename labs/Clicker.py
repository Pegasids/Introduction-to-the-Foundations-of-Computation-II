# implement HandHeldClicker
class HandHeldClicker:
    
    def __init__(self):
        self.clicker = []
    
    def push(self):
        self.clicker.append("i")
    
    def reset(self):
        self.clicker = []
    
    def get_count(self):
        return len(self.clicker)
        

clicker = HandHeldClicker()

#text interface
def main():
    print("Hand-Held Clicker starts.")
    action = input("Action:")
    while action in "pre":
        #push button
        if action == "p":
            clicker.push()
            print("Count:" + str(clicker.get_count()))
        #reset clicker
        elif action == "r":
            clicker.reset()
            print("Count:" + str(clicker.get_count()))
        #terminate cliker
        elif action == "e":
            print("Hand-Held Clicker ends.")
            break

        action = input("Action:")
    
if __name__ == "__main__":
    main()
