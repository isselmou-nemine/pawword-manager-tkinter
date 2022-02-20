import random
class Code:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        self.password_list = []
        self.password_shuffle()

    def password_shuffle(self):
        password_letters = [random.choice(self.letters) for letter in range(random.randint(8, 10))]
        password_symbols = [random.choice(self.symbols) for symbol in range(random.randint(2, 4))]
        password_numbers = [random.choice(self.numbers) for number in range(random.randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        random.shuffle(password_list)

        return  password_list



