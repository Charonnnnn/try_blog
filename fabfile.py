from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/Charonnnnn/try_blog.git"

env.user = 'charon'
env.password = 'a'

# 填写你自己的主机对应的域名
env.hosts = ['demo.charon.me']

# 一般情况下为 22 端口
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

