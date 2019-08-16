from werkzeug import Request,Response,run_simple
from werkzeug import _easteregg

@Request.application
def application(request):
	return Response('Hello World!')

run_simple('localhost',8080,_easteregg(application))
