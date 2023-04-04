use actix_web::{get, http::StatusCode, web, App, Error, HttpResponse, HttpServer, Responder};
use serde::Serialize;

#[derive(Serialize)]
struct PredictionResult {
    cancel_prob: f32,
    divert_prob: f32,
    expct_delay: f32,
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(liveness).service(predict))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}

#[get("/")]
async fn liveness() -> impl Responder {
    HttpResponse::Ok().body("Alive!")
}

#[get("/")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello world!")
}

#[get("/predict")]
async fn predict() -> Result<impl Responder, Error> {
    let res = PredictionResult {
        cancel_prob: 0.0,
        divert_prob: 0.0,
        expct_delay: 0.0,
    };

    // call prediction here

    Ok(web::Json(res))
}
