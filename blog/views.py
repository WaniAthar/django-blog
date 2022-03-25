from blog.templatetags import extras
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from blog.models import Post, BlogComment
from blog.templatetags import extras


def home(request):
    allposts = Post.objects.all().order_by('-Publishing_Time')
    recentpost = Post.objects.all().order_by('-Publishing_Time')[:3]
    context = {'allposts': allposts, 'recentpost': recentpost}

    return render(request, 'bloghome.html', context)


def Blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()  # we can use [0] instead of .first() also,, in order to get fetch the first element of the post otherwise it will fetch the __str__ returning value that is the title displayed in the admin panel
    comments = BlogComment.objects.filter(post=post, parent = None)  #to obtain the comments of this particular post from the database
    replies = BlogComment.objects.filter(post=post).exclude(parent = None)
    replydict = {}
    for reply in replies:
        if reply.parent.sno not in replydict.keys():
            replydict[reply.parent.sno] = [reply]
        else:
            replydict[reply.parent.sno].append(reply)
    # print(replydict)
        
    context = {'post': post, 'comments': comments, 'user':request.user, 'replydict':replydict}
    return render(request, "blog-post.html", context)


# to get comments from the post to database
def PostComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":

            if comment == "":
                messages.error(request, "No input was given int the comment") 

            else:
                comments = BlogComment(comment=comment, user=user, post=post)
                comments.save()
                messages.success(request, "Your comment has been addded succesfully")
        else:
            if comment == "":
                messages.error(request, "No input was given in reply")
            else:        
                parent = BlogComment.objects.get(sno=parentSno)
                comments = BlogComment(comment = comment, user = user, post = post, parent = parent)
                messages.success(request, "Your reply has been posted succesfully")
                comments.save()
                
            

        #  here i am not adding parent comment because this itself is the parent comment
        

    return redirect(f"/posts/{post.slug}")