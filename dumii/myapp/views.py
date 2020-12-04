from django.shortcuts import render
import os
from django.conf import settings
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect

from django.shortcuts import render
from .registry_class import ModelsRegistryHolder
from .services import add_classes_to_server
from django.http import HttpResponse
from django.template import RequestContext

@permission_required('admin.can_add_log_entry')
def upload(request):
    template = "csv.html"


    prompt = {


    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES.get('file')
    if not csv_file:
        messages.error(request, "Please attach a csv file")
        return redirect('/upload-csv/')
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not csv file')
        return redirect('/upload-csv/')


    add_classes_to_server()
    model = ModelsRegistryHolder().get(request.POST.get('model'))
    if not model:
        messages.error(request, f"Specified model not found {request.POST.get('model')}")
        return redirect('/upload-csv/')

    try:
        model.execute(csv_file)
    except Exception as e:
        messages.error(request, f"Exception Occured - {e}")
        return redirect('/upload-csv/')
    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application;filename=file.csv")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise HttpResponse

