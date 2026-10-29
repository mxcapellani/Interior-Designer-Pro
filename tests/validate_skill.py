from pathlib import Path
import re,sys,yaml,importlib.util
B=Path('.agents/skills/interior-designer-pro')
def validate(root):
 root=Path(root);errors=[]
 for p in ('README.md','LICENSE','CHANGELOG.md','docs/SOURCE_SPECIFICATION.md','tests/acceptance-tests.md','.github/workflows/validate.yml',str(B/'SKILL.md')):
  if not (root/p).is_file() or not (root/p).read_text().strip():errors.append('missing '+p)
 if errors:return errors
 text=(root/B/'SKILL.md').read_text()
 try:
  assert text.startswith('---\n');d=yaml.safe_load(text.split('---',2)[1]);assert d['name']=='interior-designer-pro' and isinstance(d['description'],str) and len(d['description'])>40
 except Exception:errors.append('invalid metadata')
 for t in ('REGRA INVIOLÁVEL: CÂMERA','CAPACIDADE 9','RECONCILIAÇÃO OPERACIONAL','reference_available=false','Não produzir uma terceira versão'):
  if t not in text:errors.append('missing operational rule '+t)
 for p in root.rglob('*.md'):
  for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if '://' not in link and not link.startswith('#'):
    target=(p.parent/link.split('#')[0]).resolve()
    if not target.is_relative_to(root.resolve()) or not target.exists():errors.append('bad link '+link)
 try:
  spec=importlib.util.spec_from_file_location('contract',root/B/'scripts/validate_output.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
  for p in list((root/'examples').glob('*.json'))+[root/B/'assets/reference-template.json']:m.validate(m.parse(p.read_text()))
 except Exception as e:errors.append('invalid example '+str(e))
 return errors
if __name__=='__main__':
 errors=validate(Path(__file__).resolve().parents[1]);print('\n'.join(errors) if errors else 'PASS: package, metadata, links and JSON examples');sys.exit(bool(errors))
