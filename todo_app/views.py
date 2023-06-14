from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.views import APIView
import jwt
from django.conf import settings
from rest_framework.response import Response
from .models import Tasks
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse('index')

def insert(request,userName,task,description,status):
    record=Tasks.objects.create(username=userName,task=task,description=description,status=status)
    record.save()
    response_data={"message":"insertion successfull"}
    return response_data

class DataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            token = request.META['HTTP_AUTHORIZATION'].split()[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            data = {"Userid":user_id}
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=401)



class Todo(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        try:
            response ={"WOW":"wow - 1"}
            Type = self.request.GET.get('type')
            userName = self.request.GET.get('userName')
            task = self.request.GET.get('task')
            status = self.request.GET.get('status')
            description = self.request.GET.get('description')


            return JsonResponse(response)
            
        except Exception as e:
            return Response({'error': str(e)})

    def post(self,request,*args,**kwargs):
        try:
            response ={"WOW":"wow - 1"}
            Type = self.request.GET.get('type')
            userName = self.request.GET.get('username')
            task = self.request.GET.get('task')
            status = self.request.GET.get('status')
            description = self.request.GET.get('description')
            uploaded_file = self.request.FILES.get('file')
            
            if Type == 'insert':
                response=insert(userName,task,description,status)

            return JsonResponse(response)
                
        except Exception as e:
            return Response({'error': str(e)})
