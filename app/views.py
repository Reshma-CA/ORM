from django.shortcuts import render

# Create your views here.

from . models import Movieinfo
from .forms import MovieForm
# Create your views here.

def Movie(request):
    frm = MovieForm()
    if request.POST:
        title  = request.POST.get('title')
        year = request.POST.get('year')
        descr = request.POST.get('description')
        
        
        obj = Movieinfo(title=title, year=year, description=descr)
        obj.save() 

        ''' # Create and save a Movieinfo object if data is received
        if title and year and descr:
            obj = Movieinfo(title=title, year=year, description=descr)
            obj.save()
            # Optionally, you can redirect to a success page or render another template
            return render(request, 'success.html')'''
        if title and year and descr :
            return render(request, 'success.html')
        else:
            frm = MovieForm()

    return render(request, 'index.html',{'frm':frm})

      
def data_view(request):
    data_view = Movieinfo.objects.all()
    return render(request,'list.html',{'movies':data_view})

# This is a normal edit
# ******************************************
# def edit(request, id):
#     edit_obj = Movieinfo.objects.get(id=id)

#     if request.POST:
#         title = request.POST.get('title')
#         year = request.POST.get('year')
#         description = request.POST.get('description')
        
#         # Update object attributes
#         edit_obj.title = title
#         edit_obj.year = year
#         edit_obj.description = description
        
#         # Save changes to the database
#         edit_obj.save()

#         if title and year and description:
#             return render(request,'success.html')

#     frm = MovieForm(instance=edit_obj)
#     return render(request, 'index.html', {'frm': frm})

# This is a ModelForm based edit

def edit(request,id):
    edit_obj = Movieinfo.objects.get(id=id)
    if request.POST:
        frm = MovieForm(request.POST,instance = edit_obj)
        if frm.is_valid():
            edit_obj.save()

            
    else:
        frm = MovieForm(instance = edit_obj)
    return render(request,'index.html',{'frm':frm})

def delete(request,id):
    delete_obj = Movieinfo.objects.get(id = id)
    delete_obj.delete()
    data_view = Movieinfo.objects.all()
    return render(request,'list.html',{'movies':data_view})