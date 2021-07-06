from main import Movie
import fresh_tomatoes

# Movie instances

snake_eyes = Movie("Snake Eyes", "An ancient Japanese clan called the Arashikage welcomes tenacious loner Snake Eyes after he saves the life of their heir apparent. Upon arrival in Japan, the Arashikage teach him the ways of the ninja warrior while also providing him something he's been longing for: a home. However, when secrets from Snake Eyes' past are revealed, his honor and allegiance get tested -- even if that means losing the trust of those closest to him.",
                   "https://upload.wikimedia.org/wikipedia/en/d/da/Snake_Eyes_G.I._Joe_Origins_Movie_Poster.jpg", "https://www.youtube.com/watch?v=fOzewsswtGM")


without_remorse = Movie("Without Remorse", "Seeking justice for the murder of his pregnant wife, an elite Navy SEAL uncovers a covert plot that threatens to engulf the United States and Russia in an all-out war.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f7/Without_Remorse_poster.jpg", "https://www.youtube.com/watch?v=e-rw2cxFVLg")

fast_nine = Movie("Fast and Furious 9", " Dom's crew soon comes together to stop a world-shattering plot by the most skilled assassin and high-performance driver they've ever encountered -- Dom's forsaken brother.",
                  "https://upload.wikimedia.org/wikipedia/en/2/2b/F9_film_poster.jpg", "https://www.youtube.com/watch?v=_qyw6LC5pnE")

suicide_squad = Movie("Suicide Squad 2", "Armed with high-tech weapons, the most dangerous supervillains trek through the dangerous jungle on a search-and-destroy mission, with only Col. Rick Flag on the ground to make them behave.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/The_Suicide_Squad_official_poster.jpeg/1200px-The_Suicide_Squad_official_poster.jpeg", "https://www.youtube.com/watch?v=vBumm7mYT_0")

justice_league = Movie("Zack Snyder's Justice League", "Despite the formation of an unprecedented league of heroes -- Batman, Wonder Woman, Aquaman, Cyborg and the Flash -- it may be too late to save the planet from an assault of catastrophic proportions.",
                       "https://upload.wikimedia.org/wikipedia/en/6/60/Zack_Snyder%27s_Justice_League.png", "https://www.youtube.com/watch?v=vM-Bja2Gy04")

black_widow = Movie("Black Widow", "Natasha must deal with her history as a spy, and the broken relationships left in her wake long before she became an Avenger.",
                    "https://upload.wikimedia.org/wikipedia/en/e/e9/Black_Widow_%282021_film%29_poster.jpg", "https://www.youtube.com/watch?v=Fp9pNPdNwjI")

mortal_kombat = Movie("Mortal Kombat", "Training with experienced fighters Liu Kang, Kung Lao and the rogue mercenary Kano, Cole prepares to stand with Earth's greatest champions to take on the enemies from Outworld in a high-stakes battle for the universe.",
                      "https://upload.wikimedia.org/wikipedia/en/3/37/Mortal_Kombat_%282021_film%29.png", "https://www.youtube.com/watch?v=QJHY4ggYCk4")

yasuke = Movie("Yasuke", "In an alternate-reality 16th century feudal Japan reimagined with magic and advanced technology, an African man named Yasuke went from being in the service of Jesuit missionaries during the Nanban trade to being a warrior and retainer in the service of Lord Oda Nobunaga.",
               "https://upload.wikimedia.org/wikipedia/en/e/e6/Yasuke_poster.jpg", "https://www.youtube.com/watch?v=ijKAtzQY1wc")

naruto = Movie("Naruto Shippuden", "Naruto Shippuden is the second series of Naruto anime that follows the titular hero on his quest to become Hokage",
               "https://upload.wikimedia.org/wikipedia/en/a/ad/Naruto_-_Shippuden_DVD_season_1_volume_1.jpg", "https://www.youtube.com/watch?v=thh7bVCgDHs")

# Organize movie instances in a list
movies = [snake_eyes, without_remorse, fast_nine, suicide_squad, justice_league, black_widow, mortal_kombat, yasuke, naruto]



# Generate html page
if __name__ == "__main__":
    fresh_tomatoes.open_movies_page(movies)