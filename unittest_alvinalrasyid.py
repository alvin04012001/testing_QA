# ALVIN AR-RASYID
# 201011401787

# Modul yang akan diuji
def hitung_jumlah_elemen(daftar):
    return len(daftar)

# Modul pengujian unit
import unittest

class TestHitungJumlahElemen(unittest.TestCase):

    # Tes kasus 1: Tes jika daftar kosong
    def test_daftar_kosong(self):
        daftar = []
        hasil = hitung_jumlah_elemen(daftar)
        self.assertEqual(hasil, 0)

    # Tes kasus 2: Tes jika daftar memiliki 3 elemen
    def test_daftar_tiga_elemen(self):
        daftar = [1, 2, 3]
        hasil = hitung_jumlah_elemen(daftar)
        self.assertEqual(hasil, 3)

    # Tes kasus 3: Tes jika daftar memiliki 100 elemen
    def test_daftar_seratus_elemen(self):
        daftar = list(range(1, 101))
        hasil = hitung_jumlah_elemen(daftar)
        self.assertEqual(hasil, 100)

if __name__ == '__main__':
    unittest.main()
