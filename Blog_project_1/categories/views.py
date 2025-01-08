from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST': #user post request krche
        category_form = forms.CategoryFrom(request.POST)  #user er post request data ekhane captute krlm

        if category_form.is_valid():  #post kora data gula valid kina ekhane check krbo
          category_form.save() #jodi data valid hoy taile database a save krbo
          return redirect('add_category')   #sob thik thkle takee add category te pathai dibo
    
    else:  #user normally website a gele blank form pabe
        category_form = forms.CategoryFrom()
    return render(request, 'add_category.html' , {'form' : category_form}) 