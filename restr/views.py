from django.shortcuts import render,redirect
from . import forms
from .models import Kuxnya,Zavedeniye,Restaurant,MenuItem,Review,Reservation
from .forms import ReviewForm,SearchForm,ReservationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .handlers import bot

def home(request):
    #  форма для поиска
    search_bar = forms.SearchForm()
    # Отправить элементы на фронт
    context = {"form": search_bar}
    return render(request, 'home.html', context)
def search_restaurant(request):
    if request.method == 'POST':
        info = request.POST.get('search_restaurant')
        try:
            infot = Restaurant.objects.get(name__icontains=info)
            return redirect(f'restaurant/{infot.id}')
        except:
            return redirect('/not-found')



def about(request):
    return render(request,'about.html')
def not_found(request):
    return render(request,'not-found.html')
class Register(View):
    template_name = 'registration/register.html'

    # Отправка формы регистрации
    def get(self, request):
        context = {'form': UserCreationForm}
        return render(request, self.template_name, context)

    # Добавление в БД
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {'form': UserCreationForm}
        return render(request, self.template_name, context)
def kuxnya(request):
    kuxnya_info = Kuxnya.objects.all()
    context = { 'kuxnya': kuxnya_info
               }
    return render(request, 'kuxnya.html', context)

def kuxnyaa(request, pk):
    kuxnya = Kuxnya.objects.get(id=pk)
    restaurant = Restaurant.objects.filter(kuxnya=kuxnya)
    context = {'kuxnya': restaurant}
    return render(request, 'kuxnyaa.html', context)
def zavedeniye(request):
    zavedeniye_info = Zavedeniye.objects.all()
    context = {'zavedeniye': zavedeniye_info}
    return render(request, 'zavedeniye.html', context)
def zavedeniyee(request, pk):
    zavedeniye = Zavedeniye.objects.get(id=pk)
    restaurant = Restaurant.objects.filter(zavedeniye=zavedeniye)
    context = {'zavedeniye': restaurant}
    return render(request, 'zavedeniyee.html', context)
def menu(request):
    menu_info = MenuItem.objects.all()
    context = {'menu': menu_info}
    return render(request, 'menu.html', context)
def menuu(request,pk):
    menu = MenuItem.objects.filter(id=pk)
    context = {'menu': menu}
    return render(request, 'menuu.html', context)

def review(request):
    review_info = Restaurant.objects.all()
    context = {'restaurant': review_info}
    return render(request, 'review.html', context)

def revieww(request, pk):
    restaurant = Restaurant.objects.get(id=pk)  # Получаем ресторан по его id
    reviews = Review.objects.filter(restaurant_id=pk)  # Фильтруем все отзывы по restaurant
    context = {'restaurant': restaurant, 'reviews': reviews}
    return render(request, 'revieww.html', context)


def restaurantt(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    menu = MenuItem.objects.filter(restaurant=restaurant)
    review = Review.objects.filter(restaurant=restaurant)
    kuxnya = Kuxnya.objects.filter(restaurant=restaurant)
    zavedeniye = Zavedeniye.objects.filter(restaurant=restaurant)


    return render(request, 'restaurant.html', {'restaurant': restaurant, 'menu': menu, 'review': review,
                                               'kuxnya':kuxnya,'zavedeniye':zavedeniye})




def createrev(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form = ReviewForm()
    return render(request, 'createrev.html', {'form': form})


def book(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = form.cleaned_data['user']
            reservation.time = form.cleaned_data['time']
            reservation.restaurant = form.cleaned_data['restaurant']
            reservation.desired_table = form.cleaned_data['desired_table']
            reservation.save()


            text = 'Новое бронирование!\n\n'
            text += f'Юзер: {reservation.user}\n' \
                    f'Время: {reservation.time}\n' \
                    f'Ресторан: {reservation.restaurant}\n' \
                    f'Желаемое место: {reservation.desired_table}\n\n'
            bot.send_message( -4132123880, text)

            return render(request, 'home.html')


    else:
        form = ReservationForm()
    return render(request, 'book.html', {'form': form})