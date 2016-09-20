# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager


# Create your models here.
class Article(models.Model):
    texte = models.TextField()
    date_de_publication = models.DateTimeField('date de publication')

    def __str__(self):
        return self.texte

    def nombre_de_commentaires(self):
        return self.commentaire_set.all().count()

    def recent(self):
        return self.date_de_publication >= timezone.now() - datetime.timedelta(days=1)
    recent.admin_order_field = 'date_de_publication'
    recent.boolean = True
    recent.short_description = u'Publié récemment ?'


class Commentaire(models.Model):
    article = models.ForeignKey(Article)
    commentaire = models.CharField(max_length=256)
    date_de_commentaire = models.DateTimeField('date de commentaire')
    plus_moins = models.IntegerField(default=0)

    def __str__(self):
        return self.commentaire + u'( de : '+ self.article.__str__() +u')'


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset() \
                                            .filter(status='published')


class DraftManager(models.Manager):
    def get_queryset(self):
        return super(DraftManager,self).get_queryset() \
                                            .filter(status='draft')


class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # with Manager
    objects = models.Manager() # the default manager
    published = PublishedManager() # our custom manager
    draft= DraftManager() # our custom manager
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args = [self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)