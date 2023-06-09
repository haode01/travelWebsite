import xadmin
from xadmin import views

from .models import *


class ProAdmin:
    """
    产品后台管理
    """
    list_display = ['name', 'price', 'num', 'freight', 'origin', 'pro_type', 'buyers', 'comments', 'add_time']
    list_filter = ['price', 'num', 'origin', 'pro_type', 'buyers', 'comments', 'add_time']
    search_fields = ['name', 'num', 'origin', 'pro_type', 'buyers', 'comments', 'add_time']
    list_display_links = ('name',)
    fields = ['name', 'price', 'num', 'freight', 'origin', 'pro_type', 'add_time']
    model_icon = 'fa fa-shopping-cart'
    readonly_fields = ['buyers', 'comments']
    style_fields = {"details": "ueditor"}


class ProPicAdmin:
    list_display = ['product', 'image', 'add_time']
    model_icon = 'fa fa-picture-o'


xadmin.site.register(Product, ProAdmin)
xadmin.site.register(ProPic, ProPicAdmin)