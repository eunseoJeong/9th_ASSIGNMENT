class clothes:
    def __init__(self, hat, top, bottom):
        self.hat = hat
        self.top = top
        self.bottom = bottom
    def school(self):
        print("아무거나 입어")
    def input(self):
        input("별로야 ? ")
    
today = clothes("볼캡","흰티","청바지")
today.school()
print(today.hat, today.top, today.bottom)
today.input()