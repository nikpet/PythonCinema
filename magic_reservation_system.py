from database import Database

class CLI:
    def __init__(self):
        self.cinema = Database("cinema.db")

    def show_movies(self):
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

def main():
    i_o = CLI()
    i_o.show_movies()
    i_o.show_movie_projections(1, '2014-04-01')
    i_o.show_movie_projections(2)


if __name__ == '__main__':
    main()

