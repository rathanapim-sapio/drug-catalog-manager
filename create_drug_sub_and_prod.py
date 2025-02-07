# Define the API URL and credentials
from sapiopycommons.callbacks.callback_util import CallbackUtil
from sapiopycommons.recordmodel.record_handler import RecordHandler
from sapiopylib.rest.User import SapioUser
from sapiopylib.rest.utils.recordmodel.RecordModelManager import RecordModelInstanceManager, RecordModelManager

from models.data_type_models import DirectoryModel, ConsumableModel, ConstructModel
from models.pick_list_classes import CatalogMaterialTypesList, ConstructTypesList


class DrugCatalogManager:
    def __init__(self, user: SapioUser):
        self.user = user
        self.record_handler: RecordHandler = RecordHandler(user)
        self.inst_manager: RecordModelInstanceManager = self.record_handler.inst_man
        self.record_manager: RecordModelManager = self.record_handler.rec_man

    def create_drug_sub_and_prod(self, drug_substance_name: str, drug_product_name: str):
        # Get the parent Catalogs Directory
        catalog_directories = self.record_handler.query_models(DirectoryModel, DirectoryModel.DIRECTORYNAME__FIELD_NAME.field_name, ["Catalogs"])
        if len(catalog_directories) == 0:
            raise Exception("Unable to add Drug Substance and Product. Catalogs directory not found.")
        catalog_directory: DirectoryModel = catalog_directories[0]

        # Create Drug Substance part of Material Type Drug Substance Catalog
        drug_substance: ConsumableModel = self.inst_manager.add_new_record_of_type(ConsumableModel)
        drug_substance.set_ConsumableName_field(drug_substance_name)
        drug_substance.set_ConsumableType_field(CatalogMaterialTypesList.DRUG_SUBSTANCE)
        drug_substance.add_parent(catalog_directory)
        self.record_manager.store_and_commit()  # Commit and store the record in the database to generate a record ID

        # Create a Drug Product
        drug_product: ConsumableModel = self.inst_manager.add_new_record_of_type(ConsumableModel)
        drug_product.set_ConsumableName_field(drug_product_name)
        drug_product.set_ConsumableType_field(CatalogMaterialTypesList.DRUG_PRODUCT)
        drug_product.add_parent(catalog_directory)

        # Create Drug Construct and set the DS Content link to the created Drug Substance
        drug_construct: ConstructModel = self.inst_manager.add_new_record_of_type(ConstructModel)
        drug_construct.set_ConstructType_field(ConstructTypesList.DRUG_SUBSTANCE)
        drug_construct.set_side_link(ConstructModel.DSCONTENTS__FIELD_NAME.field_name, drug_substance)
        drug_construct.add_parent(drug_product)

        self.record_manager.store_and_commit()