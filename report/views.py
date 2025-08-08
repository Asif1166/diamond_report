from django.shortcuts import redirect, render
from django.http import JsonResponse
from report.forms import ContactMessageForm
from report.models import *

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
    banner = HomeBanner.objects.first()
    about = AboutSection.objects.first()


    context = {
        'banner': banner,
        'about': about,

    }



    return render(request, 'home.html', context)



def report(request):


    context = {


    }



    return render(request, 'report.html', context)



def contact(request):
    contact_info = ContactInfo.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        return redirect('contact')  # Optional: thank you page

    return render(request, 'contact.html', {
        'contact_info': contact_info
    })