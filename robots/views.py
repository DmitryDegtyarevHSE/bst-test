import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .services import save_robot, create_excel_report, get_current_date


@method_decorator(csrf_exempt, name='dispatch')
class RobotView(View):
    http_method_names = ['post']

    def post(self, request):
        try:
            data = json.loads(request.body)
            save_robot(data)
            return JsonResponse({"message": "created"}, status=200)
        except (KeyError, json.JSONDecodeError, ValidationError) as e:
            return JsonResponse({'error': str(e)}, status=400)


def download_excel(request):
    wb = create_excel_report()
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = \
        f'attachment; filename=robots-count-week-{get_current_date()}.xlsx'
    wb.save(response)
    return response


