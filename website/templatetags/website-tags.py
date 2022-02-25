from django import template 
from blog.models import Post
register=template.Library()

@register.inclusion_tag('blog/blog-latestposts.html')
def lastestposts ():
  posts = Post.objects.filter(status=1).order_by('published_date')
  return {'posts':posts}
