from django.http import HttpResponse
import re
# import os
# from django.utils import timezone
# from django.template import loader
# import random
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-created_date')

    # post_title = '<ul>'
    # for post in posts:
    #     post_title += f'<li>{post.title}</li>'
    # post_title += '</ul>'

    context = {
        'posts': posts,
    }
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context
    )


def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)



    #템플릿을 가져옴 (단순 문자열이 아님)
    # template = loader.get_template('blog/post_list.html')
    # # 해당 템플릿을 렌더링
    # context ={
    #     'name': random.choice(['이정화', '박영수']),
    #
    # }
    # content = template.render(context, request)
    # return HttpResponse(content)
    # context ={
    #     'name': random.choice(['이정화', '박영수']),
    # }
    # # render 함수 알아보기 !!  위의 것과 같은 결과를 보여줌
    # # loader.get_template
    # # template.render
    # # HttpResponse(content)
    # # 위 3가지를 한번에 해주는 역할
    # return render(
    #     request=request,
    #     template_name='blog/post_list.html',
    #     context=context
    # )



    # # templates/blog/post_list.html 파일의 내용을 읽어온 후,
    # # 해당 내용을 아래에서 리턴해주는 HttpResponse인스턴스 생성시 인수로 넣우준다
    # # os.path.abspath(__file__) <-코드가 실행중인 파일의 경로를 나타냄
    # # os.path.dirname(<경로>) <-특정 경로의 상위폴더를 나타냄
    # # os.path.join(<경로>, <폴더/파일명>) <- 특정 경로에서 하위폴더 또는 하위 파일을 나타냄
    # # current_path = os.path.abspath(__file__)
    # # p_path = os.path.dirname(current_path)
    # # p_path = os.path.dirname(p_path)
    # # c_path = os.path.join(p_path, 'templates')
    # # c_path = os.path.join(c_path, 'blog')
    # # html_path = os.path.join(c_path, 'post_list.html')
    #
    # views_file_path = os.path.abspath(__file__)
    # blog_application_path = os.path.dirname(views_file_path)
    # app_dir = os.path.dirname(blog_application_path)
    # template_path = os.path.join(app_dir, 'template', 'blog', 'post_liost.html')
    #
    # with open(template_path, 'rt') as f:
    #     html_text = f.read()
    # # #with문 안쓴다면
    # # html_text = open(template_path, 'rt').read()
    #
    # return HttpResponse(html_text)



