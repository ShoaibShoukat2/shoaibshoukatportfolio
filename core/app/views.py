from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')



def blogs(request):
    return render(request,'Blogs.html')



def djangoFirstApp(request):

    
    return render(request,'djangoFirstApp.html')



def eventsite(request):


    return render(request,'eventsite.html')


def FuiSite(request):
    return render(request,'fui.html')



# Website functons

def AISite(request):
    
    return render(request,'websites/AiSite.html')





