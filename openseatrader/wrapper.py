from requests import Request, Session
from models.collection import Collection

_s = Session()

def retrieve_a_single_collection(collection_slug):
    url = "https://api.opensea.io/api/v1/collection/{collection_slug}".format(collection_slug=collection_slug)
    r = Request('GET', url)
    collection = Collection(collection_slug)
    collection.update(_s.send(r.prepare()).json()['collection'])
    return collection