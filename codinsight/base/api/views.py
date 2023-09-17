from django.http import JsonResponse
def getRoutes(req):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return JsonResponse(routes, safe=False)
# safe allow this to be more than python dictionary. 