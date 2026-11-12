"""Ensure cumulative packages carry the root documents linked by current READMEs."""
from pathlib import Path
import shutil, unittest, uuid, zipfile
from verify_release import verify_release

class ReleaseDocumentsTest(unittest.TestCase):
    def setUp(self):
        self.base=Path(__file__).resolve().parent.parent/'release-assets'
        self.root=self.base/('test-'+uuid.uuid4().hex)
        assert self.root.resolve().is_relative_to(self.base.resolve())
        self.root.mkdir()
        self.names=['README.md','NOTICE.md','AGENTS.md']+[
            'pet/'+name for name in ['pet.json','spritesheet.webp','README.md','NOTICE.md','validation.json','preview/README.md']]
        for name in self.names:
            file=self.root/name
            file.parent.mkdir(parents=True,exist_ok=True)
            file.write_bytes(name.encode())

    def tearDown(self):
        assert self.root.resolve().is_relative_to(self.base.resolve())
        shutil.rmtree(self.root)

    def package(self,names):
        archive=self.root/'test.zip'
        with zipfile.ZipFile(archive,'w') as package:
            for name in names:package.write(self.root/name,name)
        return archive

    def test_accepts_all_linked_root_documents(self):
        self.assertTrue(verify_release(self.root,self.package(self.names))['ok'])

    def test_rejects_local_only_documents(self):
        for name in ('PET_NAMES.md','REVIEW_PLAN.md'):
            with self.subTest(name=name):
                (self.root/name).write_text('local only',encoding='utf-8')
                with self.assertRaisesRegex(AssertionError,'Missing or unexpected'):
                    verify_release(self.root,self.package(self.names+[name]))

if __name__=='__main__':unittest.main()
