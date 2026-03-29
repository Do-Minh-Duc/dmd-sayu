#include <iostream>

// Giả định lớp Point đã được định nghĩa như sau
class Point {
public:
    int x, y;
    Point(int x = 0, int y = 0) : x(x), y(y) {}
};

class LineSegment {
private:
    // Thuộc tính private: hai điểm đầu mút
    Point d1, d2;

public:
    // 1. Hàm xây dựng mặc định, không đối số
    // Khởi tạo d1(8, 5) và d2(1, 0)
    LineSegment() : d1(8, 5), d2(1, 0) {}

    // 2. Hàm xây dựng có đối số: LineSegment(Point d1, Point d2)
    // Lấy d1 và d2 làm hai đầu mút, không tạo thêm điểm mới
    LineSegment(Point p1, Point p2) : d1(p1), d2(p2) {}

    // 3. Hàm xây dựng 4 đối số: LineSegment(int x1, int y1, int x2, int y2)
    // Tạo đoạn thẳng từ các tọa độ rời rạc
    LineSegment(int x1, int y1, int x2, int y2) : d1(x1, y1), d2(x2, y2) {}

    // 4. Hàm xây dựng sao chép: LineSegment(LineSegment S)
    // Thực hiện sao chép sâu (Deep Copy)
    LineSegment(const LineSegment &s) {
        this->d1 = s.d1;
        this->d2 = s.d2;
    }

    // Hàm hỗ trợ để kiểm tra kết quả
    void display() {
        std::cout << "LineSegment [(" << d1.x << ", " << d1.y << ") to (" 
                  << d2.x << ", " << d2.y << ")]" << std::endl;
    }
};

int main() {
    // Thử nghiệm các hàm xây dựng
    LineSegment l1; // Mặc định
    l1.display();

    Point pA(2, 2), pB(4, 4);
    LineSegment l2(pA, pB); // 2 đối số Point
    l2.display();

    LineSegment l3(0, 0, 10, 10); // 4 đối số int
    l3.display();

    LineSegment l4(l3); // Sao chép
    l4.display();

    return 0;
}