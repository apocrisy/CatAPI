Feature: Cat API query parameters

  Scenario: Verify TheCatAPI for product fit
    Given Looking for a cat over TheCatAPI in breeds endpoint
    When Get request is sent to TheCatAPI breeds
    Then Status code of response should be 200
    And List should contain cats that are hypoallergenic, dog friendly and do not shed.