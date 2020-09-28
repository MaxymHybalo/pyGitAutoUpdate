import subprocess
import logging
import sys

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('git-updater')
args = sys.argv
has_target = len(args) > 1

def exec(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = process.communicate()
    return out, err

def update_target(branch):
   c = exec(['git', 'checkout', branch])
   log.info('checkout to target branch: {0}'.format(branch))
   pull = exec(['git', 'pull'])
   log.info(pull[0])

log.info('Args,{0}'.format(args))

if has_target:
    update_target(args[1])


