# -*- coding: utf-8 -*-

from pygit2 import Keypair, RemoteCallbacks, Repository, clone_repository
from pygit2 import GIT_SORT_REVERSE
from .data import Frame


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
        commit_ids = []
        commit_messages = []
        commit_authors = []

        generator_expression = (
            commit for commit in repo.walk(
                repo.head.target,
                GIT_SORT_REVERSE) if not commit.message.startswith('Merge'))

        for commit in generator_expression:
            commit_ids.append(commit.id)
            commit_messages.append(commit.message)
            commit_authors.append(commit.author.name)

        self.frame.add_column("commit_id", commit_ids)
        self.frame.add_column("commit_message", commit_messages)
        self.frame.add_column("commit_author", commit_authors)


    @property
    def dataset(self):
        return self.frame
