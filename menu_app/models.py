from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=255, blank=True, null=True, editable=False)
    tree_depth = models.PositiveIntegerField(default=0, editable=False)

    def set_tree_depth(self):
        if self.parent:
            self.tree_depth = self.parent.tree_depth + 1
        else:
            self.tree_depth = 0

    def generate_url(self):
        if self.parent:
            parent_url = self.parent.url
            self.url = f"{parent_url}/{self.name}"
        else:
            self.url = f"{self.name}"

    def save(self, *args, **kwargs):
        self.set_tree_depth()
        self.generate_url()
        super().save(*args, **kwargs)
       
        for child in self.children.all():
            child.save()

    def __str__(self):
        return self.name