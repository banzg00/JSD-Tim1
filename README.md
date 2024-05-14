# JSD-Tim1

## Fullstack (.fs)

<b>Fullstack</b> is a domain-specific language (DSL)  for generating SpringBoot and Angular projects with CRUD operations of given entity models and REST paths. 

The file extension for your model must be .fs.

## Generator

Code generator will produce following features, based on given input model.
Model must be written using described grammar rules.

### SpringBoot Features

- Standardized project layout
- Entity classes
- For each entity:
  - JPA Repository
  - Service + CRUD operations
  - Controller + CRUD operations
  - DTO
  - Mappers - from entity to DTO

### Angular Features
- Standardized project layout
- For each entity
  - Component
    - Page preview of an entity
    - Table preview of attributes
    - New & Update entity forms
    - Delete option
  - Service 
    - CRUD operations
  
  
## Grammar

### Options

- <b>Project configuration</b>
  - *name &emsp;&emsp;&emsp; (e.g. testProject) 
  - group&emsp;&emsp;&emsp;&emsp;(e.g. uns.ac.rs)
  - description &emsp; (e.g. "test project description")
  - java version&emsp;(e.g.  21)
  

- <b>Entities</b>
  - Entity name&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;(e.g. <i>entity Address {...}</i> )
    - format `'entity' entity-name`
  - Entity attributes &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;(e.g. <i> street : str</i> )
    - format `attribute-name : built-in-type` 
    - supported built-in types: 
      - bool 
      - str 
      - int 
      - float 
      - long
  - Attribute associations &emsp;&emsp;&emsp;&emsp;&emsp;(  <i> address: Address @1..1</i>  )
    - format `attribute-name : entity-type relationship-type` 
    - supported relationship types:
        - OneToOne: &emsp;&emsp;&emsp;&emsp; @1..1
        - OneToMany:&emsp;&emsp;&emsp;&emsp;@1..* 
        - ManyToOne:&emsp;&emsp;&emsp;&emsp;@*..1
        - ManyToMany: &emsp;&emsp;&emsp; @\*..\*


- <b>Custom DTOs & Mappings</b>
  - auto-generated DTOs will be in format [EntityName]DTO
  - if you need more custom DTOs you can define them and their custom mapping from wanted entity
    1. response DTO:
        - Define DTO name  (<i>e.g CustomPersonDTO</i>)
        - Define from which Entity is mapping done (<i>e.g. (Person) </i>)
        - Define attributes 
          - format `attribute-name : built-in-type = origin-entity-attribute-name`
          - format `attribute-name : other-DTO-type = origin-entity-relationship-name` 
          
    2. input DTO:
        - Define DTO name
        - Define attributes
          - format `attribute-name : built-in-type`
          - format `attribute-name : other-DTO-type` 


- <b>REST paths</b>
  - auto-generated paths for each CRUD operation of an entity
  - if you need more custom paths:
    - Define path (new or existing)  &emsp;&emsp;(<i>e.g. API /myApi</i>)
    - Define method name&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;(<i>e.g. GET /myGetPath</i>)
    - Define parameters
      - path parameter
        - format: `'pathParam' : built-in-type param-name`
      - body parameter
        - format: `'body' : built-in-type`
        - format: `'body' : other-DTO-type`
      - return value 
        - format: `'return' : built-in-type`
        - format: `'return' : other-DTO-type`

## Example

```
project {
    name: testProject
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
```


## Instructions

To generate SpringBoot application use following command:
```
textx generate [PATH TO .fs FILE] --target springboot -o [PATH TO OUTPUT FOLDER] --overwrite
```

To generate Angular application use following command:
```
textx generate [PATH TO .fs FILE] --target angular -o [PATH TO OUTPUT FOLDER] --overwrite
```

Main difference between previous two commands is `--target` parameter, which can take values
<i>springboot</i> or <i>angular</i> whether you're generating frontend or backend application.

Example usage:

<code>textx generate example/userExample.fs --target springboot -o example/example_output --overwrite</code>
<br>
<code>textx generate example/userExample.fs --target angular -o example/example_output --overwrite</code>



# Credits

Initial project layout generated with `textx startproject`.
