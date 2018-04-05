# assuming there is a connection pool located in the repo
from pool import db

class User(object):
  def __init__(self, id, username, email):
    super(User, self).__init__()

    self.id = None
    self.username = None
    self.email = None
  
  def get_by_user_ids(self, ids):

    with db.open() as connection:
      statement = 'select id, username, email from user where id in ({})'.format(', '.join(ids))

      result = connection.execute(statement)

      users = []
      for user in result.records:
        users.append(User(user.id, user.username, user.email))

      return users
      