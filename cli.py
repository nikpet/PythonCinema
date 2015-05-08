from database import Database

class CLI:
    def __init__(self):
        self.cinema = Database("cinema.db")

    def show_movies(self):
        for movie in self.cinema.show_movies():
            print("[{}] - {} ({})".format(movie[0], movie[1], movie[2]))

def main():
    i_o = CLI()
    i_o.show_movies()


if __name__ == '__main__':
    main()

