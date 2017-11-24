from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

# 公司部门
DEPARTMENTS = (
    (0, '营销部'),
    (1, '研发部'),
    (2, '后勤部'),
)


class UserProfile(AbstractUser):
    """
    用户信息表
    """
    avatar = models.ImageField(verbose_name=u'用户头像', upload_to='user/', default='default.jpg', help_text=u"用户头像")
    mobile = models.CharField(verbose_name=u"手机号",unique=True, max_length=11, help_text=u"手机号")
    part = models.IntegerField(verbose_name=u"所属部门", choices=DEPARTMENTS, help_text=u"所属部门")
    fav_article = models.IntegerField(verbose_name=u"用户收藏文章ID", null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = verbose_name = u"用户信息表"


class Announcement(models.Model):
    """
    公司信息公告
    """
    ANNOUN_TYPE = (
        (0, '福利'),
        (1, '假期安排'),
        (2, '活动'),
    )
    title = models.CharField(verbose_name=u'公告标题', max_length=150, help_text=u"公告标题")
    # 使用富文本改写
    content = models.TextField(verbose_name=u"公告内容", help_text=u"公告内容")
    announ_type = models.IntegerField(verbose_name=u"公告类型", choices=ANNOUN_TYPE, help_text=u"公告类型")
    create_time = models.DateTimeField(verbose_name=u'发布时间', auto_now_add=True, help_text=u"公告发布时间")
    is_published = models.BooleanField(verbose_name=u"是否发布", default=True, help_text=u"是否发布公告")
    update_time = models.DateTimeField(verbose_name=u"修改时间", auto_now=True, help_text=u"修改时间")
    # 发布人
    publisher = models.IntegerField(verbose_name=u"发布人ID", help_text=u"发布人ID")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = u"公司公告"
        ordering = ['create_time', 'update_time']


class Comments(models.Model):
    """
    留言
    """
    # 留言类型
    COMMENTS_TYPE = (
        (0, '公告留言'),
        (1, '博客留言'),
        (2, '用户私信留言')
    )
    comment_type = models.IntegerField(verbose_name=u"留言类型", help_text=u"留言类型")
    parent_id = models.IntegerField(verbose_name=u"所属类型ID", help_text=u"所属类型ID")
    content = models.TextField(verbose_name=u"留言内容", help_text=u"留言内容")
    create_time = models.DateTimeField(verbose_name=u"创建时间", auto_now_add=True)
    commenter = models.IntegerField(verbose_name=u"留言者ID", help_text=u"留言者ID")
    is_published = models.BooleanField(verbose_name=u"是否公开", default=True, help_text=u"是否公开")
    is_readed = models.BooleanField(verbose_name=u"是否被文章发布者阅读", default=False, help_text=u"是否被文章发布者阅读")

    class Meta:
        verbose_name_plural = verbose_name = u"留言信息"

    def __str__(self):
        return self.comment_type


class Article(models.Model):
    """
    博客文章
    """
    ARTICLE_TYPE = (
        (0, '技术'),
        (1, '生活'),
        (2, '杂谈')
    )
    article_type = models.IntegerField(verbose_name=u"文章类型", choices=ARTICLE_TYPE)
    title = models.CharField(verbose_name="博客标题", max_length=150, help_text=u"博客标题")
    tagname = models.CharField(verbose_name="文章标签", max_length=150, help_text=u"文章标签")
    content = models.TextField(verbose_name="文章正文", help_text=u"文章正文")
    author = models.IntegerField(verbose_name=u"作者ID", help_text=u"作者ID")
    is_published = models.BooleanField(verbose_name=u"是否公开", default=True, help_text=u"是否公开")
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"修改时间", auto_now=True)
    poll_num = models.IntegerField(u"文章点赞数", default=0)
    fav_num = models.IntegerField(u"文章收藏数", default=0)
    comment_num = models.IntegerField(u"文章评论数", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = u"文章信息表"


class DailyNews(models.Model):
    """
    每日新闻
    """
    title = models.CharField(verbose_name="新闻标题", max_length=255, help_text=u"新闻标题")
    news_link = models.CharField(verbose_name=u"新闻链接")
    create_time = models.DateField(verbose_name=u"创建时间", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = "新闻链接"
        ordering = ['create_time']




