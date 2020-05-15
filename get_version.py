#!/usr/bin/env python

import io
import re


def get_version():
    with io.open('./learning_ttd_python/__init__.py', encoding='utf8') as version_f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  version_f.read(), re.M)
        if version_match:
            return version_match.group(1)
        else:
            raise RuntimeError("Unable to find version string.")


if __name__ == "__main__":
    version = get_version()
    print(version)
