from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views.generic import TemplateView



class DepartureView(TemplateView):
    template_name = 'departure.html'


class TourView(TemplateView):
    template_name = 'tour.html'


def custom_handler404(request, exception):
    return HttpResponseNotFound('''404 ошибка - ошибка на стороне
    сервера (страница не найдена), по одной из причин:
    - страница удалена;
    - ссылка на страницу указана неверно;
    - изменился её адрес''')


def custom_handler500(request):
    return HttpResponseServerError('''500 ошибка - внутренняя ошибка сервера,
    попробуйте перезагрузить страницу, если не поможет,
    то перезагрузить Ваш компьютер.
    Либо попробуйте загрузить страницу через некоторое время,
    возможно к тому моменту мы устраним неисправность.
    Если страница все еще не загружается, значит мы ведем работу
    над устранением неисправности, если Вам кажется, что слишком долго
    мы устраняем неисправность, просим Вас написать нам на электронную
    почту [адрес электронной почти], потому что возможно
    программист нашего сайта мог не заметить возникшей неисправности
    и нужно его уведомить об этом!''')
