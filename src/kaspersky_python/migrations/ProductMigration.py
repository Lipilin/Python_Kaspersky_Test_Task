from .Migration import Migration
from kaspersky_python.database.Database import Database
from kaspersky_python.database.tables.Product import Product
from sqlalchemy.orm import Session

class ProductMigration(Migration):

    def __init__(
        self, file_path: str, 
        product_mapping: dict[tuple[str, str], int | None]
    ) -> None:
        super().__init__(file_path)
        self.__product_mapping = product_mapping

    def save_data(self, batch: list) -> None:
        with Session(Database().engine) as session:
            products = []
            for data in batch:
                vendor = data.get('vendor')
                product_name = data.get('product')
                if (vendor, product_name) in self.__product_mapping:
                    continue
                product = Product(
                    vendor=vendor,
                    product_name=product_name,
                )
                products.append(product)    
                self.__product_mapping[(vendor, product_name)] = None
            session.add_all(products)
            session.commit()
            for product in products:
                self.__product_mapping[(product.vendor, product.product_name)] = product.id