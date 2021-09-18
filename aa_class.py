class Song:
    def __init__(self, title="", author="", lyrics=("",), max_lines=0):
        self.title = title
        self.author = author
        self.lyrics = lyrics

    def sing(self, max_lines=-1):
        lyrics_len = self.lyrics[0:max_lines]
        print(f"{self.author} - {self.title}")
        print("\n".join(lyrics_len))
        return self

    def yell(self, max_lines=-1):
        lyrics_len = self.lyrics[0:max_lines]
        self.lyrics = [each_string.upper() for each_string in self.lyrics]
        print(f"{self.author} - {self.title}")
        print("\n".join(self.lyrics))
        return self


ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita.sing(1).yell()

ligo_dziesma = Song("Ligo", "Autobuss Debesis", ["Viens", "Divi", "Tris"])

print(ziemelmeita.title, ligo_dziesma.title)