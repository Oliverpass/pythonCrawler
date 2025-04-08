from flask import jsonify
from app import app, db
from app.models import Movie, Actor, Director, Country, Genre
from sqlalchemy import func

@app.route('/api/movies', methods=['GET'])
def get_movies():
    """获取所有电影信息"""
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])

@app.route('/api/stats/actors', methods=['GET'])
def get_top_actors():
    """获取出演次数最多的演员"""
    # 使用 SQLAlchemy 计算每个演员的电影数量
    actor_counts = db.session.query(
        Actor.id, Actor.name, func.count(movie_actor.c.movie_id).label("movie_count")
    ).join(
        movie_actor
    ).group_by(
        Actor.id
    ).order_by(
        func.count(movie_actor.c.movie_id).desc()
    ).limit(10).all()
    
    return jsonify([
        {"id": id, "name": name, "movie_count": count}
        for id, name, count in actor_counts
    ])

@app.route('/api/stats/countries', methods=['GET'])
def get_top_countries():
    """获取制片最多的国家"""
    country_counts = db.session.query(
        Country.id, Country.name, func.count(movie_country.c.movie_id).label("movie_count")
    ).join(
        movie_country
    ).group_by(
        Country.id
    ).order_by(
        func.count(movie_country.c.movie_id).desc()
    ).all()
    
    return jsonify([
        {"id": id, "name": name, "movie_count": count}
        for id, name, count in country_counts
    ])

@app.route('/api/stats/directors', methods=['GET'])
def get_top_directors():
    """获取出现次数最多的导演"""
    director_counts = db.session.query(
        Director.id, Director.name, func.count(movie_director.c.movie_id).label("movie_count")
    ).join(
        movie_director
    ).group_by(
        Director.id
    ).order_by(
        func.count(movie_director.c.movie_id).desc()
    ).limit(10).all()
    
    return jsonify([
        {"id": id, "name": name, "movie_count": count}
        for id, name, count in director_counts
    ])

@app.route('/api/stats/genres', methods=['GET'])
def get_genres():
    """获取各类型电影数量"""
    genre_counts = db.session.query(
        Genre.id, Genre.name, func.count(movie_genre.c.movie_id).label("movie_count")
    ).join(
        movie_genre
    ).group_by(
        Genre.id
    ).order_by(
        func.count(movie_genre.c.movie_id).desc()
    ).all()
    
    return jsonify([
        {"id": id, "name": name, "movie_count": count}
        for id, name, count in genre_counts
    ])

from app.models import movie_actor, movie_director, movie_country, movie_genre 