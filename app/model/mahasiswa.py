from app import db

class Mahasiswa(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nik = db.Column(db.String(30), nullable=False)
    nama = db.Column(db.String(13), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Mahasiswa{}>'.format(self.name)