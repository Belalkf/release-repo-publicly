import json
import os
from pathlib import Path
import subprocess
import tempfile
from unittest.mock import patch

from history_fixture import HistoryFixture, module


class HistoryInputTests(HistoryFixture):
    def test_subdirectory_cannot_silently_audit_parent_repository(self):
        (self.root / 'file.txt').write_text('safe')
        self.commit()
        exported = self.root / 'exported-folder'
        exported.mkdir()
        result = module.audit(exported)
        self.assertFalse(result['complete'])
        self.assertEqual(result['inspected_objects'], 0)


    def test_legacy_grafts_cannot_hide_deleted_secret_history(self):
        token = 'gh' + 'p_' + 'D' * 40
        file = self.root / 'file.txt'
        file.write_text(token)
        self.commit()
        file.write_text('safe current content')
        self.commit()
        tip = self.git('rev-parse', 'HEAD').stdout.strip()
        graft = self.root / '.git/info/grafts'
        graft.write_bytes(tip + b'\n')
        original = graft.read_bytes()
        result = module.audit(self.root)
        self.assertFalse(result['complete'])
        self.assertTrue(any('graft' in issue.lower() for issue in result['issues']))
        self.assertEqual(graft.read_bytes(), original)
        self.assertNotIn(token, json.dumps(result))


    def test_partial_clone_is_rejected_before_git_can_fetch_missing_objects(self):
        (self.root / 'file.txt').write_text('safe local fixture')
        self.commit()
        with tempfile.TemporaryDirectory() as other:
            remote = Path(other) / 'remote.git'
            subprocess.run(['git', 'clone', '-q', '--bare', '--no-hardlinks', str(self.root), str(remote)],
                           check=True, capture_output=True, timeout=10)
            self.git('remote', 'add', 'origin', remote.as_uri())
            self.git('config', 'remote.origin.promisor', 'true')
            self.git('config', 'remote.origin.partialclonefilter', 'blob:none')
            oid = self.git('rev-parse', 'HEAD:file.txt').stdout.strip().decode()
            missing = self.root / '.git/objects' / oid[:2] / oid[2:]
            # Only this disposable fixture is altered; Windows enforces Git's read-only bit.
            missing.chmod(0o600)
            missing.unlink()
            before = self.snapshot_git_files()
            result = module.audit(self.root)
            self.assertFalse(result['complete'])
            self.assertTrue(any('partial' in issue.lower() for issue in result['issues']))
            self.assertEqual(self.snapshot_git_files(), before)


    def test_partial_clone_setting_in_included_config_is_not_missed(self):
        (self.root / 'file.txt').write_text('safe')
        self.commit()
        with tempfile.TemporaryDirectory() as other:
            included = Path(other) / 'included.config'
            included.write_text('[remote "origin"]\n\tpromisor = true\n')
            self.git('config', 'include.path', str(included))
            before = self.snapshot_git_files()
            result = module.audit(self.root)
            self.assertFalse(result['complete'])
            self.assertTrue(any('Partial' in issue for issue in result['issues']))
            self.assertEqual(self.snapshot_git_files(), before)


    def test_bare_repository_root_remains_supported(self):
        (self.root / 'file.txt').write_text('safe')
        self.commit()
        with tempfile.TemporaryDirectory() as other:
            target = Path(other) / 'bare.git'
            subprocess.run(['git', 'clone', '-q', '--bare', str(self.root), str(target)],
                           capture_output=True, check=True, timeout=10)
            result = module.audit(target)
        self.assertTrue(result['complete'])
        self.assertEqual(result['commits'], 1)


    def test_linked_worktree_and_its_shared_graft_boundary(self):
        (self.root / 'file.txt').write_text('safe')
        self.commit()
        with tempfile.TemporaryDirectory() as other:
            target = Path(other) / 'linked'
            self.git('worktree', 'add', '--detach', str(target), 'HEAD')
            try:
                self.assertTrue(module.audit(target)['complete'])
                (self.root / '.git/info/grafts').write_bytes(
                    self.git('rev-parse', 'HEAD').stdout)
                result = module.audit(target)
                self.assertFalse(result['complete'])
                self.assertTrue(any('graft' in issue.lower() for issue in result['issues']))
            finally:
                self.git('worktree', 'remove', str(target))
