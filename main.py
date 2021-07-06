import webbrowser


# Main movie class 
class Movie:
    def __init__(self, title, description, poster_image, trailer_url):
        self.movie_title = title
        self.description = description
        self.poster = poster_image
        self.movie_trailer = trailer_url

    def show_movie(self):
        webbrowser.open(self.movie_trailer)


