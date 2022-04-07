#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'student', views.StudentInfoViewSet)
router.register(r'subject', views.StudentSubjectAchievementViewSet)
router.register(r'overall', views.StudentOverallQualityViewSet)
router.register(r'design', views.StudentCourseDesignViewSet)
router.register(r'result', views.ResultViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
