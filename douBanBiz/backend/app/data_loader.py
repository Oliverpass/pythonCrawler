import json
from app import db, app
from app.models import Movie, Actor, Director, Country, Genre
import os

def load_data(json_file_path):
    """从JSON文件加载数据到数据库"""
    
    # 确保在应用上下文中操作
    with app.app_context():
        # 初始化数据库
        db.drop_all()
        db.create_all()
        
        # 获取JSON文件的绝对路径
        abs_json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', json_file_path)
        
        # 打开JSON文件
        try:
            with open(abs_json_path, 'r', encoding='utf-8') as file:
                movies_data = json.load(file)
        except FileNotFoundError:
            print(f"错误：找不到文件 {abs_json_path}")
            return
        except json.JSONDecodeError:
            print(f"错误：JSON文件格式无效 {abs_json_path}")
            return
        
        print(f"开始导入 {len(movies_data)} 部电影的数据...")
        
        for movie_data in movies_data:
            # 创建电影
            movie = Movie(
                title=movie_data['名称'],
                release_year=movie_data['上映时间']
            )
            
            # 添加演员
            for actor_name in movie_data['演员']:
                actor = Actor.query.filter_by(name=actor_name).first()
                if not actor:
                    actor = Actor(name=actor_name)
                    db.session.add(actor)
                movie.actors.append(actor)
            
            # 添加导演
            for director_name in movie_data['导演']:
                director = Director.query.filter_by(name=director_name).first()
                if not director:
                    director = Director(name=director_name)
                    db.session.add(director)
                movie.directors.append(director)
            
            # 添加国家
            for country_name in movie_data['国家']:
                country = Country.query.filter_by(name=country_name).first()
                if not country:
                    country = Country(name=country_name)
                    db.session.add(country)
                movie.countries.append(country)
            
            # 添加类型
            for genre_name in movie_data['电影类型']:
                genre = Genre.query.filter_by(name=genre_name).first()
                if not genre:
                    genre = Genre(name=genre_name)
                    db.session.add(genre)
                movie.genres.append(genre)
            
            db.session.add(movie)
        
        # 提交所有更改
        db.session.commit()
        
        print(f"成功导入 {len(movies_data)} 部电影的数据")

if __name__ == "__main__":
    # 可以直接执行此脚本导入数据
    # python -m app.data_loader
    load_data("movies.json") 