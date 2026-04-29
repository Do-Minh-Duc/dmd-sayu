import json 

class CanBo:
    def __init__(self,ho_ten,tuoi,gioi_tinh,dia_chi):
        self.ho_ten =ho_ten
        self.tuoi =tuoi
        self.gioi_tinh=gioi_tinh
        self.dia_chi=dia_chi

    def to_dict(self): #Bước quan trọng
        return{
            "ho_ten": self.ho_ten;
            "tuoi": self.tuoi;
            "gioi_tinh": self.gioi_tinh;
            "dia_chi": self.dia_chi;
            "loai": self.__class__.__name__,
        }
        
    @classmethod
    def from_dict(cls, d):   #phục hồi to dict
        return cls(d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"])

#  === Lưu ===
danh_sach = [
    CanBo("Nguyen Van A", 30, "Nam", "Hanoi"),
    CongNhan("Le Thi B", 25, "Nu", "HCM"),
]
data = [cb.to_dict() for cb in danh_sach]
with open("can_bo.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# === Tải ===
with open("can_bo.json", "r", encoding="utf-8") as f:
    raw = json.load(f)
    
# Khôi phục đúng loại theo loại
ds_loaded = [CanBo.from_dict(d) for d in raw]
for cb in ds_loaded:
    print(cb)