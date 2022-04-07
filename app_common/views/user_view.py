#! /usr/bin/env python3.9
# -*- coding: utf8 -*-

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets

from app_main import permissions
from app_common.serializers import UserSerializer, GroupSerializer
from app_student.models import StudentSubjectAchievementModel, StudentOverallQualityModel, StudentCourseDesignModel, \
    StudentResultModel, StudentInfoModel

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Determine if the user is admin, if yes return all, not then return rules with status 1
        """
        print(self.request.user)
        if self.request.user.is_staff:
            return User.objects.all()
        s_id = self.request.user.s_id
        return User.objects.filter(s_id=s_id)

    def get_object(self):
        if self.kwargs['pk'] == 'me':
            return self.request.user
        return super(UserViewSet, self).get_object()

    def retrieve(self, request, *args, **kwargs):
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        print(f"data:{data}")
        s_id = data.get('s_id')
        print(f"s_id:{s_id}")
        if s_id:
            StudentInfoModel.objects.create(s_id=s_id)
            StudentSubjectAchievementModel.objects.create(s_id=s_id)
            StudentOverallQualityModel.objects.create(s_id=s_id)
            StudentCourseDesignModel.objects.create(s_id=s_id)
            StudentResultModel.objects.create(s_id=s_id)
        return super(UserViewSet, self).create(request, *args, **kwargs)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
