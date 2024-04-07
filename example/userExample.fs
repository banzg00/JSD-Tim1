project {
    name: testProject
    group: uns.ac.rs
    description: "test project description"
    java: 17
}

entity Person {
    name : str
    address: Address @1..1
    age: dateTime
    houses: House @1..*
}

entity Address {
    street : str
    city : str
    country : str
    owner: Person @1..1
}

entity House {
    floor: int
    homeOwner: Person @*..1
    createdAt: date
}

// custom DTOs and mappers
DTO CustomPersonDTO(Person) {
    addressInfo: AddressDTO[] = address
    nameInfo: str = name
}

DTO PersonResponseDTO {
    nameInfo: str[]
    addressInfo: AddressDTO
    customInfo: CustomPersonDTO
}

// custom API requests
API /person {
    GET /getCustomPerson {
        pathParam: long id
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

