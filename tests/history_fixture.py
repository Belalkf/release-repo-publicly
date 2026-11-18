import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/release-repo-publicly/scripts/audit_history.py'
spec = importlib.util.spec_from_file_location('history_audit', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class HistoryFixture(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Synthetic maintainer')
        self.git('config', 'user.email', 'fixture@users.noreply.github.com')


    def git(self, *arguments):
        return subprocess.run(['git', '-C', str(self.root), *arguments],
                              capture_output=True, check=True, timeout=10)


    def commit(self):
        self.git('add', '-A')
        self.git('commit', '-qm', 'Synthetic fixture')


    def snapshot_git_files(self):
        return {str(path.relative_to(self.root)): path.read_bytes()
                for path in (self.root / '.git').rglob('*') if path.is_file()}
