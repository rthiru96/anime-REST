CREATE TABLE "anime" (
  "id" bigserial PRIMARY KEY,
  "anime" varchar NOT NULL,
  "released_date" varchar NOT NULL,
  "seasons" bigint NOT NULL,
  "created_at" timestamptz NOT NULL DEFAULT (now())
);
