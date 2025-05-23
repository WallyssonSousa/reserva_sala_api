from database import db

class SalaModel(db.Model):
    __tablename__ = 'sala'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    localizacao = db.Column(db.String(150), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    recursos = db.Column(db.String(250), nullable=True)
    disponivel = db.Column(db.Boolean, default=True)
    
    reservas = db.relationship('ReservaModel', backref='sala', lazy=True)

    def to_dict(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "localizacao": self.localizacao,
            "capacidade": self.capacidade,
            "recursos": self.recursos,
            "disponivel": self.disponivel
        }