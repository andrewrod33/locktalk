from tastypie.resources import ModelResource
from app.models import News,Teams
from tastypie import fields


class NewsResource(ModelResource):
    class Meta:
        queryset = News.objects.all()
        resource_name = 'news'

class TeamsResource(ModelResource):
    teams = fields.ManyToManyField(NewsResource,'news', full=True)
    class Meta:
        queryset = Teams.objects.all()
        resource_name = 'teams'

