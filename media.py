import webbrowser


# Movie class
class Movie():
    def __init__(self, title, image_url, trailer_url):
        self.title = title
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url

    # show_trailer function open a web page that shows the Movie's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer)
