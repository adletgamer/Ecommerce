from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

def blog_thumbnail_directory(instance, filename):
    return 'blog/{0}/{1}'.format(instance.title, filename)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    views = models.IntegerField(default=0, blank=True)

    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_view_count(self):
        views = ViewCount.objects.filter(category=self).count()
        return views

    

    
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title =         models.CharField(max_length=255)
    slug =          models.SlugField(max_length=255, unique=True)
    thumbnail =     models.ImageField(upload_to=blog_thumbnail_directory, max_length=500)
    
    description =   models.TextField(max_length=255)
    content =       RichTextField()

    time_read =     models.IntegerField()

    published =     models.DateTimeField(default=timezone.now)
    views =         models.IntegerField(default=0, blank=True)

    status =        models.CharField(max_length=10, choices=options, default='draft')

    category =      models.ForeignKey(Category, on_delete=models.PROTECT)

    objects =           models.Manager()  # default manager
    postobjects =       PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_view_count(self):
        views = ViewCount.objects.filter(post=self).count()
        return views


class ViewCount(models.Model):
    category = models.ForeignKey(Category, related_name='category_view_count', on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=255)

    post = models.ForeignKey(Post, related_name='blogpost_view_count', on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address}"

