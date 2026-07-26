import csv
import random
from datetime import datetime, timedelta

# Cấu hình số lượng dòng dữ liệu ảo (bạn có thể tăng lên 1,000,000 nếu muốn nặng hơn)
NUM_ROWS = 100_000

categories = ["Điện thoại", "Laptop", "Phụ kiện", "Gia dụng", "Thời trang"]
cities = ["Hà Nội", "TP.HCM", "Đà Nẵng", "Cần Thơ", "Hải Phòng"]

start_date = datetime(2025, 1, 1)

print(f"⏳ Đang khởi tạo {NUM_ROWS:,} dòng dữ liệu...")

with open("sales_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Viết Header
    writer.writerow(["MaGiaoDich", "NgayGiaoDich", "KhachHangID", "DanhMuc", "ThanhPho", "SoLuong", "DonGia"])
    
    # Sinh dữ liệu ngẫu nhiên
    for i in range(1, NUM_ROWS + 1):
        transaction_id = f"TXN{i:07d}"
        random_days = random.randint(0, 365)
        date = (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")
        customer_id = f"CUST_{random.randint(1000, 9999)}"
        category = random.choice(categories)
        city = random.choice(cities)
        quantity = random.randint(1, 10)
        price = round(random.uniform(50.0, 2000.0), 2)
        
        writer.writerow([transaction_id, date, customer_id, category, city, quantity, price])

print("✅ Đã tạo thành công file 'sales_data.csv'!")