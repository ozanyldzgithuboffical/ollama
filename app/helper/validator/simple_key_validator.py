class SimpleKeyValidator:
    @staticmethod
    def key_validation(user_request):
        if not user_request["programmingLanguage"]:
            return False
        elif not user_request["userQuery"]:
            return False
        return True

    @staticmethod
    def key_validation_reviewer(user_request):
        if not user_request["pullRequestTitle"]:
            return False
        elif not user_request["userQuery"]:
            return False
        return True

    @staticmethod
    def key_validation_tester(user_request):
        if not user_request["userQuery"]:
            return False
        elif not user_request["instruction"]:
            return False
        return True
