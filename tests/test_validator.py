import unittest,importlib.util,json,copy
from pathlib import Path
from validate_skill import validate,B
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('output',R/B/'scripts/validate_output.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class Tests(unittest.TestCase):
 def setUp(self):self.d=json.loads((R/'examples/japandi-reference.json').read_text())
 def test_package(self):self.assertEqual(validate(R),[])
 def test_reference(self):self.assertTrue(m.validate(self.d))
 def test_no_reference(self):self.assertTrue(m.validate(json.loads((R/'examples/no-reference.json').read_text())))
 def test_missing_key(self):
  del self.d['camera']
  with self.assertRaises(ValueError):m.validate(self.d)
 def test_wrong_camera(self):
  self.d['camera']['preservation_rule']='new camera'
  with self.assertRaises(ValueError):m.validate(self.d)
 def test_reference_flags(self):
  self.d['constraints']['preserve_camera']=False
  with self.assertRaises(ValueError):m.validate(self.d)
 def test_people_disabled_quantity(self):
  self.d['people']['quantity']=1
  with self.assertRaises(ValueError):m.validate(self.d)
 def test_pet_quantity_bool(self):
  self.d['pets']['quantity']=False
  with self.assertRaises(ValueError):m.validate(self.d)
 def test_structural_conflict(self):
  self.d['constraints']['allow_structural_changes']=True
  with self.assertRaises(ValueError):m.validate(self.d)
 def test_duplicate(self):
  with self.assertRaises(ValueError):m.parse('{"a":1,"a":2}')
 def test_nan(self):
  with self.assertRaises(ValueError):m.parse('{"a":NaN}')
 def test_no_reference_rule(self):
  self.d['camera']['reference_available']=False
  with self.assertRaises(ValueError):m.validate(self.d)
if __name__=='__main__':unittest.main()
