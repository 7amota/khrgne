from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, status , mixins  , viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes 
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from .serializers import *
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from .models import *




class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data )
        if serializer.is_valid():
            serializer.save()
            token = Token.objects.get(user=serializer.instance)
            response = {
            "status":1,
            "message": "User Created Successfully",
             "data": serializer.data ,
            "token":token.key
             }
            return Response(data=response, status=status.HTTP_201_CREATED)
        message = {
            "status":0,
            "message": "some thing went wrong ! ",
             "data": serializer.errors ,
            }
            
        return Response(message, status=status.HTTP_400_BAD_REQUEST)




class LoginView(generics.ListCreateAPIView):
    permission_classes = []
    serializer_class=AuthTokenSerializer

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:

            tokens, created = Token.objects.get_or_create(user=user)
            response = {
                "status":1,
                "message": "Login Successfull",
                "id": tokens.user_id,
                "token": tokens.key
            }
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)




class UpdateUser(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        TokenAuthentication.keyword = None
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user ,data=request.data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
                return Response({
                    "status":0,
                    "message":"some thing went wrong"
                }, status=status.HTTP_200_OK)
        
        response = {
            "status" : 1,
            "data":serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

        


class SliderBaseView(viewsets.ModelViewSet):
    queryset = Slider.objects.order_by('?')[:5]
    serializer_class = SliderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        response = {
            "message" : "method POST/CREATE work in admin panel"
        }
        return Response(response , status.HTTP_200_OK)
    def update(self, request, *args, **kwargs):
            response = {
                "message" : "method PUT/UPDATE work in admin panel"
            }
            return Response(response , status.HTTP_200_OK)
    def delete(self, request, *args, **kwargs):
            response = {
                "message" : "method DELETE work in admin panel"
            }
            return Response(response , status.HTTP_200_OK)
    
    



class UserImage(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user , data=request.FILES,context={"request": 
                      request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status.HTTP_200_OK)
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user
        ,context={"request":request} 
        )
        response = {
            "status" : 1,
            "data" : serializer.data
        }
        return Response(response, status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user , data=request.FILES, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            "status": 1,
            "message": "updated successfully",
            "data":serializer.data
        }
        return Response(serializer.data , status.HTTP_200_OK)




class Profile(generics.RetrieveAPIView):
    # queryset = Token.objects.all()
    
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = User.objects.get(email=request.user)
        token = Token.objects.get(user=user)
        serializer = self.serializer_class(user
        ,context={"request": request}
        
        )
        return Response(
            {
                "status":1,
                "data":serializer.data,
                "token":token.key,
                
            }
        )




class Logout(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
         request.user.auth_token.delete()
         response = {
             "status" : 1,
             "message":"user is gone ):"
         }
         return Response(response , status.HTTP_410_GONE)




class GetItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    def get(self, request, *args, **kwargs):

        item = Item.objects.all()
        serializer = self.serializer_class(item , many=True, context={"request": request})
        response = {
            'items' : serializer.data,

        }
        return Response(response, status.HTTP_200_OK)




class Addview(generics.CreateAPIView):
    queryset = View.objects.all()
    serializer_class = ViewsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
       
            item = Item.objects.get(pk=request.data["itemid"]) 
            viewsl = request.data['view']
            user = request.user
            
            view = View.objects.create(user=user , item=item , views=viewsl)
            data = ViewsSerializer(view, many=False)
            json = {
                    'status': 1,
                    'message':"created successfully",
                    'data':data.data

                }
            return Response(json , status.HTTP_200_OK)




class Addrate(generics.ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
           item = Item.objects.get(id=request.data["itemid"])
           stars = request.data['stars']
           user = request.user
           try:
                print(request.user)

                rate = Rate.objects.get(user=user.id , item=item.id)
                rate.rate = stars
                rate.save()
                serializerupdate = RateSerializer(rate , many=False)
                json = {
                    'message' : 'updated',
                    'data': serializerupdate.data
                }
                return Response(json, status.HTTP_200_OK)

            
           except:
                print(request.user)
                createrate = Rate.objects.create(
                    item=item , user=user , rate=stars
                )
                serializer = RateSerializer(createrate, many=False)
                jsonr = {
                    'message' : 'created',
                    'data' : serializer.data
                }
                return Response(jsonr, status=status.HTTP_200_OK)
    def get(self, request, *args, **kwargs):
        rat = Rate.objects.get(user=request.user , item = request.data["itemid"])
        serializer = self.serializer_class(rat)
        json = {
            "status":1,
            "data":serializer.data
        }
        return Response(json, status.HTTP_200_OK)




class Fav(generics.ListCreateAPIView):
    queryset = FavList.objects.all()
    serializer_class = FavSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        item = request.data["itemid"]
        user = request.user
        try:
            get = self.queryset.get(item=item , user=user)
            if get:
                get.delete()
            
            j = {
                "status":1,
                "message":"item deleted successfully"
            }
            return Response(j, status.HTTP_200_OK)
        except:
            getitem = Item.objects.get(id=item)
            create = self.queryset.create(user=user , item=getitem)
            data = self.serializer_class(create)
            
            json = {
                "status":1,
                "message":"item created successfully",
                "data":data.data,
            }
            return Response(json,status.HTTP_200_OK)

         

