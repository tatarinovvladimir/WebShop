from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Item, DayItem, Order
from django.conf import settings
from django.core.mail import send_mail
from .forms import OrderForm
import datetime as dt


def clothes(request):
    catalog = Item.objects.filter().order_by('price')
    if 'cart' in request.COOKIES:
        cart = request.COOKIES['cart']
    else:
        cart = 0

    if 'item_list' in request.COOKIES:
        item_list = request.COOKIES['item_list']
    else:
        item_list = ''

    if request.POST:

        response = HttpResponseRedirect(request.path)
        if int(cart):
            cart = int(cart, base=10)
        if request.POST.get('add') not in item_list:
            cart += 1
            item_list += request.POST.get('add') + '|'

        response.set_cookie('cart', cart)
        response.set_cookie('item_list', item_list)

        return response

    return render(request, 'clothes/clothes.html', {'catalog': catalog})


def home(request):
    dayitem = DayItem.objects.get()
    if 'cart' in request.COOKIES:
        cart = request.COOKIES['cart']
    else:
        cart = 0

    if 'item_list' in request.COOKIES:
        item_list = request.COOKIES['item_list']
    else:
        item_list = ''

    if request.POST:
        print('POST')

        response = HttpResponseRedirect(request.path)
        if int(cart):
            cart = int(cart, base=10)

        if request.POST.get('add') not in item_list:

            cart += 1
            item_list += request.POST.get('add') + '|'

        response.set_cookie('cart', cart)
        response.set_cookie('item_list', item_list)

        return response

    return render(request, 'home/home.html', {'dayitem': dayitem})


def about(request):
    return render(request, 'about/about.html')


def delivery(request):
    return render(request, 'delivery/delivery.html')


def item_look(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'clothes/item_look.html', {'item': item})


def cart(request):
    form = OrderForm()

    if request.POST and 'delete-button' in request.POST:
        response = HttpResponseRedirect(request.path)
        ids_list = request.COOKIES['item_list']
        ids_list = ids_list[:-1].split('|')
        count = request.COOKIES['cart']
        new_count = 0
        print(ids_list)
        del_id = request.POST.get('del_cart')
        ids_list.remove(del_id)
        print(ids_list)

        cart = Item.objects.filter(id__in=ids_list)
        new_ids_list = ''
        if len(ids_list) > 0:
            for i in ids_list:
                new_ids_list += i+'|'
                new_count = int(count, base=10)
                new_count -= 1
        else:
            response.delete_cookie('item_list')
            response.delete_cookie('cart')
        print(new_ids_list)

        response.set_cookie('item_list', new_ids_list)
        response.set_cookie('cart', new_count)
        res = 0
        for i in cart:
            res += i.price

        return response

    if request.POST and 'ord' in request.POST:
        print('POST')
        form = OrderForm(request.POST)
        if form.is_valid():
            print('form valid')
            items = request.COOKIES['item_list'][:-1].split('|')

            text_items = ''
            bd_items = Item.objects.filter(id__in=items)
            for i in bd_items:
                text_items += 'Название: {} \n Артикул: {} \n Цена: {} \n \n'.format(
                    i.name, i.id, i.price)
            order = Order.objects.create(name='{} {} {}'.format(form.cleaned_data['surname'],
                                                                form.cleaned_data['name'], form.cleaned_data['patronymic']),
                                         email=form.cleaned_data['email'],
                                         phone=form.cleaned_data['phone'],
                                         adress=form.cleaned_data['post_adress'],
                                         delivery=request.POST['deliv'],
                                         items=text_items,
                                         date=dt.datetime.now())
            # To client
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email']]

            subject = 'Заказ принят!'
            text = """Приветствую, {}!
            Ваш заказ принят в обработку.
            Скоро с вами свяжется менеджер для дальнейшего офоромления!""".format(form.cleaned_data['name'])

            send_mail(subject, text, email_from, recipient_list)
            managers = User.objects.filter()
            man_subject = 'Поступил новый заказ от {} {} {}'.format(form.cleaned_data['surname'],
                                                                    form.cleaned_data['name'], form.cleaned_data['patronymic'])
            man_text = "Данные о заказе: \n" + text_items
            man_recipient = []
            for i in managers:
                man_recipient.append(i.email)
            send_mail(man_subject, man_text, email_from, man_recipient)
            return HttpResponseRedirect(request.path)
        else:
            
            if 'item_list' in request.COOKIES:
                ids_list = request.COOKIES['item_list']

                ids_list = ids_list[:-1].split('|')

                cart = Item.objects.filter(id__in=ids_list)
                res = 0
                for i in cart:
                 res += i.price
            flag = True
            error = []
            error.append(form['name'].errors)
            error.append(form['surname'].errors)
            error.append(form['patronymic'].errors)
            error.append(form['email'].errors)
            error.append(form['phone'].errors)
            error.append(form['city'].errors)
            error.append(form['post_adress'].errors)
            initial= []
            initial.append(form['name'].value())
            initial.append(form['surname'].value())
            initial.append(form['patronymic'].value())
            initial.append(form['email'].value())
            initial.append(form['phone'].value())
            initial.append(form['city'].value())
            initial.append(form['post_adress'].value())
     
            return render(request, 'cart/cart.html', {'cart': cart, 'res': res, 'form': form, 'error': error, 'flag': flag, 'initial' : initial})
    
    if 'item_list' in request.COOKIES:
        ids_list = request.COOKIES['item_list']

        ids_list = ids_list[:-1].split('|')

        cart = Item.objects.filter(id__in=ids_list)
        res = 0
        for i in cart:
            res += i.price
        return render(request, 'cart/cart.html', {'cart': cart, 'res': res, 'form': form})

    else:
        res = 0
        return render(request, 'cart/cart.html', {'res': res, 'form': form})
