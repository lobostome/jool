# -*- coding: utf-8 -*-

from pygit2 import Keypair, RemoteCallbacks, Repository, clone_repository, GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE

class Git(object):
    def __init__(self, public_key, private_key, repo_from=None, repo_to=None):
        self.public_key = public_key
        self.private_key = private_key

    def clone_repo(self, repo_from, repo_to):
        self.repo_from = repo_from
        self.repo_to = repo_to
        keypair = Keypair("git", self.public_key, self.private_key, "")
        callbacks = RemoteCallbacks(credentials=keypair)

        clone_repository(self.repo_from, self.repo_to, callbacks=callbacks)

    def traverse(self):
        repo = Repository('%s/.git' % self.repo_to)
        commits = []
        for commit in repo.walk(repo.head.target, GIT_SORT_REVERSE):
            commits.append(commit.id)

        return commits
