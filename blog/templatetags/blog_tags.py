from django import template 
from blog.models import Post,category

register=template.Library()

@register.simple_tag(name='totalpost')

def function() :
    posts = Post.objects.filter(status=1).count()
    return posts

@register.inclusion_tag('blog/blog-popularposts.html')
def latestpost ():
  posts = Post.objects.filter(status=1).order_by('published_date')[:2]
  return {'posts':posts}
  
@register.inclusion_tag('blog/blog-postcategory.html')
def postcategories ():
  posts = Post.objects.filter(status=1)
  categories = category.objects.all()
  cat_dict = {}
  for name in categories:
    cat_dict[name]= posts.filter(category=name).count()
  return {'categories':cat_dict}  


  



