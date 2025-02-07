from typing import Final


class PickListConstants:
    @classmethod
    def is_in_list(cls, value: str) -> bool:
        """
        Check if the given value is present in the pick list.
        
        :param value: The value to check.
        :return: True if the value is present, False otherwise.
        """
        for var, val in cls.__dict__.items():
            if var != "list_name" and val == value:
                return True
        return False


class CatalogMaterialTypesList(PickListConstants):
    list_name: Final[str] = "Catalog Material Types"

    ANIMAL: Final[str] = "Animal"
    ANTIBODY: Final[str] = "Antibody"
    BEADS: Final[str] = "Beads"
    BUFFER: Final[str] = "Buffer"
    CELL_LINE: Final[str] = "Cell Line"
    CHEMICAL: Final[str] = "Chemical"
    CONTAINER: Final[str] = "Container"
    DETECTION_REAGENT: Final[str] = "Detection Reagent"
    DRUG_PRODUCT: Final[str] = "Drug Product"
    DRUG_SUBSTANCE: Final[str] = "Drug Substance"
    ELISA_KIT: Final[str] = "ELISA Kit"
    ENZYME: Final[str] = "Enzyme"
    EQUIPMENT_CONSUMABLE: Final[str] = "Equipment Consumable"
    EXCIPIENT: Final[str] = "Excipient"
    FORMULATION: Final[str] = "Formulation"
    KIT: Final[str] = "Kit"
    LADDER: Final[str] = "Ladder"
    MEDIA: Final[str] = "Media"
    PEPTIDE: Final[str] = "Peptide"
    PRIMER: Final[str] = "Primer"
    PROTEIN: Final[str] = "Protein"
    SOLVENT: Final[str] = "Solvent"
    STANDARD: Final[str] = "Standard"
    WORKING_SOLUTION: Final[str] = "Working Solution"
    PLASMID: Final[str] = "Plasmid"


class ConstructTypesList(PickListConstants):
    list_name: Final[str] = "Construct Types"

    DRUG_SUBSTANCE: Final[str] = "Drug Substance"
    DRUG_PRODUCT: Final[str] = "Drug Product"
