############################
# SENTIMENT ANALYSIS
# RAP VS. INDIE MUSIC
############################
# Created by Emma Hermanson
# 11.25.20
############################
# ALBUM 1: Chance the Rapper's "Acid Rap"
# ALBUM 2: The Head and the Heart's "The Head and The Heart"
############################
# importing lyrics from Genius.com into json files
# part 1 of sentiment analysis 
############################
import lyricsgenius

token = "zUUHoMg94K4n9pS1HnrkBC1F9RI5DFV5ek1rfWCTfs9Z9ViXMlrrdSIwEDL3obsh"
api = lyricsgenius.Genius(token)

####################################################################################
# IMPORT CHANCE'S ALBUM #
####################################################################################
artist1 = api.search_artist('Chance the Rapper', max_songs=1)
song1 = api.search_song("Good Ass Intro", artist1.name)
artist1.add_song(song1)
song2 = api.search_song("Pusha Man", artist1.name)
artist1.add_song(song2)
song3 = api.search_song("Paranoia", artist1.name)
artist1.add_song(song3)
song4 = api.search_song("Cocoa Butter Kisses", artist1.name)
artist1.add_song(song4)
song5 = api.search_song("Juice", artist1.name)
artist1.add_song(song5)
song6 = api.search_song("Lost", artist1.name)
artist1.add_song(song6)
song7 = api.search_song("Everybody's Something", artist1.name)
artist1.add_song(song7)
song8 = api.search_song("Interlude (That's Love)", artist1.name)
artist1.add_song(song8)
song9 = api.search_song("Favorite Song", artist1.name)
artist1.add_song(song9)
song10 = api.search_song("NaNa", artist1.name)
artist1.add_song(song10)
song11 = api.search_song("Smoke Again", artist1.name)
artist1.add_song(song11)
song12 = api.search_song("Acid Rain", artist1.name)
artist1.add_song(song12)
song13 = api.search_song("Chain Smoker", artist1.name)
artist1.add_song(song13)
song14 = api.search_song("Everything's Good (Good Ass Outro)", artist1.name)
artist1.add_song(song14)

# save and print album #
artist1.save_lyrics()
print(artist1)

####################################################################################
# IMPORT THE HEAD AND THE HEART ALBUM #
####################################################################################
artist2 = api.search_artist("The Head And The Heart", max_songs=1)
song_1 = api.search_song("Cats and Dogs", artist2.name)
artist2.add_song(song_1)
song_2 = api.search_song("Couer d'Alene", artist2.name)
artist2.add_song(song_2)
song_3 = api.search_song("Ghosts", artist2.name)
artist2.add_song(song_3)
song_4 = api.search_song("Down in the Valley", artist2.name)
artist2.add_song(song_4)
song_5 = api.search_song("Rivers and Roads", artist2.name)
artist2.add_song(song_5)
song_6 = api.search_song("Honey Come Home", artist2.name)
artist2.add_song(song_6)
song_7 = api.search_song("Lost in my Mind", artist2.name)
artist2.add_song(song_7)
song_8 = api.search_song("Winter Song", artist2.name)
artist2.add_song(song_8)
song_9 = api.search_song("Sounds Like Hallelujah", artist2.name)
artist2.add_song(song_9)
song_10 = api.search_song("Heaven Go Easy on Me", artist2.name)
artist2.add_song(song_10)

# save and print album #
artist2.save_lyrics()
print(artist2)

