from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from . import train_predict, summary
from django.http import HttpResponse
from django.core.mail import send_mail
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .render import Render
from django.views.generic import View
from django.utils import timezone
import json

def index(request):
    return render(request, 'index.html')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        to_email = request.POST['email']
        to_email1 = request.POST['email1']

        #return render(request, 'upload.html', {
        #    'uploaded_file_url': uploaded_file_url
        #})
        msg = train_predict.predict(filename)
        summ = summary.summary(msg)

        request.session['export'] = summ
        context = {
            'result': msg,
            'img_url': uploaded_file_url,
            'summary': summ,
            'json': json.dumps(msg),
        }

        message = "Hello, Based on your handwriting, we analysed following predictions about you: \n"+summ
        if to_email != "":
            mail_subject = "Personality prediction using handwriting analysis"
            send_mail(mail_subject, message, 'evolettech@gmail.com', [to_email,to_email1])
        return render(request, 'output.html', context)

    return render(request, 'upload.html')

#def export(request):
#    response = HttpResponse(content_type='application/pdf')
#    response['Content-Disposition'] = 'inline; filename="result.pdf"'
#
#    buffer = BytesIO()
#    p = canvas.Canvas(buffer)
#
#   pdf_content= request.session['export']
#    # Start writing the PDF here
#    p.drawString(500, 500, 'Hello world.'+ pdf_content)
#    # End writing

#    p.showPage()
#    p.save()

#    pdf = buffer.getvalue()
#    buffer.close()
#    response.write(pdf)

#    return response


def export(request):
    pdf_content = request.session['export']
    params = {
        'content': pdf_content,
        'request': request,

    }
    return Render.render('pdf.html', params)