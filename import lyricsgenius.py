import lyricsgenius 
api_key = "FJCAOWV_zrjuXCE_mMDmfFR4_jXHYt2yUpufDp4JAgUeCje_lczg7m7VXCto65sm"
genius = lyricsgenius.Genius(api_key)
name = input("Enter Artist Name : ")
artist = genius.search_artist(name)
song = input("Type your song for Lyrics : ")
song = artist.song(song)
print(song.lyrics)