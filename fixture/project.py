from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/my_view_page.php")):
            wd.find_element_by_link_text("My view").click()

    def open_projects_to_manage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def filling_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def creation(self, project):
        wd = self.app.wd
        self.open_projects_to_manage()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.filling_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_to_manage()
            self.project_cache = []
            for row in wd.find_elements_by_css_selector("tr.row-1, tr.row-2"):
                cells = row.find_elements_by_css_selector("td")
                text_name = cells[0].text
                self.project_cache.append(Project(name=text_name))
        return list(self.project_cache)

    def delete_first_project(self):
        wd = self.app.wd
        self.open_projects_to_manage()
        wd.find_element_by_css_selector("tr.row-1 > td > a").click()
        # submit delete
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.project_cache = None