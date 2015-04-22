class Egg:
    def __init__(self, kind = 'frimmed'):
        self.kind = kind
        
    def whatkind(self):
        return self.kind
        
def main():
    ried = Egg()
    scrambled = Egg('scambled')
    print(ried.whatkind())

if __name__ == "__main__": main()