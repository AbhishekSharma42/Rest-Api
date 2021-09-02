from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse ,JsonResponse

# Create your views here.
def Student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializers(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data , content_type='application/json')
    return JsonResponse(serializer.data)
    

# Create your views here.
def Student_List(request):
    stu = Student.objects.all()
    serializer = StudentSerializers(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data , content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

