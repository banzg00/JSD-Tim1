from textx import TextXSemanticError


# Object processor
# def input_dto_mapping_custom_type_processor(mapping):
#     return mapping


# Model processor == semantic check
def semantic_check(metamodel, model):
    entity_dtos = get_entity_dto_names(metamodel)
    entity_names = get_entity_names(metamodel)

    for dto in metamodel.dtos:
        if get_class_name(dto) == 'CustomResponseDTO':
            for attribute_def in dto.mappings:
                if get_class_name(attribute_def) == 'EntityDTOMapping':
                    check_attribute_type_entity_dto(attribute_def, dto, entity_dtos)

        if get_class_name(dto) == 'CustomInputDTO':
            for attribute_mappings in dto.mappings:
                if attribute_mappings.mapping:
                    if get_class_name(attribute_mappings.mapping) == 'EntityDTOMapping':
                        check_attribute_type_entity_dto(attribute_mappings.mapping, dto, entity_dtos)

    for api in metamodel.apis:
        # if api.apiPath in [entity_name.lower() for entity_name in entity_names]:
        #     print("Existing path: " + api.apiPath)
        for request in api.requests:
            # if request.pathParam:
            #     print("Path param: " + request.pathParam.name)
            full_path = api.apiPath + '/' + request.methodPath
            if request.bodyParam:
                if request.bodyParam.typeOfType == 'EntityDTO':
                    check_param_type_entity_dto(request.bodyParam, full_path, 'body parameter', entity_dtos)
            if request.returnValue:
                if request.returnValue.typeOfType == 'EntityDTO':
                    check_param_type_entity_dto(request.returnValue, full_path, 'return value', entity_dtos)


def get_class_name(param):
    return param.__class__.__name__


def check_param_type_entity_dto(param, path, definition, all_entity_dtos):
    if param.type.name not in all_entity_dtos:
        raise TextXSemanticError("Invalid type {} of {} inside {} definition".format(param.type, definition, path))


def check_attribute_type_entity_dto(attribute, dto_def, all_entity_dtos):
    if get_class_name(attribute.type) == 'EntityDTO' and attribute.type.name not in all_entity_dtos:
        raise TextXSemanticError("Invalid attribute type {} of {} inside {} definition"
                                 .format(attribute.type.name, attribute.name, dto_def.name))


def get_all_dto_names(metamodel):
    entity_dtos = get_entity_dto_names(metamodel)
    all_dto_names = entity_dtos.copy()
    all_dto_names.extend(x.name for x in metamodel.dtos)
    return all_dto_names


def get_entity_dto_names(metamodel):
    return [e.name + 'DTO' for e in metamodel.entities]


def get_entity_names(metamodel):
    return [e.name for e in metamodel.entities]