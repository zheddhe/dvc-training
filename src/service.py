import numpy as np
import bentoml
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import jwt
from datetime import datetime, timedelta

JWT_SECRET_KEY = "your_jwt_secret_key_here"
JWT_ALGORITHM = "HS256"

USERS = {"user123": "password123", "user456": "password456"}


class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path == "/v1/models/rf_classifier/predict":
            token = request.headers.get("Authorization")
            if not token:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Missing authentication token"},
                )
            try:
                token = token.split()[1]
                payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            except jwt.ExpiredSignatureError:
                return JSONResponse(status_code=401, content={"detail": "Token expired"})
            except jwt.InvalidTokenError:
                return JSONResponse(status_code=401, content={"detail": "Invalid token"})
            request.state.user = payload.get("sub")
        return await call_next(request)


class InputModel(BaseModel):
    place: int
    catu: int
    sexe: int
    secu1: float
    year_acc: int
    victim_age: int
    catv: int
    obsm: int
    motor: int
    catr: int
    circ: int
    surf: int
    situ: int
    vma: int
    jour: int
    mois: int
    lum: int
    dep: int
    com: int
    agg_: int
    int: int
    atm: int  # type: ignore
    col: int  # type: ignore
    lat: float
    long: float
    hour: int  # type: ignore
    nb_victim: int  # type: ignore
    nb_vehicules: int  # type: ignore


# =============================
# Load model (future-proof API)
# =============================
model_ref = bentoml.models.get("accidents_rf:latest")
sklearn_svc = bentoml.sklearn.load_model(model_ref)  # ← plus de Runner ni Runnable


@bentoml.service(name="rf_clf_service")
class RFService:
    def configure(self, svc: bentoml.Service):
        svc.add_asgi_middleware(JWTAuthMiddleware)  # type: ignore

    @bentoml.api(route="/login")  # Pas d’input/output en 1.4
    async def login(self, credentials: dict):
        username = credentials.get("username")
        password = credentials.get("password")

        if username in USERS and USERS[username] == password:
            token = create_jwt_token(username)
            return {"token": token}
        else:
            # Réponse HTTP explicite
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid credentials"},
            )

    @bentoml.api(  # type: ignore
        route="/v1/models/rf_classifier/predict",
    )
    async def classify(self, body: InputModel) -> dict:
        input_series = np.array([
            body.place, body.catu, body.sexe, body.secu1, body.year_acc,
            body.victim_age, body.catv, body.obsm, body.motor, body.catr,
            body.circ, body.surf, body.situ, body.vma, body.jour, body.mois,
            body.lum, body.dep, body.com, body.agg_, body.int, body.atm,
            body.col, body.lat, body.long, body.hour, body.nb_victim,
            body.nb_vehicules,
        ])
        prediction = sklearn_svc.predict(input_series.reshape(1, -1))  # type: ignore
        return {"prediction": prediction.tolist()}  # type: ignore


def create_jwt_token(user_id: str):
    expiration = datetime.utcnow() + timedelta(hours=1)
    payload = {"sub": user_id, "exp": expiration}
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
