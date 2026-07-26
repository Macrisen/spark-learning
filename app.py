from pyspark.sql import SparkSession

# 1. Khởi tạo Spark Session
spark = SparkSession.builder \
    .appName("PySpark VS Code Demo") \
    .getOrCreate()

# Giảm bớt các dòng log nhiễu không cần thiết
spark.sparkContext.setLogLevel("ERROR")

# 2. Tạo dữ liệu mẫu
data = [
    ("Nguyễn Văn A", "Công nghệ", 1500),
    ("Trần Thị B", "Kinh doanh", 1200),
    ("Lê Văn C", "Công nghệ", 1800),
    ("Phạm Thị D", "Kinh doanh", 1400)
]
columns = ["HoTen", "PhongBan", "Luong"]

# Tạo DataFrame bằng Python
df = spark.createDataFrame(data, columns)

# 3. Đăng ký thành Bảng ảo để dùng SQL
df.createOrReplaceTempView("bang_nhan_vien")

# 4. Truy vấn bằng câu lệnh SQL
result_sql = spark.sql("""
    SELECT PhongBan, COUNT(*) as SoLuong, AVG(Luong) as LuongTrungBinh
    FROM bang_nhan_vien
    GROUP BY PhongBan
""")

# 5. In kết quả ra màn hình
print("=== KẾT QUẢ XỬ LÝ BẰNG SPARK SQL ===")
result_sql.show()

# 6. Dừng Spark
spark.stop()