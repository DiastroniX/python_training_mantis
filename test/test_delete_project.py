from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.soap.project_list()) == 0:
        app.project.creation(Project(name="Moyprojectdlt"))
    old_projects = app.soap.project_list()
    project = old_projects[0]
    app.project.delete_first_project()
    new_projects = app.soap.project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)