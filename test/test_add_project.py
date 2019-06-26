from model.project import Project
import string
import random


def random_projectname(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_new_project(app):
    app.session.login("administrator", "root")
    old_projects = app.soap.project_list()
    project = Project(name=random_projectname("proekt_", 12))
    app.project.creation(project)
    new_projects = app.soap.project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)