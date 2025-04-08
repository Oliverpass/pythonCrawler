from app import app
from app.data_loader import load_data
import os

if __name__ == '__main__':
    # 检查数据库文件是否存在，不存在则导入数据
    db_path = 'app/movies.db'
    if not os.path.exists(db_path):
        print("初始化数据库并导入电影数据...")
        load_data("movies.json")
        print("数据导入完成！")
    
    app.run(debug=True) 