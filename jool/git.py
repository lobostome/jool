# -*- coding: utf-8 -*-

from pygit2 import Keypair, RemoteCallbacks, Repository, clone_repository
from pygit2 import GIT_SORT_REVERSE
from .data import Frame
from .utils import FramePopulator
import re


class Git(object):
    def __init__(self, public_key, private_key, repo_from=None, repo_to=None):
        self.public_key = public_key
        self.private_key = private_key
        self.frame = Frame()

    def clone_repo(self, repo_from, repo_to):
        self.repo_from = repo_from
        self.repo_to = repo_to
        keypair = Keypair("git", self.public_key, self.private_key, "")
        callbacks = RemoteCallbacks(credentials=keypair)

        clone_repository(self.repo_from, self.repo_to, callbacks=callbacks)

    def traverse(self):
        repo = Repository('%s/.git' % self.repo_to)
        populator = FramePopulator(self.frame)

        generator_expression = (
            commit for commit in repo.walk(
                repo.head.target,
                GIT_SORT_REVERSE) if not re.match(
                    r'^merge', commit.message, re.IGNORECASE))

        for commit in generator_expression:
            populator.create_lists(commit)

        populator.to_frame()

    @property
    def dataset(self):
        return self.frame
