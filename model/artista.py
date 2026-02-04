from dataclasses import dataclass


@dataclass
class Artista:
    artist_id = int
    name = str
    role = str
    indice = int



    def __str__(self):
        return f'{self.artist_id} ({self.name})'

    def __hash__(self):
        return hash(self.artist_id)

    def __eq__(self, other):
        if isinstance(other, Artista):
            return self.artist_id== other.artist_id
        return False