from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  # print('PREVIOUS URL:', request.META["HTTP_REFERER"])
  return render(request, 'index.html')



def new_survey(request):
  if request.method == "POST":
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    request.session['firstname'] = firstname
    request.session['lastname'] = lastname
    age= request.POST['age']
    location= request.POST['location']
    language= request.POST['language']
    comment= request.POST['comment']
    request.session['age'] = age
    request.session['location'] = location
    request.session['language'] = language
    request.session['comment'] = comment
   
    return redirect('/results')
  
def results(request):
    return render(request, 'results.html')

