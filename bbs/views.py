from django.shortcuts import render,redirect
from django.views import View

from .models import Topic

class BbsView(View):

    def get(self, request, *args, **kwargs):
        topics  = Topic.objects.all()

        print("GETメソッド")
        context = { "test":"あああああああ",
                    "topics":topics
                    }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):
        print("POSTメソッド")

        #TODO:クライアントから受け取ったデータをDBへ保存する処理
        print(request.POST)
        print(request.POST["comment"])

        #ここで受け取ったデータを保存する
        posted  = Topic( comment=request.POST["comment"] )
        posted.save()

        print(posted.comment)

        topics  = Topic.objects.all()

        print("GETメソッド")
        context = { "test":"あああああああ",
                    "topics":topics
                    }

        #FIXME:ここでレンダリングをしてしまうと、POSTメソッドで終わってしまう。
        #この状態でF5キーを押して更新すると、また同じ内容のPOSTメソッドのリクエストが送信されてしまう。
        return render(request,"bbs/index.html",context)

        #だから、POSTメソッドを受け取ったら、リダイレクトを実行する
        #リダイレクトにより、POSTメソッドが終わった後、GETメソッドにジャンプされる。この状態であればF5キーを押しても再送信はされない。
        # return redirect("bbs:index")


index   = BbsView.as_view()
