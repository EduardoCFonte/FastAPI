from database import engine
import models

models.Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
