"""ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import  xadmin
from django.urls import path,re_path
from . import view

urlpatterns = [
    re_path(r'^$', view.deng_Lu),
    path('xadmin/', xadmin.site.urls),
    path('denglu', view.denglu, name="denglu"),
    path('wuliao_index', view.wuliao_index, name='wuliao_index'),
    path('wuliao_add', view.wuliao_add, name="wuliao_add"),
    path('wuliao_delete', view.wuliao_delete, name="wuliao_delete"),
    path('wuliao_modify', view.wuliao_modify, name="wuliao_modify"),
    path('chanpin_index', view.chanpin_index, name='chanpin_index'),
    path('chanpin_add', view.chanpin_add, name="chanpin_add"),
    path('chanpin_delete', view.chanpin_delete, name="chanpin_delete"),
    path('chanpin_modify', view.chanpin_modify, name="chanpin_modify"),
    path('chanpinBOM_index', view.chanpinBOM_index, name='chanpinBOM_index'),
    path('chanpinBOM_add', view.chanpinBOM_add, name="chanpinBOM_add"),
    path('chanpinBOM_delete', view.chanpinBOM_delete, name="chanpinBOM_delete"),
    path('chanpinBOM_modify', view.chanpinBOM_modify, name="chanpinBOM_modify"),
    path('gongyiluxian_index', view.gongyiluxian_index, name='gongyiluxian_index'),
    path('gongyiluxian_add', view.gongyiluxian_add, name="gongyiluxian_add"),
    path('gongyiluxian_delete', view.gongyiluxian_delete, name="gongyiluxian_delete"),
    path('gongyiluxian_modify', view.gongyiluxian_modify, name="gongyiluxian_modify"),
    path('dingdan_index', view.dingdan_index, name='dingdan_index'),
    path('dingdan_add', view.dingdan_add, name="dingdan_add"),
    path('dingdan_delete', view.dingdan_delete, name="dingdan_delete"),
    path('dingdan_modify', view.dingdan_modify, name="dingdan_modify"),
    path('zhushengchan_index', view.zhushengchan_index, name='zhushengchan_index'),
    path('zhushengchan_add', view.zhushengchan_add, name="zhushengchan_add"),
    path('zhushengchan_delete', view.zhushengchan_delete, name="zhushengchan_delete"),
    path('zhushengchan_modify', view.zhushengchan_modify, name="zhushengchan_modify"),
    path('cunengli_index', view.cunengli_index, name='cunengli_index'),
    path('cunengli_add', view.cunengli_add, name="cunengli_add"),
    path('cunengli_delete', view.cunengli_delete, name="cunengli_delete"),
    path('cunengli_modify', view.cunengli_modify, name="cunengli_modify"),
    path('wuliaoxuqiu_index', view.wuliaoxuqiu_index, name='wuliaoxuqiu_index'),
    path('wuliaoxuqiu_add', view.wuliaoxuqiu_add, name="wuliaoxuqiu_add"),
    path('wuliaoxuqiu_delete', view.wuliaoxuqiu_delete, name="wuliaoxuqiu_delete"),
    path('wuliaoxuqiu_modify', view.wuliaoxuqiu_modify, name="wuliaoxuqiu_modify"),
    path('nenglixuqiu_index', view.nenglixuqiu_index, name='nenglixuqiu_index'),
    path('nenglixuqiu_add', view.nenglixuqiu_add, name="nenglixuqiu_add"),
    path('nenglixuqiu_delete', view.nenglixuqiu_delete, name="nenglixuqiu_delete"),
    path('nenglixuqiu_modify', view.nenglixuqiu_modify, name="nenglixuqiu_modify"),
    path('paigong_index', view.paigong_index, name='paigong_index'),
    path('paigong_add', view.paigong_add, name="paigong_add"),
    path('paigong_delete', view.paigong_delete, name="paigong_delete"),
    path('paigong_modify', view.paigong_modify, name="paigong_modify"),
    path('scpaigong_index', view.scpaigong_index, name="scpaigong_index"),
    path('scpaigong_chaxun', view.scpaigong_chaxun, name="scpaigong_chaxun"),
    path('lingliao_index', view.lingliao_index, name='lingliao_index'),
    path('lingliao_add', view.lingliao_add, name="lingliao_add"),
    path('lingliao_delete', view.lingliao_delete, name="lingliao_delete"),
    path('zhijian_index', view.zhijian_index, name='zhijian_index'),
    path('zhijian_add', view.zhijian_add, name="zhijian_add"),
    path('zhijian_delete', view.zhijian_delete, name="zhijian_delete"),
    path('zz_index', view.zz_index, name='zz_index'),
    path('zz_modify', view.zz_modify, name="zz_modify"),
    path('zhuanyi_index', view.zhuanyi_index, name='zhuanyi_index'),
    path('zhuanyi_delete', view.zhuanyi_delete, name="zhuanyi_delete"),
    path('rukushengqing_index', view.rukushengqing_index, name='rukushengqing_index'),
    path('rukushengqing_delete', view.rukushengqing_delete, name="rukushengqing_delete"),
    path('kucun_index', view.kucun_index, name='kucun_index'),
    path('kucun_add', view.kucun_add, name="kucun_add"),
    path('kucun_delete', view.kucun_delete, name="kucun_delete"),
    path('kucun_modify', view.kucun_modify, name="kucun_modify"),
    path('kucunlingliao_index', view.kucunlingliao_index, name='kucunlingliao_index'),
    path('kucunlingliao_add', view.kucunlingliao_add, name="kucunlingliao_add"),
    path('ruku_index', view.ruku_index, name='ruku_index'),
    path('ruku_delete', view.ruku_delete, name="ruku_delete"),
    path('chuku_index', view.chuku_index, name='chuku_index'),
    path('chuku_delete', view.chuku_delete, name="chuku_delete"),
    path('kucunruku_index', view.kucunruku_index, name='kucunruku_index'),
    path('kucunruku_add', view.kucunruku_add, name="kucunruku_add"),
    path('caigou_index', view.caigou_index, name='caigou_index'),
    path('caigou_add', view.caigou_add, name="caigou_add"),
    path('caigou_delete', view.caigou_delete, name="caigou_delete"),
    path('daohuo_index', view.daohuo_index, name='daohuo_index'),
    path('daohuo_add', view.daohuo_add, name="daohuo_add"),
    path('daohuo_delete', view.daohuo_delete, name="daohuo_delete"),
]
