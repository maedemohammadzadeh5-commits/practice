#  Movie کلاس
class Movie:

    def __init__(self, name, genre, price):
        self.name = name
        self.genre = genre
        self.price = price

    def show(self):
        print(f"{self.name} | {self.genre} | {self.price}")


#  Customer کلاس
class Customer:

    def __init__(self, name):
        self.name = name


#  Hall کلاس
class Hall:

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        # ساخت دیکشنری
        self.seats = {}

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.seats[(r, c)] = False

    def show_seats(self):

        print()

        for r in range(1, self.rows + 1):

            for c in range(1, self.cols + 1):

                if self.seats[(r, c)]:
                    print("X", end=" ")
                else:
                    print("O", end=" ")

            print()

    def reserve(self, seat):

        if self.seats[seat]:
            print("Seat is already reserved!")
        else:
            self.seats[seat] = True
            print("Reservation Successful!")


#  Cinema کلاس
class Cinema:

    def __init__(self):

        # ساخت لیست
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def show_movies(self):

        print("Movies")

        for movie in self.movies:
            movie.show()


# برنامه اصلی

cinema = Cinema()

movie1 = Movie("Interstellar", "Sci-Fi", 250000)
movie2 = Movie("Batman", "Action", 200000)

cinema.add_movie(movie1)
cinema.add_movie(movie2)

customer = Customer("Ali")

hall = Hall(3, 3)

cinema.show_movies()

hall.show_seats()

hall.reserve((2, 2))
hall.reserve((1, 3))
hall.reserve((2, 2))

hall.show_seats()