from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import speedtest

# Create your views here.


def servers(request):
    stest = speedtest.Speedtest()
    return JsonResponse({
        'servers': stest.get_servers(),
    })


def best(request):
    stest = speedtest.Speedtest()
    return JsonResponse({
        'best_server': stest.get_best_server(),
    })


def config(request):
    stest = speedtest.Speedtest()
    return JsonResponse({
        'config': stest.config,
    })


def upload(request):
    stest = speedtest.Speedtest()
    stest.get_best_server(servers=[{"url": "http://speedtest-cpt.voxtelecom.co.za/upload.php", "lat": "-33.9253", "lon": "18.4239", "name": "Cape Town", "country": "South Africa", "cc": "ZA", "sponsor": "Vox Telecom", "id": "7318", "url2": "http://speedtest-cpt1.voxtelecom.co.za/upload.php", "host": "speedtest-cpt.voxtelecom.co.za:8080", "d": 0.08521976909151716, "latency": 7.061}])
    return JsonResponse({
        'upload': stest.upload(),
    })


def download(request):
    stest = speedtest.Speedtest()
    stest.get_best_server(servers=[{"url": "http://speedtest-cpt.voxtelecom.co.za/upload.php", "lat": "-33.9253", "lon": "18.4239", "name": "Cape Town", "country": "South Africa", "cc": "ZA", "sponsor": "Vox Telecom", "id": "7318", "url2": "http://speedtest-cpt1.voxtelecom.co.za/upload.php", "host": "speedtest-cpt.voxtelecom.co.za:8080", "d": 0.08521976909151716, "latency": 7.061}])
    return JsonResponse({
        'download': stest.download(),
    })


def closest(request):
    stest = speedtest.Speedtest()
    return JsonResponse({
        'closest': stest.get_closest_servers(),
    })


def test(request):
    stest = speedtest.Speedtest()
    stest.get_best_server(servers=[{"url": "http://speedtest-cpt.voxtelecom.co.za/upload.php", "lat": "-33.9253", "lon": "18.4239", "name": "Cape Town", "country": "South Africa", "cc": "ZA", "sponsor": "Vox Telecom", "id": "7318", "url2": "http://speedtest-cpt1.voxtelecom.co.za/upload.php", "host": "speedtest-cpt.voxtelecom.co.za:8080", "d": 0.08521976909151716, "latency": 7.061}])
    return JsonResponse({
        'upload': stest.upload(),
        'download': stest.download(),
        'config': stest.config,
        'results': stest.results.json(),
        'summary': stest.results.share(),
    })


def tests(request):
    stest = speedtest.Speedtest()
    stest.get_best_server(servers=[{"url": "http://speedtest-cpt.voxtelecom.co.za/upload.php", "lat": "-33.9253", "lon": "18.4239", "name": "Cape Town", "country": "South Africa", "cc": "ZA", "sponsor": "Vox Telecom", "id": "7318", "url2": "http://speedtest-cpt1.voxtelecom.co.za/upload.php", "host": "speedtest-cpt.voxtelecom.co.za:8080", "d": 0.08521976909151716, "latency": 7.061}])
    stest.upload()
    stest.download()
    return JsonResponse(stest.results.dict())
