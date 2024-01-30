from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'base_app/index.html')

def other(request):
    return render(request,'base_app/other.html')

def relative(request):
    return render(request,'base_app/relative_temp_urls.html')

def base(request):
    context_dict={"text":"hello world","number":100}
    return render(request,'base_app/base.html',context=context_dict)