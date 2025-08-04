from django.shortcuts import render
from django.http import JsonResponse
from report.models import DiamondReport

# Create your views here.

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)



def get_report_data(request):
    report_number = request.GET.get('report_number')
    try:
        report = DiamondReport.objects.get(report_number=report_number)
        data = {
            'report_number': report.report_number,
            'product': report.product,
            'g_weight': report.g_weight,
            'dia_weight': report.dia_weight,
            'colour': report.colour,
            'clarity': report.clarity,
            'finish': report.finish,
            'cut': report.cut,
            'metal': report.metal,
            'diamond_image': report.diamond_image.url if report.diamond_image else '',
        }
        return JsonResponse({'success': True, 'data': data})
    except DiamondReport.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Report not found'})


def home(request):


    context = {


    }



    return render(request, 'home.html', context)
