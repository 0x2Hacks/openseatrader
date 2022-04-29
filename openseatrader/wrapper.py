from requests import Request, Session
from openseatrader.models.collection import Collection

_s = Session()

def _send(request):
    return _s.send(request.prepare()).json()

def retrieve_a_single_collection(collection_slug):
    url = "https://api.opensea.io/api/v1/collection/{collection_slug}".format(collection_slug=collection_slug)
    r = Request('GET', url)
    collection = Collection(collection_slug)
    collection.update(_send(r)['collection'])
    return collection

def retrieve_collection_stats(collection_slug):
    url = "https://api.opensea.io/api/v1/collection/{collection_slug}/stats".format(collection_slug=collection_slug)
    r = Request('GET', url)
    return _send(r)