from rest_framework import viewsets, permissions
from django.shortcuts import render, get_object_or_404
from projects.models import (
    Profile,
    Project,
    CertifyingInstitution,
    Certificate)
from projects.serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertifyingInstitutionSerializer,
    CertificateSerializer)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs.get('pk'))
        return render(request, 'profile_detail.html', {'profile': profile})


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]
