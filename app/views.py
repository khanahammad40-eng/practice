from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json 
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout,authenticate
from .models import Posts
from django.shortcuts import get_object_or_404
@method_decorator(csrf_exempt, name='dispatch')
class registerview(View):
    def post(self,request):
     print("aha")
     data=json.loads(request.body)
     username=data.get('username')
     password=data.get('password')
     if User.objects.filter(username=username).exists():
        return JsonResponse({"message":"user already presnet"})
     else:
        user=User.objects.create_user(username=username,password=password)   
        return JsonResponse({"message":"user authenticated sucessfully"},status=200)
@method_decorator(csrf_exempt, name='dispatch')        
class loginview(View):
    def post(self,request):
        data=json.loads(request.body)
        username=data.get('username')
        password=data.get('password')
        print("hello")
        user=authenticate(request,username=username,password=password)
        print("user is ",user)
        if user is None:
            return JsonResponse({"MESSAGE":"PLEASE REGISTER"})
        else:
            login(request,user)
            return JsonResponse({"MESSAGE":"LOGGED IN SUCESSFULLY"})
@method_decorator(csrf_exempt, name='dispatch')          
class postview(View):
    def post(self,request):
        data=json.loads(request.body)   
        name=data.get('name')
        description=data.get('description')
        email=data.get('email')
        post=Posts.objects.create(user=request.user,name=name,description=description,email=email)
        if post is not None:
            return JsonResponse({"name":post.name},status=200)
        else:
            return JsonResponse({"MESSAGE":"DONE"})    
    def get(self,request):
       posts= Posts.objects.filter(user=request.user) 
       post=list(posts.values())
       return JsonResponse({"MESSAGE":post},safe=False)
@method_decorator(csrf_exempt, name='dispatch')          
class postdetailview(View):
    def get(self,request,pk):
        posts=get_object_or_404(Posts,pk=pk)
        return JsonResponse({"MESSAGE":posts.name})
    def put(self,request,pk):
        posts=get_object_or_404(Posts,pk=pk)
        data=json.loads(request.body)
        posts.name=data.get('name',posts.name)
        posts.description=data.get('description',posts.description)
        posts.email=data.get('email',posts.email)
        posts.save()
        return JsonResponse({"MESSAGE":posts.name})   
    def delete(self,request,pk):
        posts=get_object_or_404(Posts,pk=pk)
        posts.delete()
        return JsonResponse({"MESSAGE":"MESSAGE DELETED"})





           
