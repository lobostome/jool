# -*- coding: utf-8 -*-

from pygit2 import Keypair, RemoteCallbacks, Repository, clone_repository
from pygit2 import Commit, Diff, GIT_SORT_REVERSE
from .data import Frame
from abc import ABCMeta, abstractmethod
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import re
import functools


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

        previous, diff = None, None
        for commit in generator_expression:
            previous, diff = self.determine_diff(
                repo, commit, previous, diff)
            populator.add_commit_to_lists(commit, diff)

        populator.to_frame()

    def determine_diff(self, repo, commit, previous, diff):
        if previous is not None:
            diff = repo.diff(str(commit.id), str(previous.id))
        else:
            tree = repo.revparse_single(str(commit.id)).tree
            diff = tree.diff_to_tree()

        if commit.parents:
            previous = commit

        return (previous, diff)

    @property
    def dataset(self):
        return self.frame


class MapInterface(object, metaclass=ABCMeta):

    @abstractmethod
    def map(self, line):
        pass


class FilterInterface(object, metaclass=ABCMeta):

    @abstractmethod
    def filter(self, words: list) -> bool:
        pass


class BugFilter(FilterInterface):

    def filter(self, words: list) -> bool:
        stemmer = PorterStemmer()
        counter = [word for word in words if stemmer.stem(word) == 'fix']
        return True if len(counter) > 0 else False


class TransformInterface(object, metaclass=ABCMeta):

    @abstractmethod
    def convert(self, key: str, commit: Commit, diff: Diff) -> str:
        pass

    def filter_diff_line(self, diff: Diff, key: str, value) -> list:
        content = []
        for p in diff:
            for h in p.hunks:
                for l in h.lines:
                    if getattr(l, key) == value:
                        content.append(l.content.strip())
        return content


class AuthorTransform(TransformInterface):

    def convert(self, key: str, commit: Commit, diff: Diff) -> str:
        value = getattr(commit, key)
        return value.name


class MessageTransform(TransformInterface):

    def convert(self, key: str, commit: Commit, diff: Diff) -> str:
        value = getattr(commit, key)
        return value.rstrip()


class BugTransform(TransformInterface):

    def convert(self, key: str, commit: Commit, diff: Diff) -> str:
        bug_filter = BugFilter()
        value = bug_filter.filter(word_tokenize(commit.message))
        return 'y' if value else 'n'


class FilesTransform(TransformInterface):

    def convert(self, key: str, commit: Commit, diff: Diff) -> str:
        files = [p.delta.new_file.path.split(
            '/') for p in diff] if len(diff) > 0 else []
        files = functools.reduce(lambda x, y: x + y, files)
        return ' '.join(list(set(files)))


class AddedTransform(TransformInterface):

    def convert(self, key: str, commit: Commit, diff: Diff) -> str:
        return " ".join(self.filter_diff_line(diff, 'new_lineno', -1))


class DeletedTransform(TransformInterface):

    def convert(self, key: str, commit: Commit, diff: Diff) -> str:
        return " ".join(self.filter_diff_line(diff, 'old_lineno', -1))


class FramePopulator(object):
    def __init__(self, frame):
        self.lists = {}
        self.frame = frame
        self.variables = [
            'commit_id',
            'commit_message',
            'commit_files',
            'delta_added',
            'delta_deleted',
            'commit_author',
            '_commit_time',
            'is_bug']
        for variable in self.variables:
            self.lists[variable] = []

    def add_commit_to_lists(self, commit: Commit, diff: Diff):
        for variable in self.variables:
            key = self.extract_key(variable)
            if self.create_transform_classname(key) in globals():
                value = self.transform(key, commit, diff)
            else:
                value = getattr(commit, key)
            self.lists[variable].append(value)

    def to_frame(self):
        for variable in self.variables:
            self.frame.add_column(variable, self.lists[variable])

    def extract_key(self, index):
        return index.split('_', maxsplit=1)[1]

    def create_transform_classname(self, value: str) -> str:
        return "%sTransform" % value.title()

    def transform(
            self,
            class_key: str,
            commit: Commit,
            diff: Diff) -> TransformInterface:
        class_name = self.create_transform_classname(class_key)
        object = globals()[class_name]
        return object().convert(class_key, commit, diff)
