project {
    name: test
    group: "uns.ac.rs"
    description: "test project description"
    java: 21
}

entity Person {
    name : str
    address: Address @1..1
    age: int
}

entity Address {
    street : str
    city : str
    country : str
    owner: Person @1..1
}

// custom DTOs and mappers
DTO CustomPersonDTO(Person) {
    addressInfo: AddressDTO = address
    nameIfo: str = name
}

DTO PersonResponseDTO {
    nameInfo: str
    addressInfo: AddressDTO
    customInfo: CustomPersonDTO
}

// custom API requests
API /person {
    GET /getCustomPerson {
        pathParam: Long id
        return: PersonResponseDTO
        body: PersonDTO
    }
}


API /myApi {
    POST /myPostPath {
        body: str
        return: str
    }
    GET /myGetPath {
        return: bool
    }
}

