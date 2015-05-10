from database import Database
import sys
import json

class CLI:
    def __init__(self):
        self.cinema = Database("cinema.db")
        self.movie_ids = []
        self.movie_id = 0
        self.movie_date = []
        self.username = ""
        self.tickets = 0
        self.available = {}
        self.seats = []
        self.reservations = []
        self.spells = {
            "show_movies": self.show_movies,
            "make_reservation": self.make_reservation,
            "help": self.helper
        }
        self.moves = {
            "set_username": self.set_username,
            "set_tickets": self.set_tickets,
            "show_movies": self.show_movies
        }

        self.step1 = [
            "set_username",
            "set_tickets",
        ]

        self.massages = [
            "Choose name>",
            "Choose number of tickets>",
            "Choose a movie>",
        ]

    def set_username(self, info):
        self.username = info

    def set_tickets(self, info):
        self.tickets = int(info)


    def step_three(self):
        to_str = ""
        projection = input("Choose a projection>")
        while False:
            if self.available[projection] > self.tickets:
                break
            projection = input("Choose a projection>")
        self.seats = self.cinema.get_available_spots(projection)
        for number in range(0, 11):
            to_str += " ".join([seat for seat in self.seats[number]])
            to_str += "\n"
        print(to_str)

    def is_taken(self, row, col):
        if self.seats[row][col] != "X":
            return False
        else:
            return True

    def step_four(self):
        for ticket in range(1, int(self.tickets) + 1):
            while True:
                seat = input("Choose seat {}>".format(ticket))
                try:
                    row = int(seat[1])
                    col = int(seat[3])
                    row_in_range = row in range(1, 10)
                    col_in_range = col in range(1, 10)
                    if row_in_range and col_in_range and not self.is_taken(row, col):
                        self.seats[row][col] = "X"
                        self.reservations.append((row, col))
                        break
                    elif not self.is_taken(row, col):
                        print("Out of range")
                    else:
                        print("Seat is already taken")
                except:
                    print("Invalid input")

    def step_five(self):
        print("This is your reservation:")
        movie = self.cinema.get_movie(self.movie_id)
        print("Movie: {} {}".format(movie[0], movie[1]))



    def show_movies(self):
        print("Current movies:")
        for movie in self.cinema.show_movies():
            if movie[0] not in self.movie_ids:
                self.movie_ids.append(movie[0])
            print("[{}] - {} ({})".format(movie[0], movie[1], movie[2]))


    def show_movie_projections(self, movie_id, date=None):
        self.movie_id = movie_id
        print("Projections for movie '{}':".format(self.cinema.get_movie(movie_id)[0]))
        if date is not None:
            for proj in self.cinema.show_movie_projection(movie_id, date):
                self.available[proj[0]] = proj[4]
                massage = "[{}] - {} ({}) - {} spots available"
                print(massage.format(proj[0], proj[2], proj[3], proj[4]))
        else:
            for proj in self.cinema.show_movie_projection(movie_id):
                self.available[proj[0]] = proj[4]
                massage = "[{}] - {} {} ({}) - {} spots available"
                print(massage.format(proj[0], proj[1], proj[2], proj[3], proj[4]))

    def helper(self):
        print("Type 'show_movies' to see all available movies")
        message = "Type 'show_movie_projections <movie_id> [<data>]' to see all available projections"
        print(message)
        print("Type 'make_reservation' to make a reservation")
        print("Type 'cancel_reservation <name>' to cancel reservation")
        print("Type 'exit' to stop the program")


    def start(self):
        while True:
            info = input(">")
            if info in self.spells:
                self.spells[info]()
            elif info == "exit":
                break
            else:
                try:
                    info = info.split(" ")
                    condition1 = info[0] == "show_movie_projections"
                    condition2 = int(info[1]) in self.movie_ids
                    if condition1 and condition2:
                        self.show_movie_projections(int(info[1]))
                    else:
                        print("Incorrect spell")
                except:
                    print("Incorrect spell")

    def make_reservation(self):
        index = 0
        for step in self.step1:
            while True:
                info = input(self.massages[index])
                if len(info) > 0:
                    break
            index += 1
            self.moves[step](info)
        self.show_movies()
        while True:
            info = input(self.massages[index])
            if len(info) > 0:
                break
        index += 1
        self.show_movie_projections(info)
        self.step_three()
        self.step_four()
        self.step_five()



def main():
    i_o = CLI()
    i_o.start()


if __name__ == '__main__':
    main()
