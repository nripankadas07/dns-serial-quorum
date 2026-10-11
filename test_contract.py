import unittest
from dns_serial_quorum import relation,evaluate
class Contract(unittest.TestCase):
    def data(self,vs,expected=0,required=1):return {'expected':expected,'required':required,'observations':[{'server':'ns'+str(i),'serial':v} for i,v in enumerate(vs)]}
    def test_equal(self):self.assertEqual(relation(42,42),'equal')
    def test_ahead(self):self.assertEqual(relation(43,42),'ahead')
    def test_behind(self):self.assertEqual(relation(41,42),'behind')
    def test_wrap_ahead(self):self.assertEqual(relation(0,4294967295),'ahead')
    def test_wrap_behind(self):self.assertEqual(relation(4294967295,0),'behind')
    def test_half_range(self):self.assertEqual(relation(2147483648,0),'ambiguous')
    def test_half_range_reverse(self):self.assertEqual(relation(0,2147483648),'ambiguous')
    def test_quorum(self):self.assertTrue(evaluate(self.data([0,0,1],required=2))['quorum_met'])
    def test_ahead_not_quorum(self):self.assertFalse(evaluate(self.data([1,1]))['quorum_met'])
    def test_unavailable(self):self.assertEqual(evaluate(self.data([None,0]))['counts']['unavailable'],1)
    def test_all_equal(self):self.assertTrue(evaluate(self.data([0,0]))['all_equal'])
    def test_mixed_not_all(self):self.assertFalse(evaluate(self.data([0,None]))['all_equal'])
    def test_duplicates(self):
        d=self.data([0,0]);d['observations'][1]['server']='ns0'
        with self.assertRaises(ValueError):evaluate(d)
    def test_invalid_serials(self):
        for v in (-1,4294967296,True,'1'):
            with self.subTest(v=v),self.assertRaises(ValueError):relation(v,0)
    def test_impossible_quorum(self):
        with self.assertRaises(ValueError):evaluate(self.data([0],required=2))
    def test_empty(self):
        with self.assertRaises(ValueError):evaluate(self.data([]))
