from database import engine, Base
import models

models.Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
