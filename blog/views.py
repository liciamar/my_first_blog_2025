from django.shortcuts import render

#we create a function (def) called post_list that takes request and will return the value it gets from calling another function render that will render (put together) our template blog/post_list.html
def post_list(request):
    return render(request, 'blog/post_list.html', {})