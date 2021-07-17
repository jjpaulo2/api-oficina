-- upgrade --
CREATE TABLE IF NOT EXISTS "car" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "manufacturer" VARCHAR(20) NOT NULL,
    "model" VARCHAR(20) NOT NULL,
    "year" INT NOT NULL
);
CREATE TABLE IF NOT EXISTS "client" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "cpf" VARCHAR(11) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "service" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "description" TEXT NOT NULL,
    "price" DOUBLE PRECISION NOT NULL
);
CREATE TABLE IF NOT EXISTS "providedservice" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "start_date" DATE NOT NULL,
    "end_date" DATE NOT NULL,
    "price" DOUBLE PRECISION NOT NULL,
    "car_id" INT NOT NULL REFERENCES "car" ("id") ON DELETE CASCADE,
    "service_id" INT NOT NULL REFERENCES "service" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "permission" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "key" VARCHAR(20) NOT NULL,
    "name" VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(20) NOT NULL,
    "password" VARCHAR(100) NOT NULL,
    "name" VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "car_client" (
    "car_id" INT NOT NULL REFERENCES "car" ("id") ON DELETE CASCADE,
    "client_id" INT NOT NULL REFERENCES "client" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "user_permission" (
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "permission_id" INT NOT NULL REFERENCES "permission" ("id") ON DELETE CASCADE
);
