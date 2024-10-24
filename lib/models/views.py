from lib.middlelayer.userauth import MyModelView
from lib.models.profile import Profile

class ProfileView(MyModelView):
    column_exclude_list = ['password']
    column_searchable_list = ['username']
    can_export = True
    can_view_details = True
