# ABSA for Vietnamese E-commerce Review
Project ứng dụng Mạng tích chập đồ thị nâng cao ngữ nghĩa và cú pháp cho bài toán Phân tích quan điểm mức khía cạnh và áp dụng vào dữ liệu tiếng Việt.


## Dữ liệu
Sử dụng 2 bộ dữ liệu tiếng Việt cho phân tích quan điểm mức khía cạnh, bao gồm các đánh giá của người dùng về điện thoại di động: <br> UIT-ViSFD [1] và UIT-ViSD4SA [2]. <br>

## Mô hình
Áp dụng mô hình SSEGCN được đề xuất bởi Zheng Zhang và cộng sự (2022) [3]

## Cấu hình
Mô hình được huấn luyện trên CPU với cài đặt cấu hình như sau: <br> 
- Số lượng CPU: 2
- Vendor ID: GenuineIntel
- CPU Family: 6
- Model: 79
- Tên Model: Intel(R) Xeon(R) CPU @ 2.20GHz
- Microcode: 0x1
- Cpu MHz: 2200.000
- Dung lượng Cache: 56320 KB
- Số nhân CPU: 1
- Cpuid level: 13
- Bogomips: 4400.00
- Address Sizes: 46 bits vật lý và 48 bits ảo
- 1 GPU Tesla T4

## Cách chạy

```
python preprocess_data.py

sh build_vocab.sh

sh run.sh
```

## Tham khảo

1. https://github.com/LuongPhan/UIT-ViSFD
2. https://github.com/kimkim00/UIT-ViSD4SA
3. https://github.com/zhangzheng1997/SSEGCN-ABSA
