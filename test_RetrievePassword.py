import unittest
from RetrievePasswordTest import*


class TestRetrieve(unittest.TestCase):
    
    
    def test_RetrievePassword(self):
        df = pd.read_csv('./Register.csv',index_col=False)
        test_f = df.loc[df['user_name'] == "Asus"]
        test_f = str(test_f['password'].values)
        result = RetrievePasswordTest("Asus")
        self.assertEqual(result, test_f)
        
        
if __name__ == '__main__':
    unittest.main()