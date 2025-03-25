import unittest

# Fungsi yang akan diuji
def tambah(a, b):
    return a + b

# Membuat kelas unit test
class TestTambah(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)
        self.assertEqual(tambah(-1, 1), 0)
        self.assertEqual(tambah(0, 0), 0)

# Menjalankan unit test
if __name__ == '__main__':
    unittest.main()
