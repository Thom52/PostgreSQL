from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Executing the instructions from our localhost "chinook" database(db)
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# Creating the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - Select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#    print(artist.ArtistId, artist.Name, sep=" | ")


# Query 2 - Select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#    print(artist.Name)


# Query 3 - Select only "Queen" from "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")


# Query 4 - Select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")


# Query 5 - Select only the albums with "ArtistId" #51 from the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")


# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )