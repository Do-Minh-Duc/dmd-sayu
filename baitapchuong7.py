import json
import csv
class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
    def __str__(self):
        return f'CanBo - Ho ten: {self.ho_ten}, Tuoi: {self.tuoi}, Gioi tinh: {self.gioi_tinh}, Dia chi: {self.dia_chi}'

    def to_dict(self):
        return {
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "gioi_tinh": self.gioi_tinh,
            "dia_chi": self.dia_chi,
            "loai": self.__class__.__name__,
        }
@classmethod
def from_dict(cls, d):
    return cls(d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"])    
class CongNhan(CanBo):
    def from dict(cls, d):
        return cls(d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"])
    def __str__(self):
        return f'CongNhan - Ho ten: {self.ho_ten}, Tuoi: {self.tuoi}, Gioi tinh: {self.gioi_tinh}, Dia chi: {self.dia_chi}'
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["loai"] = "CongNhan"
        return base_dict
@classmethod
def from_dict(cls, d):
    return cls(d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"])
class KySu(CanBo):
    def init (self, ho_ten, tuoi, gioi_tinh, dia_chi):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao
    def __str__(self):
        return f'KySu - Ho ten: {self.ho_ten}, Tuoi: {self.tuoi}, Gioi tinh: {self.gioi_tinh}, Dia chi: {self.dia_chi}, Nganh dao tao: {self.nganh_dao_tao}'
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["nganh dao_tao"] = self.nganh_dao_tao
        return base_dict
@classmethod
def from_dict(cls, d):
    return cls(d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"], d["nganh_dao_tao"])

class NhanVien(CanBo):
    def init (self, ho_ten, tuoi, gioi_tinh, dia_chi):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec
    def __str__(self):
        return f'NhanVien - Ho ten: {self.ho_ten}, Tuoi: {self.tuoi}, Gioi tinh: {self.gioi_tinh}, Dia chi: {self.dia_chi}, Cong viec: {self.cong_viec}'
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["cong_viec"] = self.cong_viec
        return base_dict
@classmethod
def from_dict(cls, d):
    return cls(d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"], d["cong_viec"])
# Lưu vào file JSON
danh_sach = [
    CanBo("Nguyen Van A", 30, "Nam", "Hanoi"),
    CongNhan("Le Thi B", 25, "Nu", "HCM"),
    KySu("Tran Van C", 28, "Nam", "Da Nang", "CNTT"),
    NhanVien("Pham Thi D", 32, "Nu", "Hue", "Hanh chinh"),
]
data = [cb.to_dict() for cb in danh_sach]
with open("can_bo.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
# Tải từ file JSON
with open("can_bo.json", "r", encoding="utf-8") as f:
    raw = json.load(f)
ds_loaded = []
for d in raw:
    loai = d.get("loai")
    if loai == "CanBo":
        ds_loaded.append(CanBo.from_dict(d))
    elif loai == "CongNhan":
        ds_loaded.append(CongNhan.from_dict(d))
    elif loai == "KySu":
        ds_loaded.append(KySu.from_dict(d))
    elif loai == "NhanVien":    
        ds_loaded.append(NhanVien.from_dict(d))
for cb in ds_loaded:
    print(cb)
LOAI_MAP = {
    "CanBo": CanBo,
    "CongNhan": CongNhan,
    "KySu": KySu,
    "NhanVien": NhanVien
}
with open("canbo.json", "r",
           encoding="utf-8") as f:
    for d in json.load(f):
        cls = LOAI_MAP.get(
            d["loai"], CanBo)
        cb = cls.from_dict(d)
        ds[cb.ho_ten] = cb

