"""lets create a introduction letter using oops concepts

"""

class Letter:
    def __init__(self, name, goal, role, crew, reqbounty,reqpower, haki , df):
        self.name = name
        self.goal = goal
        self.role = role
        self.crew = crew
        self.reqbounty = reqbounty
        self.reqpower = reqpower
        self.haki = haki
        self.df = df

    def matter(self):
        print (f"greetings \n my name is {self.name} \n im gonna be {self.goal} and im the {self.role} in the {self.crew} pirates crew "
              f"i am recruting a pirate u need basic qualifications  first your bounty should be {self.reqbounty} +"
              f"and in terms of power you should have  {self.reqpower} and "
              f"you should  have atleast {self.haki} and {self.df} \n thank you ---{self.name} ")

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))


lname = "Monkey D Luffy "
lgoal = "the king of pirates"
lrole = "captain"
lcrew = " strawhats "
lreqbounty =0
lreqpower ="no power"
lhaki = "no haki"
ldf="no devil fruit"

kname = "eustuss D captain Kid"
kgoal = "king of pirates"
krole ="captain "
kcrew = "kid"
kreqbounty =3000000
kreqpower = "capacity to take out 5 vice admirals alone"
khaki = "armement haki "
kdf ="you should be atlest logia df user"

laname ="Trafalugar D water LAW"
lagoal ="strong pirate "
larole ="captain"
lacrew ="heart "
lareqbounty =2450000
lareqpower ="you should be able to support team "
lahaki ="any one of the haki"
ladf ="you dont need any devil fruit "

luffy = Letter(lname,lgoal,lrole,lcrew,lreqbounty,lreqpower,lhaki,ldf)
print(luffy.matter(),"\n")
kid = Letter(kname, kgoal, krole, kcrew, kreqbounty, kreqpower, khaki, kdf)
print(kid.matter(),"\n")
law =Letter(laname, lagoal,larole,lacrew, lareqbounty, lareqpower, lahaki, ladf)
print(law.matter(),"\n")
shanks =Letter.from_dash(" akagami no shanks - taking one piece - captain - red hair - 500000000 - loyal- atlest two hakis - no devil fruit " )
print(shanks.matter())