"""Validate prompt contract, not language, visual quality or an official API."""
import json,sys
from pathlib import Path
KEYS={'scene_description','style','lighting','materials','camera','composition','resolution','people','pets','constraints'}
RULE='The point of view, camera height, perspective and framing are identical to the original image and must not be changed.'
NOREF='No reference image is available; no original camera has been verified.'
def pairs(items):
 d={}
 for k,v in items:
  if k in d:raise ValueError('duplicate JSON key')
  d[k]=v
 return d
def parse(text):
 return json.loads(text,object_pairs_hook=pairs,parse_constant=lambda x: (_ for _ in ()).throw(ValueError('nonfinite JSON')))
def validate(d):
 if not isinstance(d,dict) or set(d)!=KEYS:raise ValueError('exactly ten canonical keys required')
 if any(not isinstance(v,dict) or not v for v in d.values()):raise ValueError('all sections must be nonempty objects')
 camera=d['camera'];c=d['constraints'];available=camera.get('reference_available')
 if type(available) is not bool:raise ValueError('reference_available must be boolean')
 if camera.get('preservation_rule')!=(RULE if available else NOREF):raise ValueError('incorrect camera evidence rule')
 for k in ('preserve_camera','preserve_framing','preserve_perspective'):
  if c.get(k) is not available:raise ValueError('reference flags inconsistent')
 for k in ('preserve_architecture','preserve_spatial_proportions','allow_structural_changes'):
  if type(c.get(k)) is not bool:raise ValueError('constraint flag must be boolean')
 if c['allow_structural_changes'] and c['preserve_architecture']:raise ValueError('structural flags conflict')
 if not isinstance(c.get('negative_prompt'),list) or not all(isinstance(x,str) and x.strip() for x in c['negative_prompt']):raise ValueError('negative_prompt must be string list')
 for k in ('people','pets'):
  p=d[k];n=p.get('quantity');on=p.get('enabled')
  if type(on) is not bool or type(n) is not int or n<0 or (on and n==0) or (not on and n!=0):raise ValueError('invalid insertion controls')
 return True
if __name__=='__main__':
 try:validate(parse(Path(sys.argv[1]).read_text()));print('PASS: JSON contract only')
 except (ValueError,IndexError,OSError) as e:print(str(e),file=sys.stderr);sys.exit(1)
