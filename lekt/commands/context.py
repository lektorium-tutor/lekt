from ..jobs import BaseJobRunner
from ..types import Config


class Context:
    """
    Context object that is passed to all subcommands.

    The project `root` is passed to all subcommands of `lekt`; that's because
    it is defined as an argument of the top-level command. For instance:

        $ lekt --root=... local run ...
    """

    def __init__(self, root: str, plugins_root: str) -> None:
        self.root = root
        self.plugins_root = plugins_root


class BaseJobContext(Context):
    """
    Specialized context that subcommands may use.

    For instance `dev`, `local` and `k8s` define custom runners to run jobs.
    """

    def job_runner(self, config: Config) -> BaseJobRunner:
        """
        Return a runner capable of running docker-compose/kubectl commands.
        """
        raise NotImplementedError
