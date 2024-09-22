class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="New")
    interactions = db.relationship('Interaction', backref='lead', lazy=True)
    tasks = db.relationship('Task', backref='lead', lazy=True)
