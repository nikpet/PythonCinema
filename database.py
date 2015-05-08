import sqlite3


class Database:
    def __init__(self, database):
        self.db = sqlite3.connect(database)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def show_movies(self):
        query = """
            SELECT movie_id, movie_name, rating
            FROM Movies
            ORDER BY rating DESC
        """
        return self.cursor.execute(query).fetchall()

    def show_movie_projection(self, movie_id, date=None):
        query = """
            SELECT type, date, time, 100 - COUNT(row) AS available_spots
            FROM Projections AS p
            LEFT JOIN Reservations AS R
            ON p.projection_id = r.projection_id
            WHERE movie_id = ?
            {}
            GROUP BY type, time, date
            ORDER BY date, time ASC
        """
        if date is not None:
            query = query.format("""
                AND date = ?
            """)
            return self.cursor.execute(query, (movie_id, date)).fetchall()
        else:
            query = query.format('')
            return self.cursor.execute(query, (movie_id,)).fetchall()

    def make_reservation(self, movie_name, number_of_tickets):
        pass

    def cancel_reservation(self, name):
        pass

def main():
    cinema = Database("cinema.db")
    print(cinema.show_movie_projection(1, '2014-04-01'))


if __name__ == '__main__':
    main()
