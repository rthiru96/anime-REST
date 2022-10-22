import falcon
import json
from .model import Anime

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict


class AnimeResource(object):

    def on_get(self,req,resp):
        obj = OrderedDict()
        contacts = Anime.get_animes()
        print(contacts,"tesr")
        obj = [contact.to_dict() for contact in contacts]
        resp.body = json.dumps(obj)
        resp.status=falcon.HTTP_200

    def on_post(self, req, resp):
        anime_details = req.media
        anime=anime_details['anime']
        released_date=anime_details['released_date']
        seasons=anime_details['seasons']  
        test = Anime(anime,released_date,seasons)
        test.create_animes()
        resp.body = json.dumps({'message':'Anime created'})
        resp.status=falcon.HTTP_200

    def on_patch(self, req, resp, id):
        anime_details = req.media
        anime=anime_details['anime']
        released_date=anime_details['released_date']
        seasons=anime_details['seasons']  
        Anime.update_anime(id=id,data = anime_details)
        resp.body = json.dumps({'message':'Anime updated'})
        resp.status=falcon.HTTP_200

    def on_delete(self, req, resp, id):
        Anime.delete_anime(id=id)
        resp.body = json.dumps({'message':'Anime deleted sucessfully!'})
        resp.status=falcon.HTTP_200