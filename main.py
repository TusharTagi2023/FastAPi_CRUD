from fastapi import FastAPI,Depends,status,Response,HTTPException
from typing import Optional
from schemas import *
import models
import uvicorn
from database import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()


models.Base.metadata.create_all(engine)


# @app.get("/msg/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/msg/{id}")
# async def root(id:int):
#     return {"message": f"Hello World {id}"}

# @app.get("/msg/{id}/name/")
# async def root(id:int,name:Optional[str]=None):
#     return {"Id":id,"name":name}

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/details/")
def details_input(request:demo,db: Session = Depends(get_db)):
    new_demo = models.Demo(text=request.text,description=request.description)
    db.add(new_demo)
    db.commit()
    db.refresh(new_demo)
    return {"message":"your data is saved"}

@app.get("/demodata/")
def GetDemoData(db: Session = Depends(get_db),status_code=status.HTTP_201_CREATED):
    demos = db.query(models.Demo).all()
    print(demos)
    return {"Here is your all demo entries":demos}

@app.get("/demodata/{id}")
def GetDemoDatabyId(id,db: Session = Depends(get_db)):
    demo = db.query(models.Demo).filter(models.Demo.id==id).first()
    if demo:
        return demo
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deleteById(id,db: Session = Depends(get_db)):
    db.query(models.Demo).filter(models.Demo.id==id).delete(synchronize_session=False)
    db.commit()
    return{"succes":f"Id no {id} is deleted into the table"}



@app.put("/update/{id}",status_code=status.HTTP_200_OK)
async def upgrade(id,request:demo,db: Session = Depends(get_db)):
    demo_instance=db.query(models.Demo).filter(models.Demo.id == id)
    if demo_instance:
        demo_instance.update(request.model_dump())
        db.commit()
        return {"msg":"Entry is deleted"}
    raise HTTPException(status_code=404, detail="Id no {id} is not present in db")










if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)