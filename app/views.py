# create to myself
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, BaseView
from app import appbuilder, db

# new add
from flask_appbuilder import AppBuilder, expose, BaseView, has_access
from app import appbuilder



class MyView(BaseView):
    route_base = "/myview"

    @expose('/method1/')
    @has_access
    def method1(self):
        # do something with param1
        # and return to previous page or index
        return 'Hello'

    @expose('/method2/<string:param2>')
    @has_access
    def method3(self, param2):
        # do something with param1
        # and render it
        param2 = 'Goodbye Mr. %s' % (param2)
        return param2

    @expose('/method3/<string:param1>')
    @has_access
    def method3(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('method3.html',
                               param1 = param1)


appbuilder.add_view_no_menu(MyView())
appbuilder.add_link("Method1", href='/myview/method1/', category='My View')
appbuilder.add_link("Method2", href='/myview/method2/john', category='My View')
appbuilder.add_link("Method3", href='/myview/method3/john', category='My View')




"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')


    Application wide 404 error handler

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()
"""
