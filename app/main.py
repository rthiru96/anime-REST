import json
import falcon
from .resource import AnimeResource


class IndexResource(object):
  def on_get(self,req,res):
    res.status = falcon.HTTP_200
    res.body = json.dumps({"success": "My first falcon app"})



application = falcon.App()
application.add_route('/', IndexResource())
application.add_route('/anime/', AnimeResource())
application.add_route('/anime/{id}', AnimeResource())

if __name__ == "__main__":
  application.run(host="0.0.0.0", debug=True)