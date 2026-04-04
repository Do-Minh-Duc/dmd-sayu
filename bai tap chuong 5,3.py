class QLCB:
    def __init(self):
        self.__canBoList = []
    def themmoi(self):
        print("Nhập thông tin cán bộ mới:")
        ten = input("Tên: ")
        tuoi = int(input("Tuổi: "))    
        gioiTinh = input("Giới tính: ")
        diaChi = input("Địa chỉ: ")

    if loai = "1"
       bac =input (" nhâp vào bậc công nhân:")
       cb = CongNhan(ten, tuoi, gioiTinh, diaChi, bac)
    elif loai = "2"
        nganh = input("Nhập ngành nghề của kỹ sư: ")
        cb = KySu(ten, tuoi, gioiTinh, diaChi, nganh)
    elif loai = "3"
        congviec = input("Nhập công việc của nhân viên: ")
        cb = NhanVien(ten, tuoi, gioiTinh, diaChi, congviec)
    else:
        print("Loại cán bộ không hợp lệ.")
    
    self.danhSachCanBo.append(cb)

def timkiem(self):
    ten = input("Nhập tên cán bộ cần tìm: ")
    for cb in self.danhSachCanBo:
        if cb.get_ten() == ten:
            print("Thông tin cán bộ:")
            cb.inThongTin()
            return
    print("Không tìm thấy cán bộ với tên đã nhập.")