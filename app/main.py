import json
import falcon
from .resource import AnimeResource

application = falcon.App()
application.add_route('/anime/', AnimeResource())
application.add_route('/anime/{id}', AnimeResource())

if __name__ == "__main__":
  application.run(host="0.0.0.0", debug=True)