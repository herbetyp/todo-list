import pytest

from model_bakery import baker

from todo.core.models import Category, Todo


@pytest.fixture
def category(db):
    return baker.make(Category)


@pytest.fixture
def todo(db):
    return baker.make(Todo)
