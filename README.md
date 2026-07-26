# ⚡ Apache Spark Learning Journey

Nhật ký ghi lại từng bước cài đặt, cấu hình và thực hành **Apache Spark (PySpark)** trên macOS (Apple Silicon / VS Code) từ con số 0.

---

## 📌 Nội dung dự án

- **`generate_data.py`**: Script tự động tạo 100.000 dòng dữ liệu bán hàng giả lập (`sales_data.csv`).
- **`demo_spark.py`**: Ví dụ thực hành thao tác dữ liệu cơ bản bằng **PySpark DataFrame** và **Spark SQL**, sau đó xuất kết quả ra định dạng **Parquet**.
- **`Huong_Dan_Hoc_Spark.pdf`**: Tài liệu tóm tắt lộ trình 4 bước tiếp cận Spark siêu dễ hiểu.

---

## 🛠 Những gì đã thiết lập (Setup & Troubleshooting)

1. **Cấu hình Environment Variables (`~/.zshrc`):**
   - Thiết lập `SPARK_HOME` trỏ đến thư mục cài đặt Apache Spark qua Homebrew.
   - Thêm đường dẫn `bin` vào `PATH`.

2. **Cài đặt & Sửa lỗi Java Runtime (JVM):**
   - Cài đặt **OpenJDK 17** qua Homebrew (`brew install openjdk@17`).
   - Khắc phục lỗi `PySparkRuntimeError: [JAVA_GATEWAY_EXITED]` bằng cách cấu hình chuẩn `JAVA_HOME` và tạo symlink hệ thống.

3. **Cài đặt môi trường Python:**
   - Cài đặt thư viện `pyspark` bằng `pip`.
   - Cài đặt Extension **Python** và **vscode-parquet** trong VS Code để xem dữ liệu nén Parquet.

---

## 🚀 Cách chạy dự án

1. **Tạo dữ liệu ảo để thực hành:**
   ```bash
   python3 generate_data.py
