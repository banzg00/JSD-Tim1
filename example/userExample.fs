project {
    name: testProject
    group: uns.ac.rs
    description: "test project description"
    java: 17
}

entity User {
    email: str
    password: str
    fullName: str
}

entity Person {
    name : str
    address: Address @1..1
    age: int
    houses: House @1..*
}

entity Address {
    street : str
    city : str
    country : str
}

entity House {
    floor: int
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

