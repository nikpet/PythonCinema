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
        self.seats_tuples = []
        self.reservations = []
        self.proj_id = 0

    CHOOSE_NAME = "Step 1(User): Choose name>"
    CHOOSE_TICKET_NUM = "Step 1(User): Choose number of tickets>"
    CHOOSE_MOVIE = "Step 2(Movie): Choose a movie>"
    CHOOSE_PROJECTION = "Step 3(Projection): Choose a projection>"
    STEP_5 = "Step 5 (Confirm - type 'finalize')>"
    NUMS = [str(i) for i in range(1, 10)]

    def _choose_name(self):
        while True:
            var_input = input(self.CHOOSE_NAME)
            if len(var_input) > 2:
                self.username = var_input
                return True

    def _choose_num_tickets(self):
        while True:
            var_input = input(self.CHOOSE_TICKET_NUM)
            try:
                var_int = int(var_input)
                if var_int > 0 and var_int < 120:
                    self.tickets = var_int
                    return True
                else:
                    print("Wrong input")
            except:
                print("Wrong input")

    def _choose_movie(self):
        while True:
            var_input = input(self.CHOOSE_MOVIE)
            try:
                var_int = int(var_input)
                if var_int in self.movie_ids:
                    self.movie_id = var_input
                    return True
                else:
                    print("There is no such movie id")
            except:
                print("Wrong input")


    def _choose_projection(self):
        while True:
            projection = input(self.CHOOSE_PROJECTION)
            int_proj = int(projection)
            if self.available[int_proj] < self.tickets:
                print("Not enaugh available seats")
                self._choose_num_tickets()
            else:
                self.proj_id = int_proj
                return True

    def get_available_seats(self, proj_id):
        to_str = ""
        self.seats = self.cinema.get_available_spots(proj_id)
        for number in range(0, 11):
            to_str += " ".join([seat for seat in self.seats[number]])
            to_str += "\n"
        print(to_str)

    def is_free(self, row, col):
        if self.seats[row][col] == "X":
            return False
        else:
            return True

    def step_four(self):
        for ticket in range(1, int(self.tickets) + 1):
            while True:
                seat = input("Step 4 (Seats): Choose seat {}>".format(ticket))
                try:
                    row_col = eval(seat)
                    row_in_range = row_col[0] in range(1, 11)
                    col_in_range = row_col[1] in range(1, 11)
                    is_free = self.is_free(row_col[0], row_col[1])
                    if row_in_range and col_in_range and is_free:
                        self.seats[row_col[0]][row_col[1]] = "X"
                        self.reservations.append((row_col[0], row_col[1]))
                        self.seats_tuples.append(row_col)
                        break
                    elif not self.is_free(row_col[0], row_col[1]):
                        print("Seat is already taken")
                    else:
                        print("Out of range")
                except:
                    print("Invalid input")

    def _finalize(self):
        print("This is your reservation:")
        movie = self.cinema.get_movie(self.movie_id)
        proj = self.cinema.get_projection(self.proj_id)
        print("Movie: {} {}".format(movie[0], movie[1]))
        print("Date and Time: {} {} {}".format(proj[0], proj[1], proj[2]))
        tuples = str(self.seats_tuples)
        print("Seats: {}".format(tuples[1:len(tuples)-1]))
        while True:
            var_input = input(self.STEP_5)
            if var_input == "finalize":
                self.cinema.make_reservations(self.username, self.proj_id, self.seats_tuples)
                print("Thanks!")
                break




    def show_movies(self):
        print("Current movies:")
        for movie in self.cinema.show_movies():
            if movie[0] not in self.movie_ids:
                self.movie_ids.append(movie[0])
            print("[{}] - {} ({})".format(movie[0], movie[1], movie[2]))


    def show_movie_projections(self, movie_id, date=None):
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



    def help(self):
        print("Type 'show_movies' to see all available movies")
        message = "Type 'show_movie_projections <movie_id> [<data>]' to see all available projections"
        print(message)
        print("Type 'make_reservation' to make a reservation")
        print("Type 'cancel_reservation <name>' to cancel reservation")
        print("Type 'exit' to stop the program")



    def start(self):
        while True:
            var_input = input("comand>")
            #try:
            if ' ' not in var_input:
                function = "self.{}()".format(var_input)
                eval(function)
            inputs = var_input.split(' ')
            if inputs[1][0] in self.NUMS:
                function = "self.{}({})".format(inputs[0], inputs[1])
                eval(function)
            else:
                function = "self.{}('{}')".format(inputs[0], inputs[1])
                eval(function)

            #except:
            #    print("Wrong spell!")

    def make_reservation(self):
        self._choose_name()
        self._choose_num_tickets()
        self.show_movies()
        self._choose_movie()
        self.show_movie_projections(self.movie_id)
        self._choose_projection()
        self.get_available_seats(self.proj_id)
        self.step_four()
        self._finalize()

    def cancel_reservation(self, username):
        self.cinema.cancel_reservation(username)

    def give_up(self):
        print("You gave out your, reservation")
        print("Have a nice day!")
        self.start()


def main():
    i_o = CLI()
    i_o.start()


if __name__ == '__main__':
    main()
