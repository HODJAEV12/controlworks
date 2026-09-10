class Validator:
    @staticmethod
    def validate_phone(phone):
        return phone.startswith("+996")

    @staticmethod
    def validate_year(year):
        return year > 0

    @staticmethod
    def validate_pages(pages):
        return pages > 0