from backend import Backend
from mydbconfig import *
backend = Backend(config, email, firstname, lastname)

backend.add_authorized_users('cristianfigueroa@cmail.carleton.ca')
backend.add_authorized_users('my_group_mate2_email@cmail.carleton.ca')