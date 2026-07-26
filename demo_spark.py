from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round as spark_round, sum as spark_sum

# 1. Khởi tạo Spark Session
spark = SparkSession.builder \
    .appName("ThucHanhSpark") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# 2. Đọc file CSV dữ liệu ảo vừa tạo
print("\n📥 Đang đọc dữ liệu bằng Spark...")
df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)

# Hiển thị cấu trúc cột (Schema) và 5 dòng đầu
df.printSchema()
df.show(5)

# 3. Thêm cột "TongTien" = SoLuong * DonGia (dùng Python)
df_with_total = df.withColumn("TongTien", spark_round(col("SoLuong") * col("DonGia"), 2))

# 4. Thực hành dùng Spark SQL
df_with_total.createOrReplaceTempView("sales")

print("\n📊 THỐNG KÊ DOANH THU THEO THÀNH PHỐ VÀ DẠNG SẢN PHẨM (SPARK SQL):")
query = """
    SELECT 
        ThanhPho,
        DanhMuc,
        SUM(SoLuong) as TongSoLuong,
        ROUND(SUM(TongTien), 2) as TongDoanhThu
    FROM sales
    GROUP BY ThanhPho, DanhMuc
    ORDER BY TongDoanhThu DESC
"""
result = spark.sql(query)
result.show(10)

# 5. Lưu kết quả ra file định dạng PARQUET (tối ưu của Spark)
print("💾 Đang lưu kết quả ra định dạng Parquet...")
result.write.mode("overwrite").parquet("output_doanh_thu.parquet")

print("🎉 Hoàn tất!")
spark.stop()