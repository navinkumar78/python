import date
class person:
    def _init_(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.data_of_birth=date_of_birth
    def calculate_age(self):
        today=date.today()
        age=today.year-self.date_of_birth.year
        if today<date(today.year,self.date_of_birth.month,self.date_of_birth.date):
            age-=1
        return age
    p1=person("naveen","india",date(2005,11,25))
    p2=person("kumar","usa",date(2000,12,11))
    print("person")
    print("name:",p1.name)
    print("country",p1.coutnry)
    print("c=dob",p1.date_of_birth)
    print("age:",p1.calculate_age())
