Notes = [500, 200, 50]


class task:
    # notes=[500,200,50]
    def __init__(self, notes):
        self.notes = notes

    def withdraw_amount(self, amount):
        if amount % 50 != 0:
            print("Enter valid amount (multiple of 50)")
        else:
            notes_count = {}
            for note in self.notes:
                if amount >= note:
                    count = amount // note
                    notes_count[note] = count
                    amount -= note * count

            for i, j in notes_count.items():
                print(f"{i} notes : {j}")


atm = task(Notes)

while True:
    withdraw_amt = int(input("Please enter amount to be withdraw --> "))
    atm.withdraw_amount(withdraw_amt)
    choose = input("Enter (c) to continue or (x) to exit --> ").lower()
    if choose != 'c':
        break
