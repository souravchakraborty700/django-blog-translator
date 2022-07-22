from django.shortcuts import render

from googletrans import Translator




# def translate_app(request):
#     if request.method == "POST":
#         lang = request.POST.get("lang", None)
#         # txt = request.POST.get("txt", None)

#         # translator = Translator()
#         # tr = translator.translate(txt, dest=lang)

#         return lang
# lang = translate_app(request)



def translate(text):
    translator = Translator()
    translation = translator.translate(text=text, dest='de')
    return translation.text
    
















# from googletrans import Translator



# def translate(text):
#     translator = Translator()
#     translation = translator.translate(text= text, dest = 'de')
#     return translation.text