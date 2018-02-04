# -*- coding: utf-8 -*-

import pygit2

class Git(object):
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def clone_repository(self, repo_from, repo_to):
        keypair = pygit2.Keypair("git", self.public_key, self.private_key, "")
        callbacks = pygit2.RemoteCallbacks(credentials=keypair)

        pygit2.clone_repository(repo_from, repo_to, callbacks=callbacks)
