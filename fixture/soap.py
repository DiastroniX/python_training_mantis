from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    project_cache = None

    def project_list(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        self.project_cache = []
        try:
            for element in client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'],
                                                                            self.app.config['webadmin']['password']):
                name = element.name
                id = element.id
                self.project_cache.append(Project(name=name, id=id))
        except WebFault:
            return False
        return list(self.project_cache)