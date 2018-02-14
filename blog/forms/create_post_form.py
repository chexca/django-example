from django import forms

from blog.models import Post


class CreatePostForm(forms.ModelForm):

    def execute(self):
        author = self.cleaned_data.get('author')
        text = self.cleaned_data.get('text')
        title = self.cleaned_data.get('title')

        post = Post.objects.create(author=author, title=title, text=text)

        return post

    class Meta:
        model = Post
        fields = ['author', 'text', 'title']
