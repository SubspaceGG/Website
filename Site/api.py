from ninja import NinjaAPI, Router

api = NinjaAPI()
webhooks = Router()


@api.get("/hello")
def hello(request):
    return "Hello world"


@api.get("/math/add")
def add(request, a: int, b: int):
    return a + b

# @webhooks.post("webhooks/openphone")
# def openphone(request):
