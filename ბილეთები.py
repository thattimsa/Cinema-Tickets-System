class Ticket:  # 1-ლი კრიტერიუმი

    def __init__(self, Title, Cost, Quantity, Language = "Geo", Date = "მალე", Time = "ამ ეტაპზე უცნობია"):
        self.Title = Title
        self.Cost = Cost
        self.Quantity = Quantity
        self.Language = Language
        self.Date = Date   # დავამატე თარიღი და დრო, ვფიქრობ, არ იქნება ცუდი :)
        self.Time = Time

    def __str__(self):  # მე-2 კრიტერიუმი
        return "დასახელება - " + self.Title + \
               "\nფასი - " + str(self.Cost) + " ლარი" + \
               "\nხელმისაწვდომობა - " + str(self.Quantity) + " ბილეთი" + \
               "\nსეანსის ენა - " + self.Language + \
               "\nთარიღი - " + self.Date + \
               "\nდრო - " + self.Time + " საათი" + "\n"


    def __lt__(self, other):   # მე-7 კრიტერიუმი
        if isinstance(other, Ticket):
            return self.Quantity < other.Quantity
        return self.Quantity < other

    def __gt__(self, other):
        if isinstance(other, Ticket):
            return self.Quantity > other.Quantity
        return self.Quantity > other

    def __eq__(self, other):
        if isinstance(other, Ticket):
            return self.Quantity == other.Quantity
        return self.Quantity == other

class User:   # მე-3 კრიტერიუმი

    # ინიციალიზაცია
    def __init__(self, user):
        self.User = user
        self.Balance = 0

    def __str__(self):   # მე-4 კრიტერიუმი
        return "მომხმარებელი - " + self.User + \
               "\nხელმისაწვდომი ბალანსი - " + str(self.Balance) + " ლარი\n"


    def Booking(self, ticket, quantity):   # მე-5 კრიტერიუმი
        possible = True
        if ticket.Quantity < quantity:
            possible = False
            print("ბილეთების აღნიშნული რაოდენომა ამჟამად მიუწვდომელია")

        if ticket.Cost*quantity > self.Balance:
            possible = False
            print("თქვენს ბალანსზე არსებული თანხა არ არის საკმარისი ტრანზაქციის განსახორციელებლად")

        if possible == True:
            self.Balance = self.Balance - ticket.Cost*quantity
            print("--- შესყიდვა ---", "\nშესყიდულია", quantity, "ბილეთი", "\nტრანზაქცია წარმატებით დასრულდა",
                  "\nბალანსზე დარჩენილი თანხა - ", self.Balance, " ლარი\n")
            ticket.Quantity = ticket.Quantity - quantity

    def Deposit(self, balance):   # მე-6 კრიტერიუმი
        self.Balance = self.Balance + balance

# მე-8 კრიტერიუმი

# ფილმების ჩამონათვალი და მათი პარამეტრები
film_1 = Ticket(Title='ზოოსტარი 2 | Sing 2', Cost=5, Quantity=50, Language="Eng", Date="28 მარტი", Time="19:30")
film_2 = Ticket(Title='კივილი 5 | Scream 5', Cost=6, Quantity=40, Date="5 აპრილი", Time="18:00") # აქ არ მივუთითე ენა (დეფოლტი)
film_3 = Ticket(Title='ბეტმენი | The Batman', Cost=7, Quantity=30, Date="8 აპრილი", Time="16:30")
film_4 = Ticket(Title='კოშმარების ხეივანი | Nightmare Alley', Cost=8, Quantity=20, Date="12 აპრილი", Time="17:30")
film_5 = Ticket(Title='კინგსმენი | Kingsman', Cost=9, Quantity=10) # აქ არც ენა, არც თარიღი და არც დრო მივუთითე (დეფოლტი)


# მომხმარებელის ანგარიში
# დავუშვათ, ჩემი ანგარიში :)
user = User(user="Tim Sarkisiani")
user.Deposit(balance=250)



print("\n-*- კინოთეატრის ბილეთების გაყიდვა -*-\n", "\n^   აფიშა   ^\n")

# თანმიმდევრობით ვპრინტავთ ფილმებს, რომლებიც გადის ჩვენს კინოთეატრში
print("***| ფილმი #1 |***")
print(film_1)

print("***| ფილმი #2 |***")
print(film_2)

print("***| ფილმი #3 |***")
print(film_3)

print("***| ფილმი #4 |***")
print(film_4)

print("***| ფილმი #5 |***")
print(film_5)

# გამოაქვს მომხმარებლის სახელი და ბალანსი
print("# ავტორიზებული მომხმარებელი #")
print(user)

# დავუშვათ, რომ მომხმარებელი ყიდულობს მესამე ფილმის ("ბეტმენის") რვა ბილეთს
user.Booking(film_3, 8)

# ბილეთების მარაგი განახლდება, დაითვლება რაოდენობა (ამ შემთხვევაში 30-8=22 ბილეთი) და პასუხი დაიპრინტება
print("^^^ მარაგი ^^^")
print(film_3)

# მომხმარებლის ბალანსიც განახლდება (250-7*8=194 ლარი) და დაიპრინტება
print("# ავტორიზებული მომხმარებელი #")
print(user)








