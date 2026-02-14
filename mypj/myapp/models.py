from django.db import models

class product(models.Model):
    name = models.CharField(max_length=100)
    # 仕入価格 数値(小数点なし) 最大10桁 小数点以下0桁　例：1000 ※100.5は保存できません。
    price_purchase = models.DecimalField(max_digits=10,decimal_places=0)
    # 販売価格 数値(小数点なし) 最大10桁 小数点以下0桁　例：1500 ※150.5は保存できません。
    price_selling = models.DecimalField(max_digits=10,decimal_places=0)
    # 在庫数 0以上の整数 のみ保存可能
    quantity = models.PositiveIntegerField()
    # 売れた数値 初期値は 0 商品登録時は自動で0が入る ※登録時に入力不要のためフォームには表示しない
    quantity_sold = models.PositiveIntegerField(default=0)
 
    
