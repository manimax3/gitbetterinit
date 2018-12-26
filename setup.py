#!/usr/bin/env python3

from distutils.core import setup

setup(name="gitbetterinit",
      version="0.1",
      description="Some useful extensions for git init",
      author="Maximilian Schiller",
      author_email="manimax3@hotmail.de",
      url="https://github.com/manimax3/gitbetterinit",
      py_modules=["gitbetterinit"],
      scripts=['gitbetterinit.py'],
      install_requires=["github3.py", "Click",
                        "license", "keyring", "requests"]
      )
