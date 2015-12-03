import media
import fresh_tomatoes


# Create mutiple instances of Movie, one for each type of movie
braveheart = media.Movie("Braveheart",
                         ("https://upload.wikimedia.org/wikipedia/en/5/55/"
                          "Braveheart_imp.jpg"),
                         "https://www.youtube.com/watch?v=wj0I8xVTV18")

movie_300 = media.Movie("300",
                        ("https://upload.wikimedia.org/wikipedia/en/5/5c/"
                         "300poster.jpg"),
                        "https://www.youtube.com/watch?v=UrIbxk7idYA")

slumdog = media.Movie("Slumdog Millionaire",
                      ("https://upload.wikimedia.org/wikipedia/en/f/fe/"
                       "Slumdog_millionaire_ver2.jpg"),
                      "https://www.youtube.com/watch?v=JwiU94p9XPA")

usual_suspects = media.Movie("The Usual Suspects",
                             ("https://upload.wikimedia.org/wikipedia/en/9/9c/"
                              "Usual_suspects_ver1.jpg"),
                             "https://www.youtube.com/watch?v=oiXdPolca5w")


# Populate an array with all the movie instances
movies = [braveheart, movie_300, slumdog, usual_suspects]

# execute function to generate web page that will display the given array
fresh_tomatoes.open_movies_page(movies)
