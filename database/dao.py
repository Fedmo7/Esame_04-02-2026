from networkx.algorithms.components import articulation_points

from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_authorship(ruolo):

        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query ='''SELECT a.artist_id ,a.name,sum(o.curator_approved) as num_objects
FROM authorship au,objects o,artists a 
where au.`role`  =%s and
au.object_id =o.object_id and o.curator_approved =1 
and a.artist_id =au.artist_id 
group by a.artist_id,a.name '''

        cursor.execute(query,(ruolo,))

        for row in cursor:
            artista = Artist(row['artist_id'],row['name'], row['num_objects'])
            result[row['artist_id']] = artista


        cursor.close()
        conn.close()
        return result


    @staticmethod
    def query_ruoli():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = '''
                    select distinct a.role
                    from authorship a 
                '''

        cursor.execute(query)

        for row in cursor:
            result.append(row['role'])


        cursor.close()
        conn.close()
        return result


