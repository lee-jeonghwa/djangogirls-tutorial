from django.http import HttpResponse
from django.utils import timezone


def post_list(request):
    '''

    :param request: 실제 HTTP요청에 대한 정보를 가진 객체
    :return:
    '''
    current_time = timezone.now()
    return HttpResponse(
        '<html>'
        '<body>'
        '<h1>Post List</h1>'
        '<p>{}</p>'
        '</body>'
        '</html>'.format(
            current_time.strftime('%Y. %m. %d<br>%H:%M:%S')
        )
    )

