import fresh_tomatoes
import media
import webbrowser

anand = media.Movie("Anand",
                    "The story of a terminally ill man who wishes to live life to the full before the inevitable occurs, as told by his best friend.",
                    "https://upload.wikimedia.org/wikipedia/en/c/c9/Anand_film.jpg",
                    "https://www.youtube.com/watch?v=tfGX2AEaMUU")



dangal = media.Movie("Dangal ",
                     "Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games in the face of societal oppression.",
                     "http://t3.gstatic.com/images?q=tbn:ANd9GcQIXnFlBKGWT1ByyIu3qfxX6opQX6BmeeU_qsiE3X8rX9ZRr63r",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")


the_3idiots = media.Movie("The 3idiots",
                      "Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them idiots",
                      "http://sites.psu.edu/pragnyaprabakaran/wp-content/uploads/sites/38771/2016/04/3i-poster-3.jpg",
                      "https://www.youtube.com/watch?v=K0eDlFX9GMc")

jane_bhi_do_yaaro =  media.Movie("Jane bhi do yaaro",
                                 "Two friends, attempting to start-up their own photo studio, come across shady dealings, corruption and murder, and must fight to bring the guilty to light",
                                 "https://upload.wikimedia.org/wikipedia/en/6/6e/Jaane_Bhi_Do_Yaaro_1983_film_poster.jpg",
                                 "https://www.youtube.com/watch?v=spkmLziFFg4")
golmaal = media.Movie("Golmaal",
                      "Ramprasad is a recent college graduate who finds a job with a finicky man, Bhavani Shankar, who believes that a man without a mustache is a man without a character.",
                      "http://apna.com.pk/wp-content/uploads/2016/07/Golmaal-1979.jpg",
                      "https://www.youtube.com/watch?v=btYDKUZZQwk")
black_friday = media.Movie("Black Friday",
                           "Black Friday is a film about the investigations following the 1993 serial Bombay bomb blasts, told through the different stories of the people involved --police, conspirators, victims, middlemen",
                           "http://ecx.images-amazon.com/images/I/81AftiYKiOL._SY445_.jpg",
                           "https://www.youtube.com/watch?v=e0IyAAOmwx4")
                           
                    



movies = [anand,dangal,the_3idiots,jane_bhi_do_yaaro,golmaal,black_friday]
fresh_tomatoes.open_movies_page(movies)




