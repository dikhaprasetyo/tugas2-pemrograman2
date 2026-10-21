class Produk:

  def __init__(self, nama, harga, jumlah):
    self.nama = nama
    self.harga = harga
    self.jumlah = jumlah

  def hitung_total_produk(self):
    return self.harga * self.jumlah

  def tampilkan_info(self):
    total_produk = self.hitung_total_produk()
    print(f"- {self.nama} ({self.jumlah} x Rp{self.harga:,}): Rp{total_produk:,}")

  @staticmethod
  def hitung_diskon(total_seluruh):
    if total_seluruh > 5000:
      return total_seluruh * 0.05
    return 0