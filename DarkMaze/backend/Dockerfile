# TODO: Install the backend dependency package into the app folder inside the container.

# 使用 Python 3.11 作為基礎映像
FROM python:3.11

# 設置工作目錄
WORKDIR /app

# 複製 requirements.txt 到工作目錄
COPY requirements.txt .

# 安裝 Python 依賴包
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式的源代碼到工作目錄
COPY . .

# 暴露應用程式的端口
EXPOSE 8000

# 運行應用程式
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]