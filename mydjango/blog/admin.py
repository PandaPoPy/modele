from django.contrib import admin
from .models import Article, Commentaire, Post, Comment

# Register your models here.
#class CommentaireInline(admin.StackedInline):
class CommentaireInline(admin.TabularInline):
    model = Commentaire
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    #fields = ['date_de_publication', 'texte']
    '''
    collapse permet en CSS de masquer et d'afficher la date de publication à la demande
    '''
    list_display = ['texte', 'date_de_publication', 'nombre_de_commentaires', 'recent']
    list_filter = ['date_de_publication']
    search_fields = ['texte', 'commentaire__commentaire']
    fieldsets = [
        ('Date de publication', {'fields': ['date_de_publication'], 'classes':['collapse']}),
        (None, {'fields': ['texte']}),
    ]
    inlines = [CommentaireInline]


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Commentaire)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
