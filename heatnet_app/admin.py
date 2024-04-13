from django.contrib import admin

from .models import Project, Node, Link


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )


admin.site.register(Project, ProjectAdmin)
admin.site.register(Node)
admin.site.register(Link)


