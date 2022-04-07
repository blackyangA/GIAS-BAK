from django.db import models
from django_q.tasks import async_task
from utils.audit_model import FullAuditMixin
from django.utils.translation import gettext_lazy as _


class StudentInfoModel(FullAuditMixin):
    """
    学生信息表
    """

    class SexChoices(models.TextChoices):
        Man = ('男', _('男'))
        Woman = ('女', _('女'))

    class DataStatusChoices(models.IntegerChoices):
        ONE = (11, _('正常'))
        TWO = (12, _('删除'))

    s_id = models.CharField(_('学号'), max_length=4, db_index=True)
    s_name = models.CharField(_('姓名'), max_length=50, null=True)
    sex = models.CharField(_('性别'), max_length=10, null=True, choices=SexChoices.choices)
    ethnic = models.CharField(_('民族'), null=True, max_length=50)
    political_a = models.CharField(_('政治面貌'), null=True, max_length=50)
    homeland = models.CharField(_('生源地'), null=True, max_length=255)
    birthday = models.DateTimeField(_('生日'), null=True)
    id_no = models.CharField(_('身份证号'), null=True, max_length=50)
    qq = models.CharField(_('QQ号'), null=True, max_length=50)
    phone = models.CharField(_('电话号码'), null=True, max_length=50)
    data_status = models.IntegerField(_('数据状态'), null=True, default=11, choices=DataStatusChoices.choices)

    class Meta:
        ordering = ('s_id',)


class StudentSubjectAchievementModel(FullAuditMixin):
    """
    学生学科成绩表
    """

    class ResultChoices(models.TextChoices):
        one = (1, _('合格'))
        two = (0, _('不合格'))
        three = (2, _('待审核'))
        PendingUpload = (3, _('待上传'))

    s_id = models.CharField(_('学号'), max_length=4, db_index=True)
    maths = models.IntegerField(_('高等数学'), null=True)
    english = models.IntegerField(_('大学英语'), null=True)
    physics = models.IntegerField(_('大学物理'), null=True)
    computer_networks = models.IntegerField(_('计算机网络'), null=True)
    c_language = models.IntegerField(_('C语言'), null=True)
    data_structure = models.IntegerField(_('数据结构'), null=True)
    computer = models.IntegerField(_('计算机组成原理'), null=True)
    network_programming = models.IntegerField(_('网络编程'), null=True)
    network_security = models.IntegerField(_('网络安全'), null=True)
    result = models.IntegerField(_('是否合格'), default=2, null=True, choices=ResultChoices.choices)

    class Meta:
        ordering = ('s_id',)

    def save(self, *args, **kwargs):
        super(StudentSubjectAchievementModel, self).save(*args, **kwargs)
        self._create_async_task()
        self._create_final_result_task()

    def _create_async_task(self):
        """
        自动创建 后台任务
        :return:
        """
        task_id = async_task('app_student.etl_task.subject_achievement_judge_task', self.created_by.id, self.id)
        return task_id

    def _create_final_result_task(self):
        """
        自动创建 后台任务
        :return:
        """
        task_id = async_task('app_student.etl_task.final_result_judge_task', self.created_by.id, self.s_id)
        return task_id


class StudentOverallQualityModel(FullAuditMixin):
    """
    学生综合素质成绩表
    """

    class ResultChoices(models.TextChoices):
        one = (1, _('合格'))
        two = (0, _('不合格'))
        three = (2, _('待审核'))
        PendingUpload = (3, _('待上传'))

    s_id = models.CharField(_('学号'), max_length=4, db_index=True)
    community_activities = models.IntegerField(_("课外活动学分"), null=True)
    sports = models.IntegerField(_("体育成绩"), null=True)
    physical_test = models.IntegerField(_("身体素质测试"), null=True)
    computer_grade_exams = models.IntegerField(_("计算机等级考试"), null=True)
    english_grade_exams = models.IntegerField(_("英语等级考试"), null=True)
    result = models.IntegerField(_('是否合格'), default=2, choices=ResultChoices.choices, null=True)

    class Meta:
        ordering = ('s_id',)

    def save(self, *args, **kwargs):
        super(StudentOverallQualityModel, self).save(*args, **kwargs)
        self._create_async_task()
        self._create_final_result_task()

    def _create_async_task(self):
        """
        自动创建 后台任务
        :return:
        """
        task_id = async_task('app_student.etl_task.overall_quality_judge_task', self.created_by.id, self.id)
        return task_id

    def _create_final_result_task(self):
        """
        自动创建 后台任务
        :return:
        """
        task_id = async_task('app_student.etl_task.final_result_judge_task', self.created_by.id, self.s_id)
        return task_id


class StudentCourseDesignModel(FullAuditMixin):
    """
    学生课程设计成绩表
    """

    class ResultChoices(models.TextChoices):
        one = (1, _('合格'))
        two = (0, _('不合格'))
        three = (2, _('待审核'))
        PendingUpload = (3, _('待上传'))

    s_id = models.CharField(_('学号'), max_length=4, db_index=True)
    linux = models.IntegerField(_('linux课设'), null=True)
    c = models.IntegerField(_('c语言课设'), null=True)
    java = models.IntegerField(_('java课设'), null=True)
    python = models.IntegerField(_('python课设'), null=True)
    web = models.IntegerField(_('前端课设'), null=True)
    graduation_design = models.IntegerField(_('毕业设计'), null=True)
    result = models.IntegerField(_('是否合格'), default=2, null=True, choices=ResultChoices.choices)

    class Meta:
        ordering = ('s_id',)

    def save(self, *args, **kwargs):
        super(StudentCourseDesignModel, self).save(*args, **kwargs)
        self._create_async_task()
        self._create_final_result_task()

    def _create_async_task(self):
        """
        自动创建 后台任务
        :return:
        """
        task_id = async_task('app_student.etl_task.course_design_judge_task', self.created_by.id, self.id)
        return task_id

    def _create_final_result_task(self):
        """
        自动创建 后台任务
        :return:
        """
        task_id = async_task('app_student.etl_task.final_result_judge_task', self.created_by.id, self.s_id)
        return task_id


class StudentResultModel(FullAuditMixin):
    """
    最终审核结果表
    """

    class ResultChoices(models.TextChoices):
        one = (1, _('合格'))
        two = (0, _('不合格'))
        three = (2, _('待审核'))
        PendingUpload = (3, _('待上传'))

    class FinalResultChoices(models.TextChoices):
        Pass = (1, _('审核通过'))
        NoPass = (0, _('审核不通过'))
        PendingReview = (2, _('待审核'))
        PendingUpload = (3, _('成绩待上传'))

    s_id = models.CharField(_('学号'), max_length=4, db_index=True)
    subject_result = models.IntegerField(_('学生学科成绩审核结果'), default=2, null=True, choices=ResultChoices.choices)
    overall_result = models.IntegerField(_('学生综合素质审核结果'), default=2, null=True, choices=ResultChoices.choices)
    design_result = models.IntegerField(_('学生课程设计成绩审核结果'), default=2, null=True, choices=ResultChoices.choices)
    final_result = models.IntegerField(_('最终审核结果'), default=2, null=True, choices=FinalResultChoices.choices)

    class Meta:
        ordering = ('s_id',)
