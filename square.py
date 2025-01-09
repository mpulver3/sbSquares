#return dictionary of number bought, investment, % chance to get back investment, return after x iterations

'''
class number_of_squares:
    total_investment = 0
    probability = 0.0
    tot_return = 0

    def _init_(self, total_investment, probability, tot_return)


#created a dictionary with 100 entries, and no values
num_squares = {}
for i in range(0, 100):
    num_squares[i] = None

print(num_squares)

#create a list of the 3 items we wanted? 

for i in range(100):
'''

class Squares:
    def __init__(self, number):
        self.num_squares = number
        self.single_investment = self.num_squares * 20
        self.probability = round(((1 - (((100 - self.num_squares) / 100 ) ** 4)) * 100), 2)
 
square_options = {}
for i in range(100):
    square_options[i] = Squares(i)
    print(f"Invested ${(square_options[i]).single_investment}, the probability to win a single quarter is: {(square_options[i]).probability}%")



#print(f"{sq0.num_squares} squares, invested ${sq0.single_investment}, probability to win any 1 quarter: {sq0.probability}%")
#print(f"{sq1.num_squares} squares, invested ${sq1.single_investment}, probability to win any 1 quarter: {sq1.probability}%")



'''


class Squares:
    num_squares = 0  # class variable

    def __init__(self, number):
        self.num_squares = number  # instance variable

    @property
    def single_investment(self):
        return self.num_squares * 20

    @property
    def probability(self):
        return round(((1 - (((100 - self.num_squares) / 100) ** 4)) * 100), 2)

    single_return = 0  # Assuming this is constant and doesn't depend on num_squares

    def __str__(self):
        return f"{self.num_squares} squares, invested ${self.single_investment}, probability to win any 1 quarter: {self.probability}%"


sq0 = Squares(0)
sq1 = Squares(1)

print(f"{sq0}\n{sq1}")
'''