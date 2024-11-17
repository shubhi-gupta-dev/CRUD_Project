from django.shortcuts import render ,redirect
from django.views import View
from .models import Product
from .forms import AddProductForm




# Create your views here.

# Home page View
class Home(View):
    def get(self , request):
        pro_data = Product.objects.all()
        return render(request , 'core/home.html' , {'prodata' : pro_data})
    

# Add Student View 
class Add_Product(View):
    def get(self,request):
        fm = AddProductForm()
        return render(request , 'core/add-product.html', {'form':fm})
    
    def post(self, request):
        fm = AddProductForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request , 'core/add-product.html', {'form':fm})
        
    
# Update view
class EditProduct(View):
    def get(self,request,id):
        prod = Product.objects.get(id=id)
        fm = AddProductForm(instance=prod)
        return render(request, 'core/edit-product.html' , {'form':fm})
   
    def post(self,request,id):
        prod = Product.objects.get(id=id)
        fm = AddProductForm(request.POST,instance=prod)
        if fm.is_valid():
            fm.save()
            return redirect('/')

        


# Delete View

class Delete_Product(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        prodata = Product.objects.get(id=id)
        prodata.delete()
        return redirect('/')