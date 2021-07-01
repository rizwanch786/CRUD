
from api.models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print(python_data)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id = id)
            print(stu)
            # creating serializer object
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'applictaion/json')
    
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            M = {
                'msg': 'Data Inserted Sucessfully'
            }
            json_data = JSONRenderer().render(M)
            return HttpResponse(json_data, content_type = 'application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type = 'application/json')
    
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data = python_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            M = {
                'msg': 'Data Updated Sucessfully'
            }
            json_data = JSONRenderer().render(M)
            return HttpResponse(json_data, content_type = 'application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type = 'application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        M = {
                'msg': 'Data Deleted Sucessfully'
            }
        json_data = JSONRenderer().render(M)
        return HttpResponse(json_data, content_type = 'application/json')


