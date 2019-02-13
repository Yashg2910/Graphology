from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from . import train_predict, summary
from django.http import HttpResponse
from django.core.mail import send_mail


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        to_email = request.POST['email']
        #return render(request, 'upload.html', {
        #    'uploaded_file_url': uploaded_file_url
        #})
        msg = train_predict.predict(filename)
        summ = summary.summary(msg)
        context = {
            'result': msg,
            'img_url': uploaded_file_url,
            'summary': summ,
        }
        message = summ
        mail_subject = "Personality prediction using handwriting analysis"
        send_mail(mail_subject, message, 'evolettech@gmail.com', [to_email])
        return render(request, 'output.html', context)

    return render(request, 'upload.html')