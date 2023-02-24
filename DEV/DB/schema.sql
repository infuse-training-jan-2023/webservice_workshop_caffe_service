CREATE TABLE "menu"(
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "price" INTEGER NOT NULL
);

CREATE TABLE "cart"(
    "cid" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "mid" TEXT NOT NULL,
    "order_quantity" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    FOREIGN KEY ("mid") REFERENCES "menu"("id")
);