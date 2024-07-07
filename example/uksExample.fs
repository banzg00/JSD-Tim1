project {
    name: uksTest
    java: 17
}

entity User {
    customUsername: str
    email: str
    password: str
    firstName: str
    lastName: str
    fullName: str
}

entity Role {
    name: str
}

entity Member {
    role: str
    inviteStatus: str
}


entity Review {
    status: str
}

entity Branch {
    name: str
    updatedAt: dateTime
    updatedBy: User @1..1
}

entity Milestone {
    state: str
    name: str
    dueDate: dateTime
    description: str
}

entity Project {
    name: str
}

entity Issue {
    createdAt: dateTime
}

entity PullRequest {
    reviews: Review @1..*
}

entity Commit {
    message: str
    committedAt: dateTime
}

entity IssueEvent {
    type: str
    newValue: str
    createdAt: dateTime
}

entity Comment {
    message: str
    author: User @1..1
    createdAt: dateTime
    code: str
}
entity Item {
    name: str
    description: str
    state: str
    createdAt: dateTime
}
entity Label {
    name: str
    color: str
    description: str
}

