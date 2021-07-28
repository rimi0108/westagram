import json
from users.utils import signin_decorator

from django.http  import JsonResponse
from django.views import View
from django.utils import timezone

from users.models    import User
from postings.models import Post

# Create your views here.

class PostView(View):
  #@signin_decorator
  def post(self, request):
    try:
      data = json.loads(request.body)

      if not User.objects.get(email=data['email']).exists():
        return JsonResponse({'message':'INVALID_USER'}, status=401)

      now = timezone.now() 

      Post.objects.create(
        creation_time   = now.strftime("%H:%M:%S"),
        image_url       = data['image_url'],
        posting_title   = data['posting_title'],
        posting_content = data['posting_content'],
        user_id         = User.objects.get(email=data['email']).id  
      )
      return JsonResponse({'message':'CREATED'}, status=201)

    except:
      return JsonResponse({'message':'KEY_ERROR'}, status=400)

  #@signin_decorator
  #def get(self, request):
    #results = []
    #posts = Post.objects.all()

    #for post in posts:
      #results.append(
        #{
          #'user' : post.users.get(id = user_id)

        #}
      #)
              
      
    #return JsonResponse({'result':results}, status=200)
