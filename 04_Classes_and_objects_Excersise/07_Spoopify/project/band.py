from projectw.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.details()}."

    def remove_album(self, album_name):
        if album_name not in self.albums:
            return f"Album {album_name} is not found."

        if album_name.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album_name)
        return f"Album {album_name} has been removed."

    def details(self):
        result = [f"Band {self.name}"]

        if self.albums:
            for el in self.albums:
                result.append(Album.details(el))

        return "\n".join(result)
