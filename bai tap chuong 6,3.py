import mathgi
class MauSoBangKhong(Exception):
    def __init__(self):
        self.message = "Mẫu số không được bằng 0"
        super().__init__(self.message)

# 2. Xây dựng lớp PhanSo
class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau
    @property
    def tu(self):
        return self.__tu

    @tu.setter
    def tu(self, v):
        self.__tu = v
    @property 
    def mau(self):
        return self.__mau

    @mau.setter
    def mau(self, v):
        if v == 0:
            raise MauSoBangKhong()
        self.__mau = v
    def toi_gian(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu = self.tu // ucln
        self.mau = self.mau // ucln
        if self.mau < 0:
            self.tu = -self.tu
            self.mau = -self.mau
        return self

    def is_toi_gian(self):
        return math.gcd(self.tu, self.mau) == 1

    # --- Operator Overloading (Toán tử) ---
    def __add__(self, other):
        tu_moi = self.tu * other.mau + other.tu * self.mau
        mau_moi = self.mau * other.mau
        return PhanSo(tu_moi, mau_moi).toi_gian()

    def __sub__(self, other):
        tu_moi = self.tu * other.mau - other.tu * self.mau
        mau_moi = self.mau * other.mau
        return PhanSo(tu_moi, mau_moi).toi_gian()

    def __mul__(self, other):
        tu_moi = self.tu * other.tu
        mau_moi = self.mau * other.mau
        return PhanSo(tu_moi, mau_moi).toi_gian()

    def __truediv__(self, other):
        if other.tu == 0:
            raise ValueError("Không thể chia cho phân số có tử số bằng 0")
        tu_moi = self.tu * other.mau
        mau_moi = self.mau * other.tu
        return PhanSo(tu_moi, mau_moi).toi_gian()
    def __eq__(self, other):
        return self.tu * other.mau == other.tu * self.mau

    def __lt__(self, other):
        return self.tu * other.mau < other.tu * self.mau

    def __gt__(self, other):
        return self.tu * other.mau > other.tu * self.mau
    def __str__(self):
        if self.mau == 1:
            return f'{self.tu}'
        return f'{self.tu}/{self.mau}'

    def __repr__(self):
        return f'PhanSo({self.tu}, {self.mau})'

    def __hash__(self):
        u = math.gcd(self.tu, self.mau)
        t = self.tu // u
        m = self.mau // u
        if m < 0: t, m = -t, -m
        return hash((t, m))
def main():
    danh_sach = []
    print("Nhập danh sách phân số (Nhập tử số là 'q' để dừng):")
    
    while True:
        try:
            input_tu = input("\nNhập tử số: ")
            if input_tu.lower() == 'q': break
            
            tu = int(input_tu)
            mau = int(input("Nhập mẫu số: "))
            
            ps = PhanSo(tu, mau)
            danh_sach.append(ps)
            
        except MauSoBangKhong as e:
            print(f"Lỗi nghiệp vụ: {e}")
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")

    if danh_sach:
        print("\n--- Danh sách phân số tối giản ---")
        for ps in danh_sach:
            print(ps.toi_gian(), end=" | ")
        danh_sach.sort()
        
        print("\n\n--- Danh sách sau khi sắp xếp tăng dần ---")
        print(" | ".join(str(ps) for ps in danh_sach))
    else:
        print("Danh sách trống.")

if __name__ == "__main__":
    main()