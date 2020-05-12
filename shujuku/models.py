from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(models.Model):
    job = (
        ('sheji', "设计人员"),
        ('jihua', "计划人员"),
        ('caigou', "采购人员"),
        ('shengchan', "生产人员"),
        ('zhijian', "质检人员"),
        ('kucun', "库存人员"),
    )

    name = models.CharField(max_length=128, unique=True, verbose_name="登录名")
    password = models.CharField(max_length=256, verbose_name="密码")
    work = models.CharField(max_length=32, choices=job, default="", verbose_name="职位")
    c_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class gongzuozhongxin(models.Model):
    name = models.CharField(max_length=128, verbose_name="工作中心名称")
    person = models.ManyToManyField('User')

    class Meta:
        verbose_name = "工作中心"


class wuliao(models.Model):
    wlcode = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, verbose_name="物料名称")

    class Meta:
        verbose_name = "物料"


class chanpin(models.Model):
    cpcode = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, verbose_name="产品名称")
    shuliang = models.IntegerField(verbose_name="工序数量")

    class Meta:
        verbose_name = "产品"


class chanpinBOM(models.Model):
    chanpin = models.ForeignKey(chanpin, on_delete=models.CASCADE, verbose_name="产品")
    cengji = models.IntegerField(verbose_name="层级")
    name = models.CharField(max_length=128, verbose_name="名称")
    shuliang = models.IntegerField(verbose_name="数量")

    class Meta:
        verbose_name = "产品BOM"


class gongyiluxian(models.Model):
    chanpin = models.ForeignKey(chanpin, on_delete=models.CASCADE, verbose_name="产品")
    wuliao = models.ForeignKey(wuliao, on_delete=models.CASCADE, verbose_name="物料")
    gongzuozhongxin = models.ForeignKey(gongzuozhongxin, on_delete=models.CASCADE, verbose_name="工作中心")
    gongxuhao = models.CharField(max_length=128, verbose_name="工序号")
    name = models.CharField(max_length=128, verbose_name="名称")
    shuliang = models.IntegerField(verbose_name="数量")
    time = models.IntegerField(verbose_name="加工时间")
    guanjiangongxu = models.BooleanField(default=False, verbose_name="是否为关键工序")

    class Meta:
        verbose_name = "工艺路线"


class dingdan(models.Model):
    chanpin = models.ForeignKey(chanpin, on_delete=models.CASCADE, verbose_name="产品")
    name = models.CharField(max_length=128, verbose_name="产品名称")
    shuliang = models.IntegerField(verbose_name="数量")
    kaishi = models.DateField(verbose_name="开始时间")
    jieshu = models.DateField(verbose_name="结束时间")

    class Meta:
        verbose_name = "订单"


class zhushengchan(models.Model):
    dingdan = models.ForeignKey(dingdan, on_delete=models.CASCADE, verbose_name="订单")
    name = models.CharField(max_length=128, verbose_name="名称")
    diyitian = models.IntegerField(verbose_name="第一天")
    diertian = models.IntegerField(verbose_name="第二天")
    disantian = models.IntegerField(verbose_name="第三天")
    disitian = models.IntegerField(verbose_name="第四天")
    diwutian = models.IntegerField(verbose_name="第五天")
    diliutian = models.IntegerField(verbose_name="第六天")
    diqitian = models.IntegerField(verbose_name="第七天")
    cunengli = models.BooleanField(default=False, verbose_name="粗能力分析")
    nenglixuqiu = models.BooleanField(default=False, verbose_name="能力需求分析")

    class Meta:
        verbose_name = "主生产计划"


class cunenglifenxi(models.Model):
    chanpin = models.ForeignKey(zhushengchan, on_delete=models.CASCADE, verbose_name="主生产计划")
    gongzuozhongxin = models.ForeignKey(gongzuozhongxin, on_delete=models.CASCADE, verbose_name="工作中心")
    name = models.CharField(max_length=128, verbose_name="产品名称")
    diyitian = models.IntegerField(verbose_name="第一天")
    diertian = models.IntegerField(verbose_name="第二天")
    disantian = models.IntegerField(verbose_name="第三天")
    disitian = models.IntegerField(verbose_name="第四天")
    diwutian = models.IntegerField(verbose_name="第五天")
    diliutian = models.IntegerField(verbose_name="第六天")
    diqitian = models.IntegerField(verbose_name="第七天")

    class Meta:
        verbose_name = "粗能力分析"


class wuliaoxuqiu(models.Model):
    chanpin = models.ForeignKey(zhushengchan, on_delete=models.CASCADE, verbose_name="主生产计划")
    chanpinBOM = models.ForeignKey(chanpinBOM, on_delete=models.CASCADE, verbose_name="产品BOM")
    name = models.CharField(max_length=128, verbose_name="工序名称")
    diyitian = models.IntegerField(verbose_name="第一天")
    diertian = models.IntegerField(verbose_name="第二天")
    disantian = models.IntegerField(verbose_name="第三天")
    disitian = models.IntegerField(verbose_name="第四天")
    diwutian = models.IntegerField(verbose_name="第五天")
    diliutian = models.IntegerField(verbose_name="第六天")
    diqitian = models.IntegerField(verbose_name="第七天")

    class Meta:
        verbose_name = "物料需求计划"


class nenglixuqiufenxi(models.Model):
    chanpin = models.ForeignKey(zhushengchan, on_delete=models.CASCADE, verbose_name="主生产计划")
    gongzuozhongxin = models.ForeignKey(gongzuozhongxin, on_delete=models.CASCADE, verbose_name="工作中心")
    name = models.CharField(max_length=128, verbose_name="工作中心")
    diyitian = models.IntegerField(verbose_name="第一天")
    diertian = models.IntegerField(verbose_name="第二天")
    disantian = models.IntegerField(verbose_name="第三天")
    disitian = models.IntegerField(verbose_name="第四天")
    diwutian = models.IntegerField(verbose_name="第五天")
    diliutian = models.IntegerField(verbose_name="第六天")
    diqitian = models.IntegerField(verbose_name="第七天")

    class Meta:
        verbose_name = "能力需求分析"


class paigongdan(models.Model):
    paigongcode = models.AutoField(primary_key=True)
    user = models.CharField(max_length=128, null=True, verbose_name="工作人员")
    name = models.CharField(max_length=128, verbose_name="物料名称")
    shuliang = models.IntegerField(verbose_name="数量")
    gongzuozhongxin = models.CharField(max_length=128, verbose_name="工作中心")
    kaishi = models.CharField(max_length=128, verbose_name="开始时间")
    jieshu = models.CharField(max_length=128, verbose_name="结束时间")
    jinqian = models.CharField(max_length=128, verbose_name="紧前派工单")
    jinhou = models.CharField(max_length=128, verbose_name="紧后派工单")
    lingliao = models.BooleanField(default=False, verbose_name="领料状态")
    zhijian = models.BooleanField(default=False, verbose_name="质检状态")
    zhuanyi = models.BooleanField(default=False, verbose_name="转移状态")
    dingdan = models.CharField(max_length=128, verbose_name="订单号")


    class Meta:
        verbose_name = "派工单"



class fuhe(models.Model):
    gongzuozhongxin = models.ForeignKey(gongzuozhongxin, on_delete=models.CASCADE, verbose_name="工作中心")
    diyitian = models.IntegerField(verbose_name="第一天", default=0)
    diertian = models.IntegerField(verbose_name="第二天", default=0)
    disantian = models.IntegerField(verbose_name="第三天", default=0)
    disitian = models.IntegerField(verbose_name="第四天", default=0)
    diwutian = models.IntegerField(verbose_name="第五天", default=0)
    diliutian = models.IntegerField(verbose_name="第六天", default=0)
    diqitian = models.IntegerField(verbose_name="第七天", default=0)

    class Meta:
        verbose_name = "工作中心负荷表"


class caigou(models.Model):
    name = models.CharField(max_length=128, verbose_name="物料名称")
    shuliang = models.IntegerField(verbose_name="数量")


    class Meta:
        verbose_name = "采购"


class daohuotongzhi(models.Model):
    caigou = models.CharField(max_length=128, verbose_name="采购单号")
    name = models.CharField(max_length=128, verbose_name="物料名称")
    shuliang = models.IntegerField(verbose_name="数量")

    class Meta:
        verbose_name = "到货通知"

class rukushenqingdan(models.Model):
    name = models.CharField(max_length=128, verbose_name="名称")
    shuliang = models.IntegerField(verbose_name="数量")
    work = models.CharField(max_length=128, verbose_name="操作人员")

    class Meta:
        verbose_name = "入库申请单"

class rukudan(models.Model):
    name = models.CharField(max_length=128, verbose_name="名称")
    shuliang = models.IntegerField(verbose_name="数量")
    work = models.CharField(max_length=128, verbose_name="操作人员")

    class Meta:
        verbose_name = "入库单"


class chukudan(models.Model):
    name = models.CharField(max_length=128, verbose_name="名称")
    shuliang = models.IntegerField(verbose_name="数量")
    work = models.CharField(max_length=128, verbose_name="操作人员")

    class Meta:
        verbose_name = "出库单"


class lingliaodan(models.Model):
    code = models.CharField(max_length=128, verbose_name="派工单号")
    name = models.CharField(max_length=128, verbose_name="名称")
    shuliang = models.IntegerField(verbose_name="数量")


    class Meta:
        verbose_name = "领料单"


class zhijiandan(models.Model):
    code = models.CharField(max_length=128, verbose_name="派工单号")
    hege = models.IntegerField(verbose_name="合格数量")
    buhege = models.IntegerField(verbose_name="不合格数量")
    work = models.CharField(max_length=128, verbose_name="操作人员")

    class Meta:
        verbose_name = "质检单"


class feiliaodan(models.Model):
    name = models.CharField(max_length=128, verbose_name="名称")
    shuliang = models.IntegerField(verbose_name="数量")
    work = models.CharField(max_length=128, verbose_name="操作人员")

    class Meta:
        verbose_name = "废料单"


class kucun(models.Model):
    name = models.CharField(max_length=128, verbose_name="名称")
    shuliang = models.IntegerField( verbose_name="数量")

    class Meta:
        verbose_name = "库存"

class gongxuzhuanyi(models.Model):
    name1 = models.CharField(max_length=128, verbose_name="转移前派工单")
    name2 = models.CharField(max_length=128, verbose_name="转移后派工单")

    class Meta:
        verbose_name = "工序转移"

class test(models.Model):
    name = models.CharField(max_length=128, verbose_name="物料名字")
    shuliang = models.IntegerField( verbose_name="数量")

    class Meta:
        verbose_name = "计算"
