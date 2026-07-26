from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadParquet").getOrCreate()

# Đọc toàn bộ thư mục parquet vừa xuất
df = spark.read.parquet("output_doanh_thu.parquet")

# Hiển thị nội dung
df.show()