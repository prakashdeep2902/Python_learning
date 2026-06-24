class Train:
    def __init__(self, SheetAvl, fare):
        self.SheetAvl = SheetAvl
        self.fare = fare

    def getUpdate(self):
        status = {"sheet_available": self.SheetAvl, "Train_Fare": self.fare}
        return status

    def BookTicket(self):
        if self.SheetAvl <= 0:
            return "Ticket are not available"
        else:
            self.BookTicket = self.SheetAvl - 1
            return f"Ticket booked now Ticket Available {self.BookTicket}"


Railway = Train(400, 2500)

print(Railway.getUpdate())
print(Railway.BookTicket())
