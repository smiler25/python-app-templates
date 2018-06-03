import os
import multiprocessing

env = os.environ

bind = '0.0.0.0:8080'
if env.get('WORKERS'):
    workers = int(env['WORKERS'])
else:
    workers = multiprocessing.cpu_count() * 2 + 1

threads = int(env.get('THREADS', 1))

accesslog = '-'
access_logformat = '%t [%s] %a "%r" "%{User-Agent}i" [%b bytes %Tf s]'
