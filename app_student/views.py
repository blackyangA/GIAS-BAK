#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
import logging

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from utils.permission import ReadOnly
from .models import StudentInfoModel, StudentSubjectAchievementModel, StudentOverallQualityModel, \
    StudentCourseDesignModel, StudentResultModel
from .serializers import StudentInfoSerializer, StudentSubjectAchievementSerializer, StudentOverallQualitySerializer, \
    StudentCourseDesignSerializer, StudentResultSerializer

logger = logging.getLogger(__name__)


class StudentInfoViewSet(ModelViewSet):
    """
    学生基本信息 API
    """
    serializer_class = StudentInfoSerializer
    queryset = StudentInfoModel.objects.all()
    permission_classes = [IsAdminUser | (ReadOnly & IsAuthenticated)]

    def get_queryset(self):
        """
        Determine if the user is admin, if yes return all, not then return rules with status 1
        """
        if self.request.user.is_staff:
            return StudentInfoModel.objects.all()
        s_id = self.request.user.s_id
        return StudentInfoModel.objects.filter(s_id=s_id)


class StudentSubjectAchievementViewSet(ModelViewSet):
    """
    学生学科成绩 API
    """
    serializer_class = StudentSubjectAchievementSerializer
    queryset = StudentSubjectAchievementModel.objects.all()
    permission_classes = [IsAdminUser | (ReadOnly & IsAuthenticated)]

    def get_queryset(self):
        """
        Determine if the user is admin, if yes return all, not then return rules with status 1
        """
        if self.request.user.is_staff:
            return StudentSubjectAchievementModel.objects.all()
        s_id = self.request.user.s_id
        return StudentSubjectAchievementModel.objects.filter(s_id=s_id)


class StudentOverallQualityViewSet(ModelViewSet):
    """
    学生综合素质成绩 API
    """
    serializer_class = StudentOverallQualitySerializer
    queryset = StudentOverallQualityModel.objects.all()
    permission_classes = [IsAdminUser | (ReadOnly & IsAuthenticated)]

    def get_queryset(self):
        """
        Determine if the user is admin, if yes return all, not then return rules with status 1
        """
        if self.request.user.is_staff:
            return StudentOverallQualityModel.objects.all()
        s_id = self.request.user.s_id
        return StudentOverallQualityModel.objects.filter(s_id=s_id)


class StudentCourseDesignViewSet(ModelViewSet):
    """
    学生课程设计 API
    """
    serializer_class = StudentCourseDesignSerializer
    queryset = StudentCourseDesignModel.objects.all()
    permission_classes = [IsAdminUser | (ReadOnly & IsAuthenticated)]

    def get_queryset(self):
        """
        Determine if the user is admin, if yes return all, not then return rules with status 1
        """
        if self.request.user.is_staff:
            return StudentCourseDesignModel.objects.all()
        s_id = self.request.user.s_id
        return StudentCourseDesignModel.objects.filter(s_id=s_id)


class ResultViewSet(ModelViewSet):
    """审核结果汇总"""
    serializer_class = StudentResultSerializer
    queryset = StudentResultModel.objects.all()
    permission_classes = [IsAdminUser | (ReadOnly & IsAuthenticated)]

    def get_queryset(self):
        """
        Determine if the user is admin, if yes return all, not then return rules with status 1
        """
        if self.request.user.is_staff:
            return StudentResultModel.objects.all()
        s_id = self.request.user.s_id
        return StudentResultModel.objects.filter(s_id=s_id)
