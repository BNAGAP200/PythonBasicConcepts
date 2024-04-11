

class students:

    def schoolx(self, sub, sports):
        self.sub = sub
        self.sports = sports
        print(sub, sports)

    def schooly(self, sub, sports):
        self.sub = sub
        self.sports = sports
        print(sub, sports)
class teachers:
    def schoolx(self, sub , exp):
        self.sub =sub
        self.exp =exp
        print(sub,exp)

    def schooly(self, sub, exp):
        self.sub = sub
        self.exp = exp
        print(sub, exp)



s1 = students()
s1.schoolx('maths', 'Cricket')

s2 = students()
s2.schooly("english", 'football')

Teach1=teachers()
Teach1.schoolx("science",8)

Teach2=teachers()
Teach2.schooly("social",5)