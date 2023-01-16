from django.http import HttpResponse

# Импортируем загрузчик.
from django.template import loader


def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = loader.get_template('ice_cream/index.html')
    # Формируем шаблон
    return HttpResponse(template.render({}, request)) 

def ice_cream_list(request):
    return HttpResponse('Список мороженого')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
