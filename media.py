import webbrowser
class Movie():
    def __init__(self,movie_title,movie_storyline,movie_image,youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = youtube_trailer
    def show_trailer(self):

        webbrowser.open(self.youtube_trailer_url)
