from django.db import models


class Post(models.Model):
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name="posts", verbose_name="Owner")
    name = models.CharField(verbose_name="Title", max_length=100)
    content = models.TextField(verbose_name="Content")
    image = models.ImageField(verbose_name="Image", upload_to="image/", null=True, blank=True)
    created = models.DateTimeField(verbose_name="Create date", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Update date", auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name="comments", verbose_name="Owner")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "comments", verbose_name = "Post")
    content = models.TextField(verbose_name="Content")
    created = models.DateField(verbose_name="Create date", auto_now_add=True)
    updated = models.DateField(verbose_name="Update date", auto_now=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
