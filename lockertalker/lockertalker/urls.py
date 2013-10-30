from django.conf.urls import patterns, include, url
from tastypie.api import Api
from app.api.resources import NewsResource,TeamsResource

v1_api=Api(api_name='v1')
v1_api.register(NewsResource())
v1_api.register(TeamsResource())

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('app.views',
    url(r'^add-teams$', 'espn_ids_views.get_espn'),#add teams on espn
    # Examples:
    url(r'^add-news$', 'espn_news_views.get_news'),
    url(r'^add-br$', 'br_views.get_br1'),
    url(r'^add-source','sources_views.get_sources'),
    url(r'^settings$', 'settings_views.prefs'),
    url(r'^settings/sources$', 'settings_views.set_sources'),
    #url(r'^usersettings/$', 'user_settings_views.user'),
    url(r'^home$', 'home_views.home'),
    url(r'^login', 'login_views.login'),
    url(r'^facebook/$', 'facebook_views.facebook'),
    url(r'^sources$', 'news_sources_views.teams_sources'),
    #url(r'^prefs$', 'prefs_views.get_prefs'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^twilio$', 'twil.twilio'),
    # url(r'^$', 'lockertalker.views.home', name='home'),
    # url(r'^lockertalker/', include('lockertalker.foo.urls')),
    # url(r'^index$',, name= 'home' ),#index
    # url(r'^main$',', name = 'main')#main - feed_page/main
    # url()#settings/edit edit settings
    # url()#settings view settings
    # url()#favorite/NEWS_ITEM_ID
    # url()#block/NEWS_ITEM_IDs
    #      more/NEWS_SOURCE_ID
           #less/NEWS_SOURCE_ID
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
