import json

from django.db.models import Q
from django.shortcuts import render, redirect
from heatnet_app.models import Project, Node, Link
from heatnet_app.forms import NodeForm, LinkForm
import networkx as nx
import matplotlib.pyplot as plt


def proj(request):
    return render(request, 'proj.html')


def home(request):
    return render(request, 'home.html')


def create_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        # Створення нового проекту
        project = Project.objects.create(name=project_name)
        # Після створення проекту перенаправляємо на його сторінку
        return redirect('project_detail', project_id=project.id)
    else:
        return render(request, 'create_project.html')


def proj_detail(request):
    return render(request, 'proj_detail.html')


def proj_list(request):
    projects = Project.objects.all()
    return render(request, 'proj_list.html', {'projects': projects})


def node_view(request):
    return render(request, 'node.html')


def links_view(request):
    links = Link.objects.all()
    return render(request, 'links.html', {'links': links})


def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    node_form = NodeForm(request.POST or None)
    link_form = LinkForm(request.POST or None, project=project)

    if request.method == 'POST':
        if node_form.is_valid():
            node = node_form.save(commit=False)
            node.project = project
            node.save()
            return redirect('project_detail', project_id=project_id)

        elif link_form.is_valid():
            link = link_form.save(commit=False)
            link.save()
            return redirect('project_detail', project_id=project_id)
    nodes = project.nodes
    links = Link.objects.filter(Q(node1__project=project) | Q(node2__project=project))
    graph_nodes = [{"id": node.id} for node in nodes.all()]
    graph_links = [{"source": link.node1.id, "target": link.node2.id} for link in links.all()]
    graph_data = {"nodes": graph_nodes, "links": graph_links}

    return render(request, 'project_detail.html', {
        'project': project,
        'node_form': node_form,
        'link_form': link_form,
        "nodes": nodes.all(),
        "links": links.all(),
        "graph_data": json.dumps(graph_data)
    })
