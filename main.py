from produk import Produk


def main():
  print("=== SISTEM PEMBELIAN PRODUK ===")

  try:
    jumlah_jenis = int(
        input("Masukkan jumlah produk yang akan dibeli: ")
    )
  except ValueError:
    print("Input tidak valid! Harap masukkan angka bulat.")
    return

  daftar_produk = []

  for i in range(1, jumlah_jenis + 1):
    print(f"\n--- Data Produk ke-{i} ---")
    nama = input("Nama produk : ")
    harga = float(input("Harga produk (Rp) : "))
    jumlah = int(input("Jumlah beli : "))

    produk_baru = Produk(nama, harga, jumlah)
    daftar_produk.append(produk_baru)

  total_seluruh = sum(p.hitung_total_produk() for p in daftar_produk)

  diskon = Produk.hitung_diskon(total_seluruh)
  total_bayar = total_seluruh - diskon

  print("\n=== RINCIAN PEMBELIAN ===")
  for p in daftar_produk:
    p.tampilkan_info()

  print("\n=== HASIL PEMBELIAN ===")
  print(f"Total Pembelian : Rp{int(total_seluruh):,}")
  print(f"Diskon 5%       : Rp{int(diskon):,}")
  print(f"Total Bayar     : Rp{int(total_bayar):,}")


if __name__ == "__main__":
  main()