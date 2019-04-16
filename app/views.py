# create to myself
from flask import render_template, flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, BaseView
from app import appbuilder, db

# new add
from flask_appbuilder import AppBuilder, expose, BaseView, has_access
from app import appbuilder

from flask_appbuilder import SimpleFormView
from flask_babel import lazy_gettext as _
from .forms import MyForm

from flask_appbuilder import ModelView, MultipleView, MasterDetailView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import ContactGroup, Contact



class MyView(BaseView):

    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
        # do something with param1
        # and return to previous page or index
        return 'Hello'

    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        return param1

    @expose('/method3/<string:param1>')
    @has_access
    def method3(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('method3.html',
                               param1 = param1)


class MyFormView(SimpleFormView):
    form = MyForm
    form_title = 'This is my first form view'
    message = 'My form submitted'

    def form_get(self, form):
        form.field1.data = 'This was prefilled'

    def form_post(self, form):
        # post process form
        flash(self.message, 'info')



class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    label_columns = {'contact_group':'Contacts Group'}
    list_columns = ['name','personal_cellphone','birthday','contact_group']

    show_fieldsets = [
                        (
                            'Summary',
                            {'fields':['name','address','contact_group']}
                        ),
                        (
                            'Personal Info',
                            {'fields':['birthday','personal_phone','personal_cellphone'],'expanded':False}
                        ),
                     ]

class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]

class MultipleViewExp(MultipleView):
    views = [GroupModelView, ContactModelView]

class GroupMasterView(MasterDetailView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]


db.create_all()

appbuilder.add_view(MyView, "Method1", category='My View')
appbuilder.add_link("Method2", href='/myview/method2/john', category='My View')
appbuilder.add_link("Method3", href='/myview/method3/john', category='My View')

appbuilder.add_view(MyFormView, "My form View", icon="fa-group", label=_('My form View'),
                     category="My Forms", category_icon="fa-cogs")

appbuilder.add_view(GroupModelView,
                    "List Groups",
                    icon = "fa-folder-open-o",
                    category = "Contacts",
                    category_icon = "fa-envelope")
appbuilder.add_view(ContactModelView,
                    "List Contacts",
                    icon = "fa-envelope",
                    category = "Contacts")

appbuilder.add_view(MultipleViewExp,
                    "Multiple Views",
                    icon="fa-envelope",
                    category="Contacts")

appbuilder.add_view(GroupMasterView,
                    "Master View",
                    icon="fa-envelope",
                    category="Contacts")
