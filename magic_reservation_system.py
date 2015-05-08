from database import Database
import sys

class CLI:
    def __init__(self):
        self.cinema = Database("cinema.db")
        self.username = ""
        self.tickets = 0
        self.available = {}
        self.seats = []
        self.reservations = []


    def step_one(self):
        self.username = input("Choose name>")
        self.tickets = input("Choose number of tickets>")
        self.show_movies()

    def step_two(self):
        movie = input("Choose a movie>")
        self.show_movie_projections(movie)

    def step_three(self):
        to_str = ""
        projection = input("Choose a projection>")
        while False:
            if self.available[projection] > self.tickets:
                break
            projection = input("Choose a projection>")
        self.seats = self.cinema.get_available_spots(projection)
        print(self.seats)

    def is_taken(self, row, col):
        if self.seats[row][col] != "X":
            return False
        else:
            return True

    def step_four(self):
        for ticket in range(1, self.tickets + 1):
            while True:
                seat = input("Choose seat {}>".format(ticket))
                row_in_range = seat[0] in range(1, 10)
                col_in_range = seat[1] in range(1, 10)
                if row_in_range and col_in_range and not self.is_taken(seat[0], seat[1]):
                    self.reservations.append(seat)
                    break
                elif self.is_taken(seat[0], seat[1]):
                    print("Out of range")
                else:
                    print("Seat is already taken")

    def step_five(self):
        print("This is your reservation:")
        print("Movie: Wreck-It Ralph (7.8)")



    def show_movies(self):
        print("Current movies:")
        for movie in self.cinema.show_movies():
            print("[{}] - {} ({})".format(movie[0], movie[1], movie[2]))


    def show_movie_projections(self, movie_id, date=None):
        print("Projections for movie '{}':".format(self.cinema.get_movie(movie_id)))
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




    def make_reservation(self):
        self.step_one()
        self.step_two()
        self.step_three()


def main():
    i_o = CLI()
    i_o.make_reservation()


if __name__ == '__main__':
    main()
