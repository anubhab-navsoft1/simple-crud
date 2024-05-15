from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from .models import SampleUser
from .serializers import SampleUSerSerializers
from .validation import EmailValidator
from .errorHandler import BadRequest
from django.db import transaction
# Create your views here.


class CreateSampleUser(generics. GenericAPIView):
    def post(self, request):
        try:
            with transaction.atomic():
                    data = request.data
                    name = data.get('name', '')
                    email = data.get('email', '')
                    age = data.get('age', '')
                    account = data.get('account', '')
                    
                    if SampleUser.objects.filter(email = email).exists():
                        return Response({"message" : 'Mail already exists'})
                    if not EmailValidator(email):
                        return Response({"error": "Email is not according to the requirements, An email must be contains alphanumeric values"}, status = status.HTTP_401_UNAUTHORIZED)
                    if age < 18 :
                        return Response({"error": "You are not adult"}, status =  status.HTTP_400_BAD_REQUEST)
                    user_data = {
                        'name' : name,
                        'email' : email,
                        'age' : age,
                        'account' : account
                    }
                    
                    serializer = SampleUSerSerializers(data = user_data)
                    if serializer.is_valid():
                        user_instance = serializer.save()
                        response = {
                            'id' : user_instance.id,
                            'name' : name,
                            'email' : email,
                            'age' : age,
                            'account' : account
                        }
                        return Response({
                            "message" : "You are registered", 
                            "data" : response
                        }, status = status.HTTP_201_CREATED)
                    return Response({"message" : serializer.errors}, status = 400)
        except Exception as e:
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          
     
class ListOfUsers(generics.GenericAPIView):
    
    def get(self, request):
        search_query = request.query_params.get('search', None)
        sort_by = request.query_params.get('sort_by', None)

        if search_query:
            users = SampleUser.objects.filter(name__icontains = search_query)
            user_count = users.count()
        else:
            users = SampleUser.objects.all()
            user_count = SampleUser.objects.count()

        if sort_by:
            users = SampleUser.order_by(sort_by)

        serializer = SampleUSerSerializers(users, many=True)
        return Response({"count": user_count, "data": serializer.data})
        