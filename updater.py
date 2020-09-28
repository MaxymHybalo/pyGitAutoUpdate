import subprocess
import logging
import sys
import yaml
from yaml import Loader as Loader

def exec(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = process.communicate()
    return out, err

def update_target(branch):
    c = exec(['git', 'checkout', branch])
    log.info('checkout to target branch: {0}'.format(branch))
    pull = exec(['git', 'pull'])
    log_output(pull)
    merge = exec(['git', 'pull', 'origin', MASTER, '--no-edit'])
    log_output(merge)
    push = exec(['git', 'push'])
    log_output(push)

def log_output(output):
    out, err = output
    if out:
        log.info(out)
    if err:
        log.error(err)

def config():
    data = {}
    with open('config.yml', 'r') as stream:
        data= yaml.load(stream, Loader=Loader)
    return data

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('git-updater')
args = sys.argv
has_target = len(args) > 1
MASTER = config()['master']
log.info('master branch: {0}'.format(MASTER))
log.info('Args,{0}'.format(args))

if has_target:
    update_target(args[1])


