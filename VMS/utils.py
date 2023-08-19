
# Extra Functions

def is_super_admin(user):
    return user.is_superuser


def is_admin(user):
    return user.groups.filter(name='Admin').exists()
