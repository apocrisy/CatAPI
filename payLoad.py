import random
import string



def RandomEmail(nameLen, surnameLen):
  letters = string.ascii_lowercase
  EmailOne = (''.join(random.choice(letters) for i in range(nameLen)))
  EmailTwo = (''.join(random.choice(letters) for i in range(surnameLen)))
  EmailThree = '@gmail.com'

  return EmailOne + '.' + EmailTwo + EmailThree



def registerB2B():
    body = {
  "type": "company",
  "name": "Lorem Ipsum",
  "companyName": "API test",
  "countryId": 191,
  "email": RandomEmail(6, 5),
  "subscribedToNewsletter": False,
  "password": "JohnDoe1",
  "phone": "+38669618399",
  "signupTerms": True,
  "vatId": "SI11223344",
  "survey": [
    {
      "questionId": 1,
      "answers": [
        1,
        2
      ]
    },
    {
      "questionId": 2,
      "answers": [
        5
      ]
    }
  ]
}
    return body

def billingDetailsChange():
  body = {
      "companyName": "My almost good company",
      "countryId": "1",
      "street": "20-22 Wenlock Road",
      "zip": "N1 7GU",
      "city": "London"
  }

  return body

def billingDetailsRevert():
  body = {
    "companyName": "My awesome company",
    "countryId": "191",
    "street": "Cesta v Gorice 34B",
    "zip": "1000",
    "city": "Ljubljana"
  }

  return body


def registerShortPassB2B():
  body = {
    "type": "company",
    "name": "Lorem Ipsum",
    "companyName": "API test",
    "countryId": 191,
    "email": RandomEmail(5,5),
    "subscribedToNewsletter": False,
    "password": "John1",
    "phone": "+38669618399",
    "signupTerms": True,
    "vatId": "SI11223344",
    "survey": [
      {
        "questionId": 1,
        "answers": [
          1,
          2
        ]
      },
      {
        "questionId": 2,
        "answers": [
          5
        ]
      }
    ]
  }
  return body

def registerInvalidPassB2B():
  body = {
    "type": "company",
    "name": "Lorem Ipsum",
    "companyName": "API test",
    "countryId": 191,
    "email": RandomEmail(5,6),
    "subscribedToNewsletter": False,
    "password": "johnjohn123",
    "phone": "+38669618399",
    "signupTerms": True,
    "vatId": "SI11223344",
    "survey": [
      {
        "questionId": 1,
        "answers": [
          1,
          2
        ]
      },
      {
        "questionId": 2,
        "answers": [
          5
        ]
      }
    ]
  }
  return body