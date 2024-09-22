class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="New")
    interactions = db.relationship('Interaction', backref='lead', lazy=True)
    tasks = db.relationship('Task', backref='lead', lazy=True)



class Interaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    date = db.Column(db.DateTime, default=db.func.now())
    interaction_type = db.Column(db.String(50))
    notes = db.Column(db.Text)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'), nullable=False)
    task_name = db.Column(db.String(200), nullable=False)
    due_date = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
