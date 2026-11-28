"""The GitLab CI file (.gitlab-ci.yml) runs the same offline checks as
.github/workflows/tests.yml and reuses this repository's own scripts, so it cannot
drift away from them or point at a file that has been moved or renamed."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GITLAB = ROOT / ".gitlab-ci.yml"
GITHUB = ROOT / ".github/workflows/tests.yml"
# A repository path a step runs or reads: scripts/build/android.sh, personas.json,
# demo-app... Ends on a name, so a sentence's trailing dot is not read as part of it.
REFERENCE = re.compile(r"\b(?:scripts|docs|briefs|tests|demo-app)/[\w./-]*\w")


class GitLabCI(unittest.TestCase):
    def setUp(self):
        self.text = GITLAB.read_text(encoding="utf-8")

    def test_every_referenced_file_exists(self):
        missing = sorted(r for r in set(REFERENCE.findall(self.text)) if not (ROOT / r).exists())
        self.assertEqual(missing, [])

    def test_it_runs_the_offline_checks_of_the_github_workflow(self):
        github = GITHUB.read_text(encoding="utf-8")
        for command in ("python3 -m unittest discover -s tests", "shellcheck -S warning"):
            self.assertIn(command, github)
            self.assertIn(command, self.text)

    def test_the_android_job_reuses_the_repository_scripts(self):
        self.assertIn("scripts/build/android.sh", self.text)
        self.assertIn("scripts/android/run_agent.sh", self.text)


if __name__ == "__main__":
    unittest.main()
