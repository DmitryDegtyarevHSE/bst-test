import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Robot


@method_decorator(csrf_exempt, name="dispatch")
class RobotView(View):
    http_method_names = ['post']

    def post(self, request):
        try:
            data = json.loads(request.body)
            robot = Robot(
                model=data["model"],
                version=data["version"],
                created=data["created"],
            )
            robot.full_clean()
            robot.save()
            return JsonResponse({"message": "created"}, status=200)
        except (KeyError, json.JSONDecodeError, ValidationError) as e:
            return JsonResponse({'error': str(e)}, status=400)
