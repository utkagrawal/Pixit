from django.shortcuts import render
from . import models
from django.http import JsonResponse
import cv2
import numpy as np
from django.urls import reverse
from PIL import Image
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView


def square_image(inpath, outpath):
    img = cv2.imread(inpath)

    height, width = img.shape[:2]

    max_dim = max(width, height)

    square_canvas = np.ones((max_dim, max_dim, 3), dtype=np.uint8) * 255

    paste_x = (max_dim - width) // 2
    paste_y = (max_dim - height) // 2

    square_canvas[paste_y:paste_y+height, paste_x:paste_x+width] = img

    cv2.imwrite(outpath, square_canvas)

num=2
gnum=32

# Create your views here.
def IntroPageView(request):
    return render(request, 'my_app/example.html')



def HomePageView(request):
    if request.method == 'POST':
        if 'imageInput' in request.FILES:
            image_file = request.FILES['imageInput']
            
            
            with open('media/touse/images/image.png', 'wb') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)

            
            inpath = "media/touse/images/image.png"
            outpath = "media/touse/images/image.png"
            square_image(inpath, outpath)

            
            num=2
            gnum=32
            for i in range(6):
                img = cv2.imread(outpath)
                
                height, width = img.shape[:2]

                temp = cv2.resize(img, (num, num), interpolation=cv2.INTER_CUBIC)
                img = cv2.resize(temp, (640, 640), interpolation=cv2.INTER_NEAREST)

                grid_spacing = gnum * 10  # Adjust this value as needed
                for y in range(0, 640, grid_spacing):
                    cv2.line(img, (0, y), (640, y), (0, 0, 0), 1)
                for x in range(0, 640, grid_spacing):
                    cv2.line(img, (x, 0), (x, 640), (0, 0, 0), 1)


                output_path = f"my_app/static/my_app/output{i}.png"
                cv2.imwrite(output_path, img)

                num *= 2
                gnum /= 2
                gnum=int(gnum)
                #pixleit(num,gnum)
            return HttpResponseRedirect(reverse('my_app:loading'))

    return render(request, 'my_app/home.html')

def LoadView(request):
    return render(request,'my_app/loading.html')

def ResultView(request):
    return render(request,'my_app/result.html')

def ExampleView(request):
    return render(request, 'my_app/sample.html')

def AboutView(request):
    return render(request,'my_app/about.html')

