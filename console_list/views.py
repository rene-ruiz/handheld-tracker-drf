from django.http import JsonResponse


def console_list(request):
    if request.method == "GET":
        return JsonResponse({"Hola": "Mundo"})
