import datetime
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import or_, and_, func
from sqlalchemy.orm import aliased

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Main(db.Model):
    __tablename__ = "Main"
    MainId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Content = db.Column(db.String(128),  nullable=True)
    A =db.relationship("A",backref=db.backref('Main', lazy="joined"),lazy="dynamic")
    B = db.relationship("B", backref="Main", lazy="dynamic")
    C = db.relationship("C", backref="Main", lazy="dynamic")
    D = db.relationship("D", backref="Main", lazy="dynamic")

    def __init__(
            self,
            Content=None,
    ):
        self.Content = Content


class A(db.Model):
    __tablename__ = "A"
    AId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    MainId = db.Column(db.Integer, db.ForeignKey("Main.MainId"), nullable=False)
    Content = db.Column(db.String(128),  nullable=True)

    def __init__(
            self,
            MainId,
            Content=None,
    ):
        self.MainId = MainId
        self.Content = Content

class B(db.Model):
    __tablename__ = "B"
    BId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    MainId = db.Column(db.Integer, db.ForeignKey("Main.MainId"), nullable=False)
    Content = db.Column(db.String(128),  nullable=True)

    def __init__(
            self,
            MainId,
            Content=None,
    ):
        self.MainId = MainId
        self.Content = Content

class C(db.Model):
    __tablename__ = "C"
    CId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    MainId = db.Column(db.Integer, db.ForeignKey("Main.MainId"), nullable=False)
    Content = db.Column(db.String(128),  nullable=True)

    def __init__(
            self,
            MainId,
            Content=None,
    ):
        self.MainId = MainId
        self.Content = Content

class D(db.Model):
    __tablename__ = "D"
    DId = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    MainId = db.Column(db.Integer, db.ForeignKey("Main.MainId"), nullable=False)
    Content = db.Column(db.String(128),  nullable=True)

    def __init__(
            self,
            MainId,
            Content=None,
    ):
        self.MainId = MainId
        self.Content = Content


class ProjectFile(db.Model):
    __tablename__ = "ProjectFile"
    ProjectFileId = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    Name = db.Column(db.String(128), nullable=False)
    ProjectLog = db.relationship('CommitFile',
                                  backref=db.backref('ProjectFile', lazy="joined"), lazy="dynamic")

    def __init__(
            self,
            Name,
    ):
        self.Name = Name

class CommitFile(db.Model):
    __tablename__ = "CommitFile"
    CommitFileId = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ProjectLogId = db.Column(db.Integer, db.ForeignKey("ProjectLog.ProjectLogId"), nullable=False)
    ProjectFileId = db.Column(db.Integer, db.ForeignKey("ProjectFile.ProjectFileId"), nullable=False)

    def __init__(
            self,
            ProjectLogId,
            ProjectFileId,
    ):
        self.ProjectLogId = ProjectLogId
        self.ProjectFileId = ProjectFileId

class ProjectLog(db.Model):
    __tablename__ = "ProjectLog"
    ProjectLogId = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    Name = db.Column(db.String(128), nullable=False)
    ProjectFile = db.relationship('CommitFile',
                               backref=db.backref('ProjectLog', lazy="joined"), lazy="dynamic")

    def __init__(
            self,
            Name,
    ):
        self.Name = Name

if __name__ == '__main__':
    manager.run()
