# main.py
import os

from dotenv import load_dotenv
from sapiopylib.rest.User import SapioUser

from create_drug_sub_and_prod import DrugCatalogManager

load_dotenv()
api_url = os.getenv('API_URL')
username = os.getenv('API_USERNAME')
password = os.getenv('API_PASSWORD')

if __name__ == "__main__":
    user = SapioUser(url=api_url, verify_ssl_cert=True, username=username, password=password)

    # Get Data, replace with your own data
    drug_substance_name: str = "Drug Substance XXX001"
    drug_product_name: str = "Drug Product XXX001"

    drug_catalog_manager = DrugCatalogManager(user=user)
    drug_catalog_manager.create_drug_sub_and_prod(drug_substance_name=drug_substance_name, drug_product_name=drug_product_name)