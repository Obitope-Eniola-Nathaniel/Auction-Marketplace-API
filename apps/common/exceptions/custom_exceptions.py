from rest_framework.exceptions import APIException


class BusinessRuleViolation(APIException):
    status_code = 400
    default_detail = "This action violates a business rule."
    default_code = "business_rule_violation"
