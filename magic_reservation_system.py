from database import Database
import sys

class CLI:
    def __init__(self):
        self.cinema = Database("cinema.db")
        self.username = ""
        self.tickets = 0
        self.options = {}

    STEPS = [
        "STEP 1",
        "STEP 2",
        "STEP 3",
        "STEP 3"
    ]

    def step_one(self):
        self.username = input("Choose name>")
        self.tickets = input("Choose number of tickets>")

    def show_movies(self):
        print("Current movies:")
        for movie in self.cinema.show_movies():
            print("[{}] - {} ({})".format(movie[0], movie[1], movie[2]))

    def show_movie_projections(self, movie_id, date=None):
        if date is not None:
            for proj in self.cinema.show_movie_projection(movie_id, date):
                massage = "[{}] - {} ({}) - {} spots available"
                print(massage.format(proj[0], proj[2], proj[3], proj[4]))
        else:
            for proj in self.cinema.show_movie_projection(movie_id):
                massage = "[{}] - {} {} ({}) - {} spots available"
                print(massage.format(proj[0], proj[1], proj[2], proj[3], proj[4]))

    def make_reservation(self):
        self.step_one()
        self.show_movies()
        movie = input("Choose a movie>")
        self.show_movie_projections(movie)

def main():
    i_o = CLI()
    i_o.make_reservation()


if __name__ == '__main__':
    main()

