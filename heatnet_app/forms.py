from django import forms
from .models import Node, Link


class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['number', 'address', 'type']


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['node1', 'node2', 'length', 'flow_rate', 'speed']

    def __init__(self, link=None, **kwargs):
        print(kwargs)
        print(link)
        project = kwargs.pop("project")
        super().__init__(**kwargs)

        if project is not None:
            node_qs = Node.objects.filter(project=project)
            self.fields["node1"].queryset = node_qs
            self.fields["node2"].queryset = node_qs
