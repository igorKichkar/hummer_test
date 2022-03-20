from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from .models import Profile
from .serializers import ProfileSerializer, AuthorizationCodeSerializer
from .utils import generate_random_digit_string


class Code(generics.CreateAPIView):
    authorization_code = generate_random_digit_string(4)
    queryset = Profile.objects.all()
    serializer_class = AuthorizationCodeSerializer

    def perform_create(self, serializer):
        serializer.save(authorization_code=self.authorization_code)

    def create(self, request, *args, **kwargs):
        profile = Profile.objects.filter(phone=request.data['phone'])
        if profile:
            authorization_code = generate_random_digit_string(4)
            a = Profile.objects.get(phone=request.data['phone'])
            a.authorization_code = authorization_code
            a.save()
            return Response({'phone': request.data['phone'], 'authorization_code': authorization_code})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
