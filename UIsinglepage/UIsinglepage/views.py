from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "UIsinglepage/index.html")


texts =["This is the Gods given Job, for me now to sit at home, to be the servant of my wife, who is controlling me by means of a hackers who has hacked all my phones, laptop, bank account & so on. Also the hacker is listening to all my discussion with anyone if I am carrying the phone.",
       "As I had married a girl, telling that I dont wants to marry, but since my father forcing me, so I cannt avoid: it So I left it to her to decide, Now after totally discussing all my point my wife didnot able to judge me & since last years she totally controlling me but I am unaware of this so I didnot able to know this but since I am aware that a girl will do like this rather even after so many blames to me by his staffs, her mother office staff I didnot able to know anything about this, just did whatever she told I did, I never demand money given kind of pressures but I was doing the work my heart to give her the happiness she lost her father when she was old;",
       "whether to marry me, also I told her that you should collect data about my family, house which good, still she agrees that day. till now she  keeping me a servant, now since, I became old & suffered disease so time she can kill me.;""This is the Gods given Job, for me now to sit at home, to be the servant of my wife, who is controlling me by means of a hackers who has hacked all my phones, laptop, bank account & so on. Also the hacker is listening to all my discussion with anyone if I am carrying the phone."]

def section(request, num):
    if 1<= num <=3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")