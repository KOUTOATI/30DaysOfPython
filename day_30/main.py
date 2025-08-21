import os
import uvicorn
import uuid
from datetime import datetime, timedelta
from typing import Optional, List, Literal

from fastapi import FastAPI, Depends, HTTPException, status, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import create_engine, Column, String, Text, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from pydantic import BaseModel, EmailStr, Field, HttpUrl, validator
from slugify import slugify
from passlib.context import CryptContext
from jose import JWTError, jwt

# --- Configuration et variables d'environnement ---
# Chargement des variables d'environnement (simulé ici, mais utilisez dotenv en production)
SECRET_KEY = os.getenv("SECRET_KEY", "votre-super-cle-secrete-par-defaut")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./monuments.db")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# --- Initialisation des extensions et dépendances ---
app = FastAPI(
    title="Africa Heritage API",
    description="API pour cataloguer les sites et monuments du patrimoine africain.",
    version="0.1.0",
)

# Authentification JWT
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# --- Base de données ---
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Fonction de dépendance pour obtenir une session de base de données."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Modèles de données (SQLAlchemy) ---
class User(Base):
    """Modèle de la table 'users'."""
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="visitor")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    submissions = relationship("Item", back_populates="submitted_by_user")

class Item(Base):
    """Modèle de la table 'items' pour les fiches de patrimoine."""
    __tablename__ = "items"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    slug = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    title = Column(String)
    category = Column(String)
    country = Column(String)
    description = Column(Text)
    image_url = Column(String)
    official_url = Column(String)
    tags = Column(String) # Chaîne de caractères
    status = Column(Enum('pending', 'approved', 'rejected', name='item_status'), default='pending')
    is_deleted = Column(Integer, default=0) # 0 = false, 1 = true
    submitted_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    submitted_by_user = relationship("User", back_populates="submissions")

# --- Schémas de données (Pydantic) ---
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: str
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[str] = None
    role: Optional[str] = None

class ItemBase(BaseModel):
    name: str
    title: Optional[str] = None
    category: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[HttpUrl] = None
    official_url: Optional[HttpUrl] = None
    tags: Optional[List[str]] = None

    @validator("tags", pre=True)
    def tags_to_list(cls, v):
        if isinstance(v, str):
            return [tag.strip() for tag in v.split(',')]
        return v

class ItemCreate(ItemBase):
    pass

class ItemOut(ItemBase):
    id: str
    slug: str
    status: str
    is_deleted: int
    submitted_by: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

# --- Fonctions de sécurité ---
def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: SessionLocal = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise credentials_exception
        return user
    except JWTError:
        raise credentials_exception

# --- Routes d'authentification ---
@app.post("/auth/register", response_model=UserOut)
def register(user_data: UserCreate, db: SessionLocal = Depends(get_db)):
    """Enregistre un nouvel utilisateur."""
    db_user = db.query(User).filter(User.email == user_data.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email déjà enregistré")
    
    hashed_password = get_password_hash(user_data.password)
    new_user = User(email=user_data.email, password_hash=hashed_password, role="admin")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/auth/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_db)):
    """Authentifie un utilisateur et renvoie un token JWT."""
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id, "role": user.role}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# --- Routes publiques ---
@app.get("/items", response_model=List[ItemOut])
def get_approved_items(db: SessionLocal = Depends(get_db)):
    """Récupère la liste des fiches approuvées et non-supprimées."""
    items = db.query(Item).filter(Item.status == 'approved', Item.is_deleted == 0).all()
    return items

@app.get("/items/{item_slug}", response_model=ItemOut)
def get_item_by_slug(item_slug: str, db: SessionLocal = Depends(get_db)):
    """Récupère une fiche par son slug."""
    item = db.query(Item).filter(Item.slug == item_slug, Item.status == 'approved', Item.is_deleted == 0).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item non trouvé ou non approuvé")
    return item

# --- Routes pour les soumissions (contributeurs) ---
@app.post("/submissions", response_model=ItemOut, status_code=201)
def create_submission(item_data: ItemCreate, user: User = Depends(get_current_user), db: SessionLocal = Depends(get_db)):
    """Crée une nouvelle fiche de patrimoine (statut 'pending')."""
    if user.role not in ['contributor', 'admin']:
        raise HTTPException(status_code=403, detail="Vous n'avez pas la permission de soumettre.")

    item_data_dict = item_data.model_dump()
    if item_data_dict.get('tags'):
        item_data_dict['tags'] = ",".join(item_data_dict['tags'])

    new_slug = slugify(item_data.name)
    existing_item = db.query(Item).filter(Item.slug == new_slug).first()
    if existing_item:
        new_slug = f"{new_slug}-{uuid.uuid4().hex[:4]}"

    new_item = Item(
        **item_data_dict,
        slug=new_slug,
        submitted_by=user.id
    )
    
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/my-submissions", response_model=List[ItemOut])
def get_my_submissions(user: User = Depends(get_current_user), db: SessionLocal = Depends(get_db)):
    """Récupère la liste des soumissions de l'utilisateur connecté."""
    if user.role not in ['contributor', 'admin']:
        raise HTTPException(status_code=403, detail="Vous n'avez pas la permission d'accéder à cette ressource.")
    
    submissions = db.query(Item).filter(Item.submitted_by == user.id).all()
    return submissions

# --- Routes pour l'administration ---
@app.get("/admin/submissions", response_model=List[ItemOut])
def get_admin_submissions(
    status: Literal['pending', 'approved', 'rejected'] = Query('pending'),
    user: User = Depends(get_current_user),
    db: SessionLocal = Depends(get_db)
):
    """Récupère les soumissions en fonction de leur statut."""
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Accès admin requis.")
    
    submissions = db.query(Item).filter(Item.status == status).all()
    return submissions

@app.post("/admin/submissions/{item_id}/approve")
def approve_item(item_id: str, user: User = Depends(get_current_user), db: SessionLocal = Depends(get_db)):
    """Approuve une fiche."""
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Accès admin requis.")
    
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    
    item.status = 'approved'
    db.commit()
    return {"message": "Item approuvé."}

@app.post("/admin/submissions/{item_id}/reject")
def reject_item(item_id: str, user: User = Depends(get_current_user), db: SessionLocal = Depends(get_db)):
    """Rejette une fiche."""
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Accès admin requis.")
    
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    
    item.status = 'rejected'
    db.commit()
    return {"message": "Item rejeté."}

@app.patch("/admin/items/{item_id}", response_model=ItemOut)
def update_item(item_id: str, item_data: ItemCreate, user: User = Depends(get_current_user), db: SessionLocal = Depends(get_db)):
    """Met à jour une fiche existante."""
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Accès admin requis.")
    
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item non trouvé")

    for key, value in item_data.model_dump(exclude_unset=True).items():
        if key == "tags" and isinstance(value, list):
            setattr(item, key, ",".join(value))
        else:
            setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item

@app.delete("/admin/items/{item_id}")
def soft_delete_item(item_id: str, user: User = Depends(get_current_user), db: SessionLocal = Depends(get_db)):
    """Supprime logiquement (soft delete) une fiche."""
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Accès admin requis.")
    
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    
    item.is_deleted = 1
    db.commit()
    return {"message": "Item supprimé (soft delete)."}

@app.post("/admin/items/{item_id}/restore")
def restore_item(item_id: str, user: User = Depends(get_current_user), db: SessionLocal = Depends(get_db)):
    """Restaure une fiche précédemment supprimée."""
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Accès admin requis.")
    
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    
    item.is_deleted = 0
    db.commit()
    return {"message": "Item restauré."}

# --- Initialisation de la base de données ---
@app.on_event("startup")
def create_db_tables():
    """Crée les tables de la base de données si elles n'existent pas."""
    Base.metadata.create_all(bind=engine)

# --- Point d'entrée pour le développement ---
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
