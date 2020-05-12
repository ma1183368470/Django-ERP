# -*- coding: utf-8 -*-
import xadmin
from .models import User, gongzuozhongxin, fuhe


class UserAdmin(object):
    pass


class gongzuozhongxinAdmin(object):
    style_fields = {'person': 'm2m_transfer'}

class fuheAdmin(object):
    pass

xadmin.site.register(User, UserAdmin)
xadmin.site.register(gongzuozhongxin, gongzuozhongxinAdmin)
xadmin.site.register(fuhe, fuheAdmin)
