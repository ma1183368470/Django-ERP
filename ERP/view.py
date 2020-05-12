from django.shortcuts import render
import json
from shujuku.models import *


# Create your views here.

def deng_Lu(request):
    pass
    # 登陆管理
    return render(request, "login.html")


def denglu(request):
    # 用户登录后跳转页面
    username = request.POST.get("username")
    userpassword = request.POST.get("userpassword")
    response = User.objects.filter(name=username, password=userpassword)
    request.session['username'] = username
    if response:
        for i in response:
            zhiwei = i.work
            mingzi = i.name
            if zhiwei == 'sheji':
                return render(request, "base-sheji.html", {'name': mingzi})
            elif zhiwei == 'jihua':
                return render(request, "base-jihua.html", {'name': mingzi})
            elif zhiwei == 'caigou':
                return render(request, "base-caigou.html", {'name': mingzi})
            elif zhiwei == 'shengchan':
                return render(request, "base-shengchan.html", {'name': mingzi})
            elif zhiwei == 'zhijian':
                return render(request, "base-zhijian.html", {'name': mingzi})
            elif zhiwei == 'kucun':
                return render(request, "base-kucun.html", {'name': mingzi})
    else:
        return 0


def wuliao_index(request):
    wuliao_list = wuliao.objects.all()
    return render(request, 'sheji-wuliao.html', {"wuliao_list": wuliao_list})

def wuliao_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        wlcode = request.POST.get('wlcode')
        name = request.POST.get('name')
        this_wl = wuliao(wlcode=wlcode, name=name)
        this_wl.save()
        this_ts = test(name=name, shuliang=0)
        this_ts.save()
    return render(request, 'sheji-wuliao.html')


def wuliao_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        wuliao.objects.filter(wlcode=aa).delete()
    return render(request, 'sheji-wuliao.html')


def wuliao_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        busCode2 = request.POST.get('busCode2')
        busLicense = request.POST.get('busLicense')
        wuliao.objects.filter(wlcode=busCode).update(wlcode=busCode2, name=busLicense)
    return render(request, 'sheji-wuliao.html')


def chanpin_index(request):
    chanpin_list = chanpin.objects.all()
    return render(request, 'sheji-chanpin.html', {"chanpin_list": chanpin_list})

def chanpin_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        wlcode = request.POST.get('cpcode')
        name = request.POST.get('name')
        shuliang = request.POST.get('shuliang')
        this_cp = chanpin(cpcode=wlcode, name=name, shuliang=shuliang)
        this_cp.save()
    return render(request, 'sheji-chanpin.html')


def chanpin_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        chanpin.objects.filter(cpcode=aa).delete()
    return render(request, 'sheji-chanpin.html')


def chanpin_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        busCode2 = request.POST.get('busCode2')
        busLicense = request.POST.get('busLicense')
        length = request.POST.get('shuliang')
        chanpin.objects.filter(cpcode=busCode).update(cpcode=busCode2, name=busLicense, shuliang=length)
    return render(request, 'sheji-chanpin.html')


def chanpinBOM_index(request):
    chanpinBOM_list = chanpinBOM.objects.all()
    chanpin_list = chanpin.objects.all()
    return render(request, 'sheji-chanpinBOM.html', {"chanpinBOM_list": chanpinBOM_list, "chanpin_list": chanpin_list})

def chanpinBOM_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        xuanze = request.POST.get('xuanze')
        cp = chanpin.objects.get(name=xuanze)
        name = request.POST.get('name')
        shuliang = request.POST.get('shuliang')
        cengji = request.POST.get('cengji')
        this_cp = chanpinBOM(chanpin=cp, name=name, shuliang=shuliang, cengji=cengji)
        this_cp.save()
    return render(request, 'sheji-chanpinBOM.html')


def chanpinBOM_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        chanpinBOM.objects.filter(id=aa).delete()
    return render(request, 'sheji-chanpinBOM.html')


def chanpinBOM_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        xuanze = request.POST.get('xuanze')
        cp = chanpin.objects.get(name=xuanze)
        gongxu = request.POST.get('gongxu')
        length = request.POST.get('shuliang')
        cengji = request.POST.get('cengji')
        chanpinBOM.objects.filter(id=busCode).update(chanpin=cp, name=gongxu, shuliang=length, cengji=cengji)
    return render(request, 'sheji-chanpinBOM.html')


def gongyiluxian_index(request):
    gongyiluxian_list = gongyiluxian.objects.all()
    wuliao_list = wuliao.objects.all()
    chanpin_list = chanpin.objects.all()
    gongzuozhongxin_list = gongzuozhongxin.objects.all()
    return render(request, 'sheji-gongyiluxian.html', {"gongyiluxian_list": gongyiluxian_list, "chanpin_list": chanpin_list, "wuliao_list": wuliao_list, "gongzuozhongxin_list": gongzuozhongxin_list})

def gongyiluxian_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        gongxuhao = request.POST.get('gongxuhao')
        xuanze = request.POST.get('xuanze')
        cp = chanpin.objects.get(name=xuanze)
        xuanze2 = request.POST.get('xuanze2')
        zhongxin = gongzuozhongxin.objects.get(name=xuanze2)
        name = request.POST.get('name')
        xuanze3 = request.POST.get('xuanze3')
        wl = wuliao.objects.get(name=xuanze3)
        shuliang = request.POST.get('shuliang')
        shijian = request.POST.get('time')
        guanjiangongxu = request.POST.get('xuanze4')
        this_cp = gongyiluxian(gongxuhao=gongxuhao, chanpin=cp, gongzuozhongxin=zhongxin, name=name, wuliao=wl, shuliang=shuliang, time=shijian, guanjiangongxu=guanjiangongxu)
        this_cp.save()
    return render(request, 'sheji-gongyiluxian.html')


def gongyiluxian_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        gongyiluxian.objects.filter(id=aa).delete()
    return render(request, 'sheji-gongyiluxian.html')


def gongyiluxian_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        gongxuhao = request.POST.get('gongxuhao')
        xuanze = request.POST.get('xuanze')
        cp = chanpin.objects.get(name=xuanze)
        xuanze2 = request.POST.get('xuanze2')
        zhongxin = gongzuozhongxin.objects.get(name=xuanze2)
        name = request.POST.get('name')
        xuanze3 = request.POST.get('xuanze3')
        wl = wuliao.objects.get(name=xuanze3)
        shuliang = request.POST.get('shuliang')
        shijian = request.POST.get('time')
        guanjiangongxu = request.POST.get('xuanze4')
        gongyiluxian.objects.filter(id=busCode).update(gongxuhao=gongxuhao, chanpin=cp, gongzuozhongxin=zhongxin, name=name, wuliao=wl, shuliang=shuliang, time=shijian, guanjiangongxu=guanjiangongxu)
    return render(request, 'sheji-gongyiluxian.html')


def dingdan_index(request):
    dingdan_list = dingdan.objects.all()
    chanpin_list = chanpin.objects.all()
    return render(request, 'jihua-dingdan.html', {"dingdan_list": dingdan_list, "chanpin_list": chanpin_list})

def dingdan_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        xuanze = request.POST.get('xuanze')
        cp = chanpin.objects.get(name=xuanze)
        shuliang = request.POST.get('shuliang')
        kaishishijian = request.POST.get('ks')
        jieshushijian = request.POST.get('js')
        this_cp = dingdan(chanpin=cp, name=cp.name, shuliang=shuliang, kaishi=kaishishijian, jieshu=jieshushijian)
        this_cp.save()
    return render(request, 'jihua-dingdan.html')


def dingdan_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        dingdan.objects.filter(id=aa).delete()
    return render(request, 'jihua-dingdan.html')


def dingdan_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        xuanze = request.POST.get('xuanze')
        cp = chanpin.objects.get(name=xuanze)
        shuliang = request.POST.get('shuliang')
        kaishishijian = request.POST.get('ks')
        jieshushijian = request.POST.get('js')
        dingdan.objects.filter(id=busCode).update(chanpin=cp, name=cp.name, shuliang=shuliang, kaishi=kaishishijian, jieshu=jieshushijian)
    return render(request, 'jihua-dingdan.html')


def zhushengchan_index(request):
    dingdan_list = dingdan.objects.all()
    zhushengchan_list = zhushengchan.objects.all()
    return render(request, 'jihua-zhushengchan.html', {"dingdan_list": dingdan_list, "zhushengchan_list": zhushengchan_list})

def zhushengchan_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        xuanze = request.POST.get('xuanze')
        dd = dingdan.objects.get(id=xuanze)
        a = int((dd.jieshu-dd.kaishi).days) + 1
        b = int(dd.shuliang)/a
        diyi = dier = disan = disi = diwu = diliu = diqi = int(0)
        if a == 1:
            diyi = b
        elif a == 2:
            diyi = dier = b
        elif a == 3:
            diyi = dier = disan = b
        elif a == 4:
            diyi = dier = disan = disi = b
        elif a == 5:
            diyi = dier = disan = disi = diwu = b
        elif a == 6:
            diyi = dier = disan = disi = diwu = diliu = b
        elif a == 7:
            diyi = dier = disan = disi = diwu = diliu = diqi = b
        this_cp = zhushengchan(dingdan=dd, name=dd.name, diyitian=diyi, diertian=dier, disantian=disan, disitian=disi, diwutian=diwu, diliutian=diliu, diqitian=diqi, cunengli=False, nenglixuqiu=False)
        this_cp.save()
    return render(request, 'jihua-zhushengchan.html')


def zhushengchan_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        zhushengchan.objects.filter(id=aa).delete()
    return render(request, 'jihua-zhushengchan.html')


def zhushengchan_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        xuanze = request.POST.get('xuanze')
        dd = dingdan.objects.get(id=xuanze)
        d1 = request.POST.get('diyi')
        d2 = request.POST.get('dier')
        d3 = request.POST.get('disan')
        d4 = request.POST.get('disi')
        d5 = request.POST.get('diwu')
        d6 = request.POST.get('diliu')
        d7 = request.POST.get('diqi')
        cnl = request.POST.get('xuanze2')
        xnl = request.POST.get('xuanze3')
        zhushengchan.objects.filter(id=busCode).update(dingdan=dd, name=dd.name, diyitian=d1, diertian=d2, disantian=d3, disitian=d4, diwutian=d5, diliutian=d6, diqitian=d7, cunengli=cnl, nenglixuqiu=xnl)
    return render(request, 'jihua-zhushengchan.html')


def cunengli_index(request):
    cunengli_list = cunenglifenxi.objects.all()
    zhushengchan_list = zhushengchan.objects.all()
    return render(request, 'jihua-cunengli.html', {"cunengli_list": cunengli_list, "zhushengchan_list": zhushengchan_list})

def cunengli_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        xuanze = request.POST.get('xuanze')
        zsc = zhushengchan.objects.get(id=xuanze)
        cp = chanpin.objects.get(name=zsc.name)
        jisuan = gongyiluxian.objects.get(chanpin=cp, guanjiangongxu=True)
        gzzx = fuhe.objects.get(gongzuozhongxin=jisuan.gongzuozhongxin)
        i = gzzx
        this_cp = cunenglifenxi(chanpin=zsc, gongzuozhongxin=i.gongzuozhongxin, name=zsc.name, diyitian=i.diyitian, diertian=i.diertian, disantian=i.disantian, disitian=i.disitian, diwutian=i.diwutian, diliutian=i.diliutian, diqitian=i.diqitian)
        this_cp.save()
        shijian = jisuan.time
        di1 = zsc.diyitian * shijian + gzzx.diyitian
        di2 = zsc.diertian * shijian + gzzx.diertian
        di3 = zsc.disantian * shijian + gzzx.disantian
        di4 = zsc.disitian * shijian + gzzx.disitian
        di5 = zsc.diwutian * shijian + gzzx.diwutian
        di6 = zsc.diliutian * shijian + gzzx.diliutian
        di7 = zsc.diqitian * shijian + gzzx.diqitian
        if di1 < 24 and di2 < 24 and di3 < 24 and di1 < 24 and di1 < 24 and di1 < 24 and di1 < 24 and di1 < 24:
            zhushengchan.objects.filter(id=zsc.id).update(cunengli=True)
        a = cunenglifenxi.objects.get(chanpin=zsc, gongzuozhongxin=gzzx.gongzuozhongxin)
        cunenglifenxi.objects.filter(id=a.id).update(diyitian=di1, diertian=di2, disantian=di3, disitian=di4, diwutian=di5, diliutian=di6, diqitian=di7)
    return render(request, 'jihua-cunengli.html')


def cunengli_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        cunenglifenxi.objects.filter(id=aa).delete()
    return render(request, 'jihua-cunengli.html')


def cunengli_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        d1 = request.POST.get('diyi')
        d2 = request.POST.get('dier')
        d3 = request.POST.get('disan')
        d4 = request.POST.get('disi')
        d5 = request.POST.get('diwu')
        d6 = request.POST.get('diliu')
        d7 = request.POST.get('diqi')
        cunenglifenxi.objects.filter(id=busCode).update(diyitian=d1, diertian=d2, disantian=d3, disitian=d4, diwutian=d5, diliutian=d6, diqitian=d7)
    return render(request, 'jihua-cunengli.html')


def wuliaoxuqiu_index(request):
    wuliaoxuqiu_list = wuliaoxuqiu.objects.all()
    zhushengchan_list = zhushengchan.objects.all()
    return render(request, 'jihua-wuliaoxuqiu.html', {"wuliaoxuqiu_list": wuliaoxuqiu_list, "zhushengchan_list": zhushengchan_list})

def wuliaoxuqiu_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        xuanze = request.POST.get('xuanze')
        zsc = zhushengchan.objects.get(id=xuanze)
        cp = chanpin.objects.get(name=zsc.name)
        bom = chanpinBOM.objects.filter(chanpin=cp)
        for i in bom:
            jisuan = i.shuliang
            di1 = zsc.diyitian * jisuan
            di2 = zsc.diertian * jisuan
            di3 = zsc.disantian * jisuan
            di4 = zsc.disitian * jisuan
            di5 = zsc.diwutian * jisuan
            di6 = zsc.diliutian * jisuan
            di7 = zsc.diqitian * jisuan
            this_cp = wuliaoxuqiu(chanpin=zsc, chanpinBOM=i, name=i.name, diyitian=di1, diertian=di2, disantian=di3, disitian=di4, diwutian=di5, diliutian=di6, diqitian=di7)
            this_cp.save()
    return render(request, 'jihua-wuliaoxuqiu.html')


def wuliaoxuqiu_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        wuliaoxuqiu.objects.filter(id=aa).delete()
    return render(request, 'jihua-wuliaoxuqiu.html')


def wuliaoxuqiu_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        d1 = request.POST.get('diyi')
        d2 = request.POST.get('dier')
        d3 = request.POST.get('disan')
        d4 = request.POST.get('disi')
        d5 = request.POST.get('diwu')
        d6 = request.POST.get('diliu')
        d7 = request.POST.get('diqi')
        wuliaoxuqiu.objects.filter(id=busCode).update(diyitian=d1, diertian=d2, disantian=d3, disitian=d4, diwutian=d5, diliutian=d6, diqitian=d7)
    return render(request, 'jihua-wuliaoxuqiu.html')


def nenglixuqiu_index(request):
    nenglixuqiu_list = nenglixuqiufenxi.objects.all()
    zhushengchan_list = zhushengchan.objects.all()
    return render(request, 'jihua-nenglixuqiu.html', {"nenglixuqiu_list": nenglixuqiu_list, "zhushengchan_list": zhushengchan_list})

def nenglixuqiu_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        xuanze = request.POST.get('xuanze')
        zsc = zhushengchan.objects.get(id=xuanze)
        cp = chanpin.objects.get(name=zsc.name)
        jisuan = gongyiluxian.objects.filter(chanpin=cp)
        gz = fuhe.objects.all()
        for i in gz:
            this_cp = nenglixuqiufenxi(chanpin=zsc, gongzuozhongxin=i.gongzuozhongxin, name=i.gongzuozhongxin.name, diyitian=i.diyitian, diertian=i.diertian, disantian=i.disantian, disitian=i.disitian, diwutian=i.diwutian, diliutian=i.diliutian, diqitian=i.diqitian)
            this_cp.save()
        for j in jisuan:
            a = j.time
            bom = wuliaoxuqiu.objects.get(chanpin=zsc, name=j.name)
            gzzx = nenglixuqiufenxi.objects.get(chanpin=zsc, gongzuozhongxin=j.gongzuozhongxin)
            di1 = bom.diyitian * a + gzzx.diyitian
            di2 = bom.diertian * a + gzzx.diertian
            di3 = bom.disantian * a + gzzx.disantian
            di4 = bom.disitian * a + gzzx.disitian
            di5 = bom.diwutian * a + gzzx.diwutian
            di6 = bom.diliutian * a + gzzx.diliutian
            di7 = bom.diqitian * a + gzzx.diqitian
            if di1 < 24 and di2 < 24 and di3 < 24 and di1 < 24 and di1 < 24 and di1 < 24 and di1 < 24 and di1 < 24:
                zhushengchan.objects.filter(id=zsc.id).update(nenglixuqiu=True)
            nenglixuqiufenxi.objects.filter(id=gzzx.id).update(diyitian=di1, diertian=di2, disantian=di3, disitian=di4, diwutian=di5, diliutian=di6, diqitian=di7)
    return render(request, 'jihua-nenglixuqiu.html')


def nenglixuqiu_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        nenglixuqiufenxi.objects.filter(id=aa).delete()
    return render(request, 'jihua-nenglixuqiu.html')


def nenglixuqiu_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        d1 = request.POST.get('diyi')
        d2 = request.POST.get('dier')
        d3 = request.POST.get('disan')
        d4 = request.POST.get('disi')
        d5 = request.POST.get('diwu')
        d6 = request.POST.get('diliu')
        d7 = request.POST.get('diqi')
        nenglixuqiufenxi.objects.filter(id=busCode).update(diyitian=d1, diertian=d2, disantian=d3, disitian=d4, diwutian=d5, diliutian=d6, diqitian=d7)
    return render(request, 'jihua-nenglixuqiu.html')


def paigong_index(request):
    paigong_list = paigongdan.objects.all()
    zhushengchan_list = zhushengchan.objects.all()
    User_list = User.objects.filter(work="shengchan")
    return render(request, 'jihua-paigong.html', {"paigong_list": paigong_list, "zhushengchan_list": zhushengchan_list, "User_list": User_list})

def paigong_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        xuanze = request.POST.get('xuanze')
        zsc = zhushengchan.objects.get(id=xuanze)
        mingzi = zsc.name
        cp = chanpin.objects.get(name=mingzi)
        paixu = gongyiluxian.objects.filter(chanpin=cp).order_by("gongxuhao")
        month = zsc.dingdan.kaishi.month
        day = zsc.dingdan.kaishi.day
        if zsc.cunengli == True and zsc.nenglixuqiu == True:
            for j in range(6):
                if j == 0:
                    if zsc.diyitian != 0:
                        for i in paixu:
                            str = '{0}{1}{2}'.format(zsc.id, j, i.gongxuhao)
                            code = int(str)
                            bom = chanpinBOM.objects.get(name=i.name)
                            sl = bom.shuliang * i.shuliang
                            if int(i.gongxuhao) == 1:
                                jinq = "null"
                                zy = True
                            else:
                                k = int(i.gongxuhao) - 1
                                str2 = '{0}{1}{2}'.format(zsc.id, j, k)
                                code2 = int(str2)
                                jinq = code2
                                zy = False
                            if int(i.gongxuhao) < cp.shuliang:
                                l = int(i.gongxuhao) + 1
                                str3 = '{0}{1}{2}'.format(zsc.id, j, l)
                                code3 = int(str3)
                                jinh = code3
                            else:
                                jinh = "null"
                            gzzx = fuhe.objects.get(gongzuozhongxin=i.gongzuozhongxin)
                            ks = gzzx.diyitian
                            ks1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 1, ks)
                            js = ks + bom.shuliang * i.time
                            js1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 1, js)
                            this_cp = paigongdan(paigongcode=code, user='null', shuliang=sl, name=i.wuliao.name, gongzuozhongxin=gzzx.gongzuozhongxin.name,
                                                 kaishi=ks1, jieshu=js1, jinqian=jinq, jinhou=jinh, lingliao=False, zhijian=False, zhuanyi=zy, dingdan=zsc.dingdan.id)
                            this_cp.save()
                            fuhe.objects.filter(gongzuozhongxin=i.gongzuozhongxin).update(diyitian=js)
                elif j ==1:
                    if zsc.diertian != 0:
                        for i in paixu:
                            str = '{0}{1}{2}'.format(zsc.id, j, i.gongxuhao)
                            code = int(str)
                            bom = chanpinBOM.objects.get(name=i.name)
                            sl = bom.shuliang * i.shuliang
                            if int(i.gongxuhao) == 1:
                                jinq = "null"
                                zy = True
                            else:
                                k = int(i.gongxuhao) - 1
                                str2 = '{0}{1}{2}'.format(zsc.id, j, k)
                                code2 = int(str2)
                                jinq = code2
                                zy = False
                            if int(i.gongxuhao) < cp.shuliang:
                                l = int(i.gongxuhao) + 1
                                str3 = '{0}{1}{2}'.format(zsc.id, j, l)
                                code3 = int(str3)
                                jinh = code3
                            else:
                                jinh = "null"
                            gzzx = fuhe.objects.get(gongzuozhongxin=i.gongzuozhongxin)
                            ks = gzzx.diertian
                            ks1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 2, ks)
                            js = ks + bom.shuliang * i.time
                            js1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 2, js)
                            this_cp = paigongdan(paigongcode=code, user='null', shuliang=sl, name=i.wuliao.name,
                                                 gongzuozhongxin=gzzx.gongzuozhongxin.name,
                                                 kaishi=ks1, jieshu=js1, jinqian=jinq, jinhou=jinh, lingliao=False,
                                                 zhijian=False, zhuanyi=zy, dingdan=zsc.dingdan.id)
                            this_cp.save()
                            fuhe.objects.filter(gongzuozhongxin=i.gongzuozhongxin).update(diertian=js)
                elif j ==2:
                    if zsc.disantian != 0:
                        for i in paixu:
                            str = '{0}{1}{2}'.format(zsc.id, j, i.gongxuhao)
                            code = int(str)
                            bom = chanpinBOM.objects.get(name=i.name)
                            sl = bom.shuliang * i.shuliang
                            if int(i.gongxuhao) == 1:
                                jinq = "null"
                                zy = True
                            else:
                                k = int(i.gongxuhao) - 1
                                str2 = '{0}{1}{2}'.format(zsc.id, j, k)
                                code2 = int(str2)
                                jinq = code2
                                zy = False
                            if int(i.gongxuhao) < cp.shuliang:
                                l = int(i.gongxuhao) + 1
                                str3 = '{0}{1}{2}'.format(zsc.id, j, l)
                                code3 = int(str3)
                                jinh = code3
                            else:
                                jinh = "null"
                            gzzx = fuhe.objects.get(gongzuozhongxin=i.gongzuozhongxin)
                            ks = gzzx.disantian
                            ks1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 3, ks)
                            js = ks + bom.shuliang * i.time
                            js1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 3, js)
                            this_cp = paigongdan(paigongcode=code, user='null', shuliang=sl, name=i.wuliao.name,
                                                 gongzuozhongxin=gzzx.gongzuozhongxin.name,
                                                 kaishi=ks1, jieshu=js1, jinqian=jinq, jinhou=jinh, lingliao=False,
                                                 zhijian=False, zhuanyi=zy, dingdan=zsc.dingdan.id)
                            this_cp.save()
                            fuhe.objects.filter(gongzuozhongxin=i.gongzuozhongxin).update(disantian=js)
                elif j ==3:
                    if zsc.disitian != 0:
                        for i in paixu:
                            str = '{0}{1}{2}'.format(zsc.id, j, i.gongxuhao)
                            code = int(str)
                            bom = chanpinBOM.objects.get(name=i.name)
                            sl = bom.shuliang * i.shuliang
                            if int(i.gongxuhao) == 1:
                                jinq = "null"
                                zy = True
                            else:
                                k = int(i.gongxuhao) - 1
                                str2 = '{0}{1}{2}'.format(zsc.id, j, k)
                                code2 = int(str2)
                                jinq = code2
                                zy = False
                            if int(i.gongxuhao) < cp.shuliang:
                                l = int(i.gongxuhao) + 1
                                str3 = '{0}{1}{2}'.format(zsc.id, j, l)
                                code3 = int(str3)
                                jinh = code3
                            else:
                                jinh = "null"
                            gzzx = fuhe.objects.get(gongzuozhongxin=i.gongzuozhongxin)
                            ks = gzzx.disitian
                            ks1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 4, ks)
                            js = ks + bom.shuliang * i.time
                            js1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 4, js)
                            this_cp = paigongdan(paigongcode=code, user='null', shuliang=sl, name=i.wuliao.name,
                                                 gongzuozhongxin=gzzx.gongzuozhongxin.name,
                                                 kaishi=ks1, jieshu=js1, jinqian=jinq, jinhou=jinh, lingliao=False,
                                                 zhijian=False, zhuanyi=zy, dingdan=zsc.dingdan.id)
                            this_cp.save()
                            fuhe.objects.filter(gongzuozhongxin=i.gongzuozhongxin).update(disitian=js)
                elif j ==4:
                    if zsc.diwutian != 0:
                        for i in paixu:
                            str = '{0}{1}{2}'.format(zsc.id, j, i.gongxuhao)
                            code = int(str)
                            bom = chanpinBOM.objects.get(name=i.name)
                            sl = bom.shuliang * i.shuliang
                            if int(i.gongxuhao) == 1:
                                jinq = "null"
                                zy = True
                            else:
                                k = int(i.gongxuhao) - 1
                                str2 = '{0}{1}{2}'.format(zsc.id, j, k)
                                code2 = int(str2)
                                jinq = code2
                                zy = False
                            if int(i.gongxuhao) < cp.shuliang:
                                l = int(i.gongxuhao) + 1
                                str3 = '{0}{1}{2}'.format(zsc.id, j, l)
                                code3 = int(str3)
                                jinh = code3
                            else:
                                jinh = "null"
                            gzzx = fuhe.objects.get(gongzuozhongxin=i.gongzuozhongxin)
                            ks = gzzx.diwutian
                            ks1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 5, ks)
                            js = ks + bom.shuliang * i.time
                            js1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 5, js)
                            this_cp = paigongdan(paigongcode=code, user='null', shuliang=sl, name=i.wuliao.name,
                                                 gongzuozhongxin=gzzx.gongzuozhongxin.name,
                                                 kaishi=ks1, jieshu=js1, jinqian=jinq, jinhou=jinh, lingliao=False,
                                                 zhijian=False, zhuanyi=zy, dingdan=zsc.dingdan.id)
                            this_cp.save()
                            fuhe.objects.filter(gongzuozhongxin=i.gongzuozhongxin).update(diwutian=js)
                elif j ==5:
                    if zsc.diliutian != 0:
                        for i in paixu:
                            str = '{0}{1}{2}'.format(zsc.id, j, i.gongxuhao)
                            code = int(str)
                            bom = chanpinBOM.objects.get(name=i.name)
                            sl = bom.shuliang * i.shuliang
                            if int(i.gongxuhao) == 1:
                                jinq = "null"
                                zy = True
                            else:
                                k = int(i.gongxuhao) - 1
                                str2 = '{0}{1}{2}'.format(zsc.id, j, k)
                                code2 = int(str2)
                                jinq = code2
                                zy = False
                            if int(i.gongxuhao) < cp.shuliang:
                                l = int(i.gongxuhao) + 1
                                str3 = '{0}{1}{2}'.format(zsc.id, j, l)
                                code3 = int(str3)
                                jinh = code3
                            else:
                                jinh = "null"
                            gzzx = fuhe.objects.get(gongzuozhongxin=i.gongzuozhongxin)
                            ks = gzzx.diliutian
                            ks1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 6, ks)
                            js = ks + bom.shuliang * i.time
                            js1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 6, js)
                            this_cp = paigongdan(paigongcode=code, user='null', shuliang=sl, name=i.wuliao.name,
                                                 gongzuozhongxin=gzzx.gongzuozhongxin.name,
                                                 kaishi=ks1, jieshu=js1, jinqian=jinq, jinhou=jinh, lingliao=False,
                                                 zhijian=False, zhuanyi=zy, dingdan=zsc.dingdan.id)
                            this_cp.save()
                            fuhe.objects.filter(gongzuozhongxin=i.gongzuozhongxin).update(diliutian=js)
                elif j ==6:
                    if zsc.diqitian != 0:
                        for i in paixu:
                            str = '{0}{1}{2}'.format(zsc.id, j, i.gongxuhao)
                            code = int(str)
                            bom = chanpinBOM.objects.get(name=i.name)
                            sl = bom.shuliang * i.shuliang
                            if int(i.gongxuhao) == 1:
                                jinq = "null"
                                zy = True
                            else:
                                k = int(i.gongxuhao) - 1
                                str2 = '{0}{1}{2}'.format(zsc.id, j, k)
                                code2 = int(str2)
                                jinq = code2
                                zy = False
                            if int(i.gongxuhao) < cp.shuliang:
                                l = int(i.gongxuhao) + 1
                                str3 = '{0}{1}{2}'.format(zsc.id, j, l)
                                code3 = int(str3)
                                jinh = code3
                            else:
                                jinh = "null"
                            gzzx = fuhe.objects.get(gongzuozhongxin=i.gongzuozhongxin)
                            ks = gzzx.diqitian
                            ks1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 7, ks)
                            js = ks + bom.shuliang * i.time
                            js1 = '{0}-{1}-{2}'.format(zsc.dingdan.kaishi.month, 7, js)
                            this_cp = paigongdan(paigongcode=code, user='null', shuliang=sl, name=i.wuliao.name,
                                                 gongzuozhongxin=gzzx.gongzuozhongxin.name,
                                                 kaishi=ks1, jieshu=js1, jinqian=jinq, jinhou=jinh, lingliao=False,
                                                 zhijian=False, zhuanyi=zy, dingdan=zsc.dingdan.id)
                            this_cp.save()
                            fuhe.objects.filter(gongzuozhongxin=i.gongzuozhongxin).update(diqitian=js)
        return render(request, 'jihua-paigong.html')
    else:
        return render(request, 'jihua-paigong-shibai.html')

def paigong_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        paigongdan.objects.filter(paigongcode=aa).delete()
    return render(request, 'jihua-paigong.html')


def paigong_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        xuanze = request.POST.get('xuanze2')
        paigongdan.objects.filter(paigongcode=busCode).update(user=xuanze)
    return render(request, 'jihua-paigong.html')

def scpaigong_index(request):
    scpaigong_list = paigongdan.objects.all()
    return render(request, 'shengchan-paigong.html', {"scpaigong_list": scpaigong_list})

def scpaigong_chaxun(request):
    if request.method == 'POST':
        aa = request.POST.get("three")
        pgchaxun_list = paigongdan.objects.filter(user=aa)
    return render(request, 'shengchan-paigongchaxun.html', {"pgchaxun_list": pgchaxun_list})


def lingliao_index(request):
    lingliao_list = lingliaodan.objects.all()
    paigong_list = paigongdan.objects.all()
    return render(request, 'shengchan-lingliao.html', {"lingliao_list": lingliao_list, "paigong_list": paigong_list})

def lingliao_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        xuanze = request.POST.get('xuanze')
        pg = paigongdan.objects.get(paigongcode=xuanze)
        if pg.zhuanyi==True:
            this_cp = lingliaodan(code=pg.paigongcode, name=pg.name, shuliang=pg.shuliang)
            this_cp.save()
            paigongdan.objects.filter(paigongcode=pg.paigongcode).update(lingliao=True)
            return render(request, 'shengchan-lingliao.html')
        else:
            return render(request, 'shengchan-lingliao-shibai.html')


def lingliao_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        lingliaodan.objects.filter(id=aa).delete()
    return render(request, 'shengchan-lingliao.html')


def zhijian_index(request):
    zhijian_list = zhijiandan.objects.all()
    paigong_list = paigongdan.objects.all()
    return render(request, 'shengchan-zhijian.html', {"zhijian_list": zhijian_list, "paigong_list": paigong_list})

def zhijian_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        xuanze = request.POST.get('xuanze')
        pg = paigongdan.objects.get(paigongcode=xuanze)
        this_cp = zhijiandan(code=pg.paigongcode, hege=0, buhege=0, work="null")
        this_cp.save()
        paigongdan.objects.filter(paigongcode=pg.paigongcode).update(zhijian=True)
    return render(request, 'shengchan-zhijian.html')


def zhijian_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        zhijiandan.objects.filter(id=aa).delete()
    return render(request, 'shengchan-zhijian.html')


def zz_index(request):
    zhijian_list = zhijiandan.objects.all()
    return render(request, 'zhijian-zhijian.html', {"zhijian_list": zhijian_list})

def zz_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        hg1 = request.POST.get('hg')
        hg = int(hg1)
        bhg1 = request.POST.get('bhg')
        bhg = int(bhg1)
        qm = request.POST.get('qianming')
        zhijiandan.objects.filter(id=busCode).update(hege=hg, buhege=bhg, work=qm)
        zz = zhijiandan.objects.get(id=busCode)
        pg = paigongdan.objects.get(paigongcode=zz.code)
        if int(bhg) > 0:
            str = '{0}{1}'.format(pg.name,"废料")
            this_cp = feiliaodan(name=str, shuliang=bhg, work=qm)
            this_cp.save()
            this_sq = rukushenqingdan(name=str, shuliang=bhg, work=qm)
            this_sq.save()
        if pg.jinhou =="null":
            dd = dingdan.objects.get(id=pg.dingdan)
            this_rk = rukushenqingdan(name=dd.name, shuliang=dd.shuliang, work=qm)
            this_rk.save()
        else:
            this_zy = gongxuzhuanyi(name1=pg.paigongcode,name2=pg.jinhou)
            this_zy.save()
            paigongdan.objects.filter(paigongcode=pg.jinhou).update(zhuanyi=True)

    return render(request, 'zhijian-zhijian.html')


def zhuanyi_index(request):
    zhuanyi_list = gongxuzhuanyi.objects.all()
    return render(request, 'zhijian-zhuanyi.html', {"zhuanyi_list": zhuanyi_list})

def zhuanyi_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        gongxuzhuanyi.objects.filter(id=aa).delete()
    return render(request, 'zhijian-zhuanyi.html')

def rukushengqing_index(request):
    rukushengqing_list = rukushenqingdan.objects.all()
    return render(request, 'zhijian-rukushengqing.html', {"rukushengqing_list": rukushengqing_list})

def rukushengqing_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        rukushenqingdan.objects.filter(id=aa).delete()
    return render(request, 'zhijian-rukushengqing.html')


def kucun_index(request):
    kucun_list = kucun.objects.all()
    return render(request, 'kucun-kucun.html', {"kucun_list": kucun_list})

def kucun_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        wlcode = request.POST.get('code')
        sl1 = request.POST.get('sl')
        this_wl = kucun(name=wlcode, shuliang=sl1)
        this_wl.save()
    return render(request, 'kucun-kucun.html')

def kucun_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        kucun.objects.filter(id=aa).delete()
    return render(request, 'kucun-kucun.html')


def kucun_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        busCode2 = request.POST.get('busCode2')
        busLicense = request.POST.get('busLicense')
        kucun.objects.filter(id=busCode).update(name=busCode2, shuliang=busLicense)
    return render(request, 'kucun-kucun.html')


def kucunlingliao_index(request):
    lingliao_list = lingliaodan.objects.all()
    return render(request, 'kucun-lingliao.html', {"lingliao_list": lingliao_list})

def kucunlingliao_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        llcode = request.POST.get('xuanze')
        ll = int(llcode)
        mz = request.POST.get('qianming')
        jisuan = lingliaodan.objects.get(id=ll)
        this_wl = chukudan(name=jisuan.name, shuliang=jisuan.shuliang, work=mz)
        this_wl.save()
        abc = kucun.objects.get(name=jisuan.name)
        c = abc.shuliang
        d = jisuan.shuliang
        b = c - d
        kucun.objects.filter(name=jisuan.name).update(shuliang=b)
        lingliaodan.objects.filter(id=ll).delete()
    return render(request, 'kucun-lingliao.html')


def ruku_index(request):
    ruku_list = rukudan.objects.all()
    return render(request, 'kucun-rukudan.html', {"ruku_list": ruku_list})

def ruku_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        rukudan.objects.filter(id=aa).delete()
    return render(request, 'kucun-rukudan.html')

def chuku_index(request):
    chuku_list = chukudan.objects.all()
    return render(request, 'kucun-chukudan.html', {"chuku_list": chuku_list})

def chuku_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        chukudan.objects.filter(id=aa).delete()
    return render(request, 'kucun-chukudan.html')


def kucunruku_index(request):
    rukushenqing_list = rukushenqingdan.objects.all()
    return render(request, 'kucun-kucunruku.html', {"rukushenqing_list": rukushenqing_list})

def kucunruku_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        llcode = request.POST.get('xuanze')
        ll = int(llcode)
        mz = request.POST.get('qianming')
        jisuan = rukushenqingdan.objects.get(id=ll)
        this_wl = rukudan(name=jisuan.name, shuliang=jisuan.shuliang, work=mz)
        this_wl.save()
        abc = kucun.objects.get(name=jisuan.name)
        c = abc.shuliang
        d = jisuan.shuliang
        b = c + d
        kucun.objects.filter(name=jisuan.name).update(shuliang=b)
        rukushenqingdan.objects.filter(id=ll).delete()
    return render(request, 'kucun-kucunruku.html')



def caigou_index(request):
    caigou_list = caigou.objects.all()
    zhushengchan_list = zhushengchan.objects.all()
    return render(request, 'caigou-caigou.html', {"caigou_list": caigou_list, "zhushengchan_list": zhushengchan_list})

def caigou_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        xuanze = request.POST.get('xuanze')
        zsc = zhushengchan.objects.get(id=xuanze)
        wlxq = wuliaoxuqiu.objects.filter(chanpin=zsc)
        for i in wlxq:
            a = i.diyitian + i.diertian + i.disantian + i.disitian + i.diwutian +i.diliutian + i.diqitian
            gylx = gongyiluxian.objects.get(name=i.name)
            c =  a * gylx.shuliang
            cs = test.objects.get(name=gylx.wuliao.name)
            d = cs.shuliang + c
            test.objects.filter(name=gylx.wuliao.name).update(shuliang=d)
        jisuan = test.objects.all()
        for j in jisuan:
            aaa = kucun.objects.get(name=j.name)
            if aaa.shuliang < j.shuliang:
                bbb = j.shuliang - aaa.shuliang
                this_wl = caigou(name=j.name, shuliang=bbb)
                this_wl.save()
                test.objects.filter(name=j.name).update(shuliang=0)
    return render(request, 'caigou-caigou.html')

def caigou_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        caigou.objects.filter(id=aa).delete()
    return render(request, 'caigou-caigou.html')


def daohuo_index(request):
    daohuo_list = daohuotongzhi.objects.all()
    caigou_list = caigou.objects.all()
    return render(request, 'caigou-daohuo.html', {"daohuo_list": daohuo_list, "caigou_list": caigou_list})

def daohuo_add(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        xuanze = request.POST.get('xuanze')
        mz = request.POST.get('qianming')
        cg = caigou.objects.get(id=xuanze)
        this_wl = daohuotongzhi(name=cg.name, shuliang=cg.shuliang)
        this_wl.save()
        this_sq = rukushenqingdan(name=cg.name, shuliang=cg.shuliang, work=mz)
        this_sq.save()
    return render(request, 'caigou-daohuo.html')

def daohuo_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        daohuotongzhi.objects.filter(id=aa).delete()
    return render(request, 'caigou-daohuo.html')