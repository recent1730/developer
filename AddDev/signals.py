from django.db.models.signals import pre_save, post_save,m2m_changed
from django.dispatch import receiver
from .models import Developer


@receiver(post_save, sender=Developer)
def pre_save_developer(sender, instance, **kwargs):
    score = 0
    projectRating =0
    blogRating =0
    qaRating =0
    for project in instance.project.all():
        projectRating +=project.rating
    for blog in instance.blog.all():
        blogRating += blog.rating
    for q in instance.q_a.all():
        qaRating += q.rating

    score=projectRating+blogRating+qaRating
    print("Score here : ",score)

    instance.score =  "{:.2f}".format(score)
