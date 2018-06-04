from fabric.api import env
from fabric.api import run
from fabric.operations import sudo

GIT_REPO = "https://github.com/Charonnnnn/try_blog.git"

env.user = 'charon'
env.password = 'a'

# domain name
env.hosts = ['demo.charon.me']

# normally is port 22
env.port = '22'


def deploy():
    source_folder = '/home/charon/sites/demo.charon.me/try_blog'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-demo.charon.me')
    sudo('service nginx reload')

