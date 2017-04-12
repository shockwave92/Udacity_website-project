import media, fresh_tomatoes

#Add movie information
toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=4KPTXpQehio', '1995')

avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY', '2009')

inception = media.Movie('Inception',
                     'A man who hacked peoples dream',
                     'https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg',
                     'https://www.youtube.com/watch?v=d3A3-zSOBT4', '2010')

#print avatar.storyline
#inception.show_trailer()

distric_9 = media.Movie('Distric 9',
                     'A story of a man changed to alien',
                     'https://images-na.ssl-images-amazon.com/images/M/MV5BMTM4OTI1OTM5NF5BMl5BanBnXkFtZTcwMzk5MTU1Mg@@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
                     'https://www.youtube.com/watch?v=DyLUwOcR5pk', '2009')

world_war_z = media.Movie('World War Z',
                     'Zombie attack!',
                     'https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/World_War_Z_poster.jpg/220px-World_War_Z_poster.jpg',
                     'https://www.youtube.com/watch?v=HcwTxRuq-uk','2013')

chefs_table = media.Movie('Chefs Table',
                     'Series storys about world top chefs',
                     'https://upload.wikimedia.org/wikipedia/en/1/11/Chef%27s_Table.jpg',
                     'https://www.youtube.com/watch?v=qKqj85oo2wI', '2015')

movies = [toy_story, avatar, inception, distric_9, world_war_z, chefs_table]


#Open html file from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS
#print media.Movie.__doc__
