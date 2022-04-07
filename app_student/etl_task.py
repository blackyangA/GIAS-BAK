#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
import os
import time
import logging

import django
from pythonjsonlogger.jsonlogger import JsonFormatter

from app_main.settings import database
from django.contrib.auth import get_user_model
from utils.logging_utils import ThreadLocalLoggingHandler
from app_student.models import StudentSubjectAchievementModel, StudentOverallQualityModel, StudentCourseDesignModel, \
    StudentResultModel

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_main.settings")  # noqa
django.setup()  # noqa
logger = logging.getLogger(__name__)
local_logging_handler = ThreadLocalLoggingHandler()
local_logging_handler.setLevel(logging.INFO)
logging_fmt = JsonFormatter('%(name)s %(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s')
local_logging_handler.setFormatter(logging_fmt)
logger.addHandler(local_logging_handler)

"""此处可以添加复杂的判断程序 目前只加了最简单的判断方式 可以根据需求改动"""


def subject_achievement_judge_task(create_id, data_id=0):
    """学生学科成绩审核ETL程序"""

    if data_id == 0:
        return
    time.sleep(3)

    def extract():
        """取数据"""
        obj = StudentSubjectAchievementModel.objects.get(pk=data_id)
        data = dict()
        data['maths'] = obj.maths
        data['english'] = obj.english
        data['physics'] = obj.physics
        data['computer_networks'] = obj.computer_networks
        data['c_language'] = obj.c_language
        data['data_structure'] = obj.data_structure
        data['computer'] = obj.computer
        data['network_programming'] = obj.network_programming
        data['network_security'] = obj.network_security
        data['network_security'] = obj.network_security

        logger.info(f"学生学科成绩审核ETL程序:\n{data}")

        ret = {
            'data': data,
        }
        return ret

    def transform(extracted_data):
        """转换数据"""
        data = extracted_data['data']
        result = 1
        for k, v in data.items():
            if v is None:
                result = 3
                break
            if v < 60:
                result = 0
                break
        ret = {
            'result': result
        }
        return ret

    def load(transformed_data):
        """存储数据"""
        result = transformed_data['result']
        sql = f"update app_student_studentsubjectachievementmodel set result = {result} ,modified_by_id = {create_id} where id = {data_id};"
        database.execute_sql(sql)

    # E
    extracted_data = extract()
    # T
    transformed_dta = transform(extracted_data)
    # L
    load(transformed_dta)


def overall_quality_judge_task(create_id, data_id=0):
    """学生综合素质成绩审核ETL程序"""

    if data_id == 0:
        return

    time.sleep(3)

    def extract():
        """取数据"""
        obj = StudentOverallQualityModel.objects.get(pk=data_id)
        data = dict()
        data['community_activities'] = obj.community_activities
        data['sports'] = obj.sports
        data['physical_test'] = obj.physical_test
        data['computer_grade_exams'] = obj.computer_grade_exams
        data['english_grade_exams'] = obj.english_grade_exams

        logger.info(f"学生综合素质成绩审核ETL程序:\n{data}")

        ret = {
            'data': data
        }
        return ret

    def transform(extracted_data):
        """转换数据"""
        data = extracted_data['data']

        ret = {
            'result': 1
        }

        for k, v in data.items():
            if v is None:
                ret['result'] = 3
                return ret

        # 英语等级考试不过400分的直接审核不通过
        english_grade_exams = data['english_grade_exams']
        if english_grade_exams < 400:
            ret['result'] = 0
            return ret

        data.pop('english_grade_exams')
        total_grades = 0
        for k, v in data.items():
            total_grades += int(v)
        average_grades = total_grades // len(list(data.keys()))

        if average_grades < 60:
            ret['result'] = 0
            return ret

        return ret

    def load(transformed_data):
        """存储数据"""
        result = transformed_data['result']
        sql = f"update app_student_studentoverallqualitymodel set result={result} ,modified_by_id={create_id} where id={data_id};"
        database.execute_sql(sql)

    # E
    extracted_data = extract()
    # T
    transformed_data = transform(extracted_data)
    # L
    load(transformed_data)


def course_design_judge_task(create_id, data_id=0):
    """学生课程设计成绩审核ETL程序"""
    if data_id == 0:
        return

    time.sleep(3)

    def extract():
        """取数据"""
        obj = StudentCourseDesignModel.objects.get(pk=data_id)
        data = dict()
        data['linux'] = obj.linux
        data['c'] = obj.c
        data['java'] = obj.java
        data['python'] = obj.python
        data['web'] = obj.web
        data['graduation_design'] = obj.graduation_design

        logger.info(f"学生课程设计成绩审核ETL程序:\n{data}")

        ret = {
            'data': data
        }
        print(f"e_data:{ret}")
        return ret

    def transform(extracted_data):
        """转换数据"""
        data = extracted_data['data']
        result = 1
        for k, v in data.items():
            if v is None:
                result = 3
                break
            if v < 60:
                result = 0
                break
        ret = {
            'result': result
        }
        print(f"ret:{ret}")

        return ret

    def load(transformed_data):
        """存储数据"""
        result = transformed_data['result']
        sql = f"update app_student_studentcoursedesignmodel set result = {result}, modified_by_id={create_id} where id = {data_id};"
        database.execute_sql(sql)
        database.commit()
        pass

    # E
    extracted_data = extract()
    # T
    transformed_data = transform(extracted_data)
    # L
    load(transformed_data)


def final_result_judge_task(create_id, data_id=0):
    """学生最终成绩审核ETL程序"""
    if data_id == 0:
        return

    # 暂停8s等待数据落库（此处为异步任务）
    time.sleep(8)

    user_model = get_user_model()
    user = user_model.objects.get(pk=create_id)
    obj = StudentResultModel.objects.get(s_id=data_id)

    def extract():
        """取数据"""
        data = dict()

        subject_result = 3
        subject = StudentSubjectAchievementModel.objects.get(s_id=data_id)
        if subject:
            subject_result = subject.result
        data['subject_result'] = subject_result

        overall_result = 3
        overall = StudentOverallQualityModel.objects.get(s_id=data_id)
        if overall:
            overall_result = overall.result
        data['overall_result'] = overall_result

        design_result = 3
        design = StudentCourseDesignModel.objects.get(s_id=data_id)
        if design:
            design_result = design.result
        data['design_result'] = design_result

        logger.info(f"学生最终成绩审核ETL程序:\n{data}")

        ret = {
            'data': data
        }
        return ret

    def transform(extracted_data):
        """转换数据"""
        data = extracted_data['data']
        subject_result = data['subject_result']
        overall_result = data['overall_result']
        design_result = data['design_result']
        final_result = 3
        ret = {
            'subject_result': subject_result,
            'overall_result': overall_result,
            'design_result': design_result,
            'final_result': final_result,
        }
        if subject_result == 3 or overall_result == 3 or design_result == 3:
            return ret

        if subject_result == 1 and overall_result == 1 and design_result == 1:
            ret['final_result'] = 1
            return ret
        else:
            ret['final_result'] = 0
            return ret

    def load(transformed_data):
        """存储数据"""
        print(f"transformed_data:{transformed_data}")
        subject_result = transformed_data['subject_result']
        overall_result = transformed_data['overall_result']
        design_result = transformed_data['design_result']
        final_result = transformed_data['final_result']
        obj.subject_result = subject_result
        obj.overall_result = overall_result
        obj.design_result = design_result
        obj.final_result = final_result
        obj.save(current_user=user)

    # E
    extracted_data = extract()
    # T
    transformed_data = transform(extracted_data)
    # L
    load(transformed_data)


if __name__ == '__main__':
    pass
