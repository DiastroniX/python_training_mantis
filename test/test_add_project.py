from model.project import Project

def test_add_new_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    project = Project(name="Moyproject")
    app.project.creation(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    old_projects == new_projects