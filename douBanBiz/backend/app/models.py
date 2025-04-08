from app import db

# 电影和演员的多对多关系表
movie_actor = db.Table('movie_actor',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
    db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'), primary_key=True)
)

# 电影和导演的多对多关系表
movie_director = db.Table('movie_director',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
    db.Column('director_id', db.Integer, db.ForeignKey('director.id'), primary_key=True)
)

# 电影和国家的多对多关系表
movie_country = db.Table('movie_country',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
    db.Column('country_id', db.Integer, db.ForeignKey('country.id'), primary_key=True)
)

# 电影和类型的多对多关系表
movie_genre = db.Table('movie_genre',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True)
)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    release_year = db.Column(db.String(10))
    
    # 关联关系
    actors = db.relationship('Actor', secondary=movie_actor, lazy='subquery',
                            backref=db.backref('movies', lazy=True))
    directors = db.relationship('Director', secondary=movie_director, lazy='subquery',
                            backref=db.backref('movies', lazy=True))
    countries = db.relationship('Country', secondary=movie_country, lazy='subquery',
                            backref=db.backref('movies', lazy=True))
    genres = db.relationship('Genre', secondary=movie_genre, lazy='subquery',
                            backref=db.backref('movies', lazy=True))
    
    def __repr__(self):
        return f'<Movie {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
            'actors': [actor.name for actor in self.actors],
            'directors': [director.name for director in self.directors],
            'countries': [country.name for country in self.countries],
            'genres': [genre.name for genre in self.genres]
        }

class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Actor {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'movie_count': len(self.movies)
        }

class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Director {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'movie_count': len(self.movies)
        }

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Country {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'movie_count': len(self.movies)
        }

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Genre {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'movie_count': len(self.movies)
        } 