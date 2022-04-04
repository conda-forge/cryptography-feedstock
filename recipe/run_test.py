import re
import subprocess
import time
from cryptography.hazmat.backends.openssl import backend

# the version that cryptography uses
linked_version = backend.openssl_version_text()
# the version present in the conda environment
env_version = subprocess.check_output('openssl version', shell=True).decode('utf8').strip()
# strip off possible brackets from e.g. "OpenSSL 3.0.0 7 sep 2021 (Library: OpenSSL 3.0.0 7 sep 2021)"
env_version = re.sub(r"(?P<version>OpenSSL [\d\.]+ \d+ [A-Za-z]{3} 20\d\d)(?P<irrelevant> \(.*\))?",
                     r"\1", env_version)

print('Version used by cryptography:\n{linked_version}'.format(linked_version=linked_version))
print('Version in conda environment:\n{env_version}'.format(env_version=env_version))

# avoid race condition between print and (possible) AssertionError
time.sleep(1)

# linking problems have appeared on windows before (see issue #38),
# and were only caught by lucky accident through the test suite.
# This is intended to ensure it does not happen again.
assert linked_version == env_version
