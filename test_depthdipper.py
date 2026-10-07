import unittest
import depthdipper as p
class DepthTests(unittest.TestCase):
    def test_scalar(self):self.assertEqual(p.analyze(b'1')['max_value_depth'],0)
    def test_array(self):self.assertEqual(p.analyze(b'[1,2]')['types'],{'array':1,'number':2})
    def test_nested(self):self.assertEqual(p.analyze(b'{"x":[[0]]}')['max_value_depth'],3)
    def test_empty_array(self):self.assertEqual(p.analyze(b'[]')['values'],1)
    def test_empty_object(self):self.assertEqual(p.analyze(b'{}')['types'],{'object':1})
    def test_bool(self):self.assertEqual(p.analyze(b'true')['types'],{'boolean':1})
    def test_null(self):self.assertEqual(p.analyze(b'null')['types'],{'null':1})
    def test_string(self):self.assertEqual(p.analyze(b'"1"')['types'],{'string':1})
    def test_overflow(self):self.assertEqual(p.analyze(b'1e9999')['types'],{'number':1})
    def test_keys_not_values(self):self.assertEqual(p.analyze(b'{"x":1}')['values'],2)
    def test_duplicate(self):
        with self.assertRaises(ValueError):p.analyze(b'{"x":1,"x":2}')
    def test_constant(self):
        with self.assertRaises(ValueError):p.analyze(b'NaN')
    def test_bad(self):
        for b in (b'',b'\xff',b'1 2'):
            with self.assertRaises(ValueError):p.analyze(b)
    def test_hidden(self):self.assertNotIn('secret-marker',str(p.analyze(b'{"secret-marker":"secret-marker"}')))
    def test_cap(self):
        with self.assertRaises(ValueError):p.analyze(b' '*1048577)
    def test_branch(self):self.assertEqual(p.analyze(b'[{},[1,2],null]')['values'],6)
if __name__=='__main__':unittest.main()
