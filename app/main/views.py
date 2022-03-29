from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


def anonymous_required(redirect_url):
    def _wrapped(view_func, *args, **kwargs):
        def check_anonymous(request, *args, **kwargs):
            view = view_func(request, *args, **kwargs)
            if request.user.is_authenticated:
                return redirect(redirect_url)
            return view

        return check_anonymous

    return _wrapped


class Welcome(APIView):

    def get(self, request):
        response = {
            'message': 'Welcome to the BEON Python/Django Challenge'
        }
        return Response(response, status=status.HTTP_200_OK)
