from django.shortcuts import render,redirect
from .models import product
from django.contrib import messages #メッセージ表示用

def product_create(request):
    if request.method == 'POST':
        # フォームからのデータを処理するロジックをここに追加
        name = request.POST['name']
        price_purchase = request.POST['purchase_price']
        price_selling = request.POST['selling_price']
        quantity = request.POST['quantity']
        # データベースに保存するなどの処理を行う
    
        # 未入力チェック
        if not price_purchase or not price_selling or not quantity:
            messages.error(request, '未入力の項目があります。')
            return render(request, 'product_create.html')

        item_product = product(
            name=name,
            price_purchase=price_purchase,
            price_selling=price_selling,
            quantity=quantity
        )

        # データベースに保存
        item_product.save()

        print("SAVE完了")

        messages.success(request, '商品が正常に作成されました。')

        # return redirect('/')
        return redirect('product_list')
    
    return render(request, 'product_create.html')


def product_list(request):
    items_product = product.objects.all()


    return render(request, 'product_list.html', {
        'items_product': items_product
    })


def product_update(request):
    return render(request, 'product_update.html', {})

