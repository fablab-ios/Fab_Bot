
class Ticket:
    def __init__(self, name: str, number: int, email_address: str, status: str, date: str, time: str):
        self.name = name
        self.number = number
        self.email_address = email_address
        self.status = status
        self.date = date
        self.time = time

        self.status_rank = -1
        if self.status == "Created":
            self.status_rank = 1
        elif self.status == "Waiting on client input":
            self.status_rank = 2
        elif self.status == "Ready for pickup":
            self.status_rank = 3
        elif self.status == "Closed":
            self.status_rank = 4

    def __str__(self) -> str:
        return self.name + ", " + \
               str(self.number) + ", " + \
               self.email_address + ", " + \
               self.status + ", " + \
               self.date + ", " + \
               self.time
