CREATE TABLE "menu"(
    "menu_item_id" TEXT NOT NULL PRIMARY KEY,
    "menu_item_name" TEXT NOT NULL,
    "menu_item_description" TEXT NOT NULL,
    "menu_item_price" INTEGER NOT NULL
);

CREATE TABLE "cart"(
    "cart_id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "menu_item_id" TEXT NOT NULL,
    "order_quantity" TEXT NOT NULL,
    "customer_name" TEXT NOT NULL,
    FOREIGN KEY ("menu_item_id") REFERENCES "menu"("menu_item_id")
);