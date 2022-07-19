def get_albums_by_publisher(data, ascending=True):
    """Return the number of books by each publisher as a pandas series"""
    return data.groupby("publisher").size().sort_values(ascending=ascending)

def get_artists_by_publisher(data, ascending=True):
    """Returns the number of authors by each publisher as a pandas series"""
    return (
        data.assign(name=data.first_name.str.cat(data.last_name, sep=" "))
        .groupby("publisher")
        .nunique()
        .loc[:, "name"]
        .sort_values(ascending=ascending)
    )

def get_authors(session):
    """Get a list of author objects sorted by last name"""
    return session.query(Author).order_by(Author.last_name).all()


def main():
    """Main entry point of program"""
    # Connect to the database using SQLAlchemy
    with resources.path(
        "project.data", "author_book_publisher.db"
    ) as sqlite_filepath:
        engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()


    albums_by_publisher = get_albums_by_publishers(session, ascending=False)
    for row in albums_by_publisher:
        print(f"Publisher: {row.name}")
    print()
"
    # Get the number of authors each publisher publishes
    artists_by_publisher = get_artists_by_publishers(session)
    for row in authors_by_publisher:
        print(f"Publisher: {row.name}")
    print()

    # Output hierarchical author data
    artists = get_artists(session)
    output_author_hierarchy(authors)

    # Add a new book
    add_new_album(
        session,
        artist_name="Novelle Vague",
        title="Na fruteira",
        publisher_name="Indie",
    )
    # Output the updated hierarchical author data
    authors = get_authors(session)

if __name__ == "__main__":
    main()
