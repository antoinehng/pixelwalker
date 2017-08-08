# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic


# import db models
from engine.models import EncodingProvider, Media, Assessment


# List all encoding providers
def list(request):
    encoding_provider_list = EncodingProvider.objects.all().order_by('name')
    return render(request, 'encoding_provider/list.html', {'encoding_provider_list':encoding_provider_list})


#Crud
def create(request):
    # Submitting values for new encoding provider
    if request.POST:
        new_encoding_provider = EncodingProvider()
        # set values
        new_encoding_provider.name = request.POST.get('name')
        new_encoding_provider.save()
        return HttpResponseRedirect(reverse('webgui:encoding_provider_read', args=(new_encoding_provider.id,)))

    # Asking for the new encoding provider form
    else:
        return render(request, 'encoding_provider/create.html')


#cRud
def read(request, encoding_provider_id):
    encoding_provider = get_object_or_404(EncodingProvider, pk=encoding_provider_id)
    media_list = Media.objects.filter(encoding_provider=encoding_provider)
    return render(request, 'encoding_provider/read.html', {'encoding_provider': encoding_provider, 'media_list':media_list})


#crUd
def update(request, encoding_provider_id):
    encoding_provider = get_object_or_404(EncodingProvider, pk=encoding_provider_id)

    # Submitting values for updating encoding provider
    if request.POST:
        # update values
        encoding_provider.name = request.POST.get('name')
        encoding_provider.save()
        return HttpResponseRedirect(reverse('webgui:encoding_provider_read', args=(encoding_provider.id,)))

    # Asking for the edit encoding provider form
    else:
        return render(request, 'encoding_provider/update.html', {'encoding_provider': encoding_provider})


#cruD
def delete(request, encoding_provider_id):
    encoding_provider = EncodingProvider.objects.filter(id=encoding_provider_id)[0]

    # If delete confirm
    if request.POST:
        # delete the encoding provider object
        if encoding_provider_id == request.POST.get('delete_id'):
            encoding_provider.delete()
            return HttpResponseRedirect(reverse('webgui:encoding_provider_list'))
        else:
            return render(request, 'encoding_provider/read.html', {'encoding_provider': encoding_provider})

    # Asking for the delete confirmation form
    else:
        return render(request, 'encoding_provider/delete.html', {'encoding_provider': encoding_provider})
