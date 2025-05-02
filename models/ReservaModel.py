from database import db

class ReservaModel(db.Model):
    __tablename__ = 'reserva'

    id = db.Column(db.Integer, primary_key=True)
    sala_id = db.Column(db.Integer, db.ForeignKey('sala.id'), nullable=False)
    horario_inicio = db.Column(db.DateTime, nullable=False)
    horario_fim = db.Column(db.DateTime, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "sala_id": self.sala_id,
            "horario_inicio": self.horario_inicio.isoformat(),
            "horario_fim": self.horario_fim.isoformat(),
            "professor_id": self.professor_id,
            "turma_id": self.turma_id
        }
