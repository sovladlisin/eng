from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from app.forms import JobForm
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from app.models import Job, Card, PortfolioCard, PortfolioPicture, Certificate, Request
from django.http import StreamingHttpResponse, HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def handler404(request, exception):
    return redirect('app:home')


def Home(request):
    if request.user.is_authenticated:
        marker = True
    else:
        marker = False
    cards = Card.objects.all()
    portfolios = PortfolioCard.objects.all()
    return render(request, 'app/home.html', {'marker': marker, 'cards': cards, 'portfolio_cards': portfolios})


def Jobs(request):
    if request.user.is_authenticated:
        marker = True
    else:
        marker = False
    jobs = Job.objects.all()
    return render(request, 'app/jobs.html', {'marker': marker, 'jobs': jobs})


def Info(request):
    if request.user.is_authenticated:
        marker = True
    else:
        marker = False
    # jobs = Job.objects.all()
    return render(request, 'app/info.html', {'marker': marker})


def JobEdit(request, pk):
    if request.user.is_authenticated:
        job = get_object_or_404(Job, pk=pk)

        if request.method == "POST":
            form = JobForm(request.POST, request.FILES, instance=job)
            if form.is_valid():
                job = form.save(commit=False)
                job.save()
                return redirect('app:home')
            else:
                return HttpResponse("Ошибка в форме")
        else:
            form = JobForm(instance=job)
        return render(request, 'app/forms/jobEdit.html', {'form': form, 'job': job})
    else:
        return redirect('app:home')


def JobView(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'app/job.html', {'job': job})


def PortfolioJobView(request, pk):
    job = get_object_or_404(PortfolioCard, pk=pk)
    album = PortfolioPicture.objects.all().filter(portfolio_job=job)
    return render(request, 'app/portfolio_page.html', {'job': job, 'album': album})


def CertificatesView(request):
    album = Certificate.objects.all()
    return render(request, 'app/certificates.html', {'album': album})


def ContactsView(request):
    return render(request, 'app/contacts.html')


def PortfolioView(request):
    portfolios = PortfolioCard.objects.all()
    return render(request, 'app/portfolio.html', {'jobs': portfolios, })


def Email(request):
    phone = request.POST.get('phone', '')
    mail = request.POST.get('mail', '')
    message = request.POST.get('message', '')

    if (phone is not None) and (mail is not None) and (message is not None):
        new_request = Request(phone=phone, mail=mail, message=message)
        new_request.save()
        return render(request, 'app/success.html')
    else:
        return render(request, 'app/error.html')


def Requests(request):
    if request.user.is_authenticated:
        requests = Request.objects.all()
        return render(request, 'app/requests.html', {'requests': requests, })


def DeleteRequest(request, pk):
    if request.user.is_authenticated:
        new_request = get_object_or_404(Request, pk=pk)
        new_request.delete()
        requests = Request.objects.all()
        return render(request, 'app/requests.html', {'requests': requests, })
