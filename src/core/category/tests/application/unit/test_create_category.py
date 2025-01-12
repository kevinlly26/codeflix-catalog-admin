from unittest.mock import MagicMock
from uuid import UUID

import pytest

from src.core.category.application.exceptions import InvalidCategotryData
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest

class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)
        request = CreateCategoryRequest(
            name="Filme",
            description="Categoria de filmes",
            is_active=True
        )

        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response.id, UUID)
        assert mock_repository.save.called is True

    def test_create_category_With_invalid_data(self):
        use_case = CreateCategory(repository=MagicMock(CategoryRepository))

        with pytest.raises(InvalidCategotryData, match="name cannot be empty") as exc_info:
            use_case.execute(CreateCategoryRequest(name=""))

        assert exc_info.type is InvalidCategotryData
        assert str(exc_info.value) == "name cannot be empty" 