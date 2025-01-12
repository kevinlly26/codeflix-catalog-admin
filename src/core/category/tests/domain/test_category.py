import pytest
from src.core.category.domain.category import Category

class TestCategory:
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()


class TestUpdateCategory:
    def test_update_Category_with_name_and_description(self):
        category = Category(name="Filme", description="Filmes em geral")

        category.update_category(name="Serie", description="General series")

        assert category.name == "Serie"
        assert category.description == "General series"

    def test_update_category_with_invalid_name(self):
        categoy = Category(name="Filme", description="General Filmes")

        with pytest.raises(ValueError, match="name cannot be longer than 255"):
            categoy.update_category(name="a" * 256, description="General series")    

class TestActivate:
    def test_Activate_category(self):
        category = Category(
            name="Filme",
            description="General Filmes",
            is_active=False
        )            

        category.activate()

        assert category.is_active is True