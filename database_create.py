from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

artist_publisher = Table(
    "artist_publisher",
    Base.metadata,
    Column("artist_id", Integer, ForeignKey("author.author_id")),
    Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
)

album_publisher = Table(
    "album_publisher",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("album.album_id")),
    Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
)

class Artist(Base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    died = Column(Bool)
    albuns = relationship("Album", backref=backref("artist"))

class Album(Base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("artist.author_id"))
    title = Column(String)
da    date = Column(String)

class Publisher(Base):
    __tablename__ = "publisher"
    publisher_id = Column(Integer, primary_key=True)
    name = Column(String)
    authors = relationship(
        "Author", secondary=author_publisher, back_populates="publishers"
    )
    books = relationship(
        "Book", secondary=book_publisher, back_populates="publishers"
    )
