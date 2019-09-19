class Nur (object) :
    def __init__(self, nama, nim, matkul) :
        self.nama = nama
        self.nim = nim
        self.matkul = matkul
    
    def cetakdata(self):
        print("Nama   : ", self.nama)
        print("Nim    : ", self.nim)
        print("Matkul : ", self.matkul)
        
class NurInayah (Nur):
    def __init__(self, nama, nim, matkul, kelas) :
        self.nama = nama
        self.nim = nim
        self.matkul = matkul
        self.kelas = kelas
        
    def cetakdata(self):
        print("Nama        : ", self.nama)
        print("Nim         : ", self.nim)
        print("Mata Kuliah : ", self.matkul)
        print("Kelas       : ", self.kelas)
        
def main ():
    NurInayah1 = NurInayah('Nur Inayah Yusuf', '1829140001', 'Pemrograman Lanjut', 'Tekom B')
    NurInayah1.cetakdata()
       
if __name__== "__main__":
    main()
