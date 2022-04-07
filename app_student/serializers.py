#! /usr/bin/env python3.9
# -*- coding: utf8 -*-

import logging

from rest_framework import serializers
from utils.audit_serializer import AuditSerializer
from .models import StudentInfoModel, StudentSubjectAchievementModel, StudentCourseDesignModel, \
    StudentOverallQualityModel, StudentResultModel
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


class StudentInfoSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = StudentInfoModel
        fields = '__all__'


class StudentSubjectAchievementSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = StudentSubjectAchievementModel
        fields = '__all__'


class StudentOverallQualitySerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = StudentOverallQualityModel
        fields = '__all__'


class StudentCourseDesignSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = StudentCourseDesignModel
        fields = '__all__'


class StudentResultSerializer(AuditSerializer, serializers.ModelSerializer):
    class Meta:
        model = StudentResultModel
        fields = '__all__'
