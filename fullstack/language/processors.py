from textx import TextXSemanticError


# Object processor
# def input_dto_mapping_custom_type_processor(mapping):
#     return mapping


# Model processor == semantic check
def semantic_check(metamodel, model):
    entity_dtos = get_entity_dto_names(metamodel)

    for dto in metamodel.dtos:
        if get_class_name(dto) == 'CustomResponseDTO':
            for attribute_def in dto.mappings:
                check_attribute_type_entity_dto(attribute_def, dto, entity_dtos)

        if get_class_name(dto) == 'CustomInputDTO':
            for attribute_mappings in dto.mappings:
                if get_class_name(attribute_mappings.mapping) == 'EntityDTOMapping':
                    check_attribute_type_entity_dto(attribute_mappings.mapping, dto, entity_dtos)


def get_class_name(param):
    return param.__class__.__name__


def check_attribute_type_entity_dto(attribute, dto_def, all_entity_dtos):
    if not check_entity_dto_name(attribute.type, all_entity_dtos):
        raise TextXSemanticError("Invalid attribute type {} of {} inside {} definition"
                                 .format(attribute.type.name, attribute.name, dto_def.name))


def check_entity_dto_name(entity_dto, all_entity_dtos):
    return get_class_name(entity_dto) != 'EntityDTO' or entity_dto.name in all_entity_dtos


def get_all_dto_names(metamodel):
    entity_dtos = get_entity_dto_names(metamodel)
    all_dto_names = entity_dtos.copy()
    all_dto_names.extend(x.name for x in metamodel.dtos)
    return all_dto_names


def get_entity_dto_names(metamodel):
    entity_dtos = []
    for e in metamodel.entities:
        entity_dtos.append(e.name + 'DTO')
    return entity_dtos
