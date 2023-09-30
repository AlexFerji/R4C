import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View

from .models import Robot


@method_decorator(csrf_exempt, name='dispatch')
class RobotView(View):
    def post(self, request):
        data = json.loads(request.body)

        robot_model = data.get('model')
        robot_version = data.get('version')
        robot_created = data.get('created')
        robot_serial = f"{robot_model}-{robot_version}"

        robot_data = {
            'serial': robot_serial,
            'model': robot_model,
            'version': robot_version,
            "created": robot_created
        }


        robot_obj = Robot.objects.create(**robot_data)

        data_message = {
            'message': f'Новый робот создан {robot_obj.serial}'
        }
        return JsonResponse(data_message, status=201)
