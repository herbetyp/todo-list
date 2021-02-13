from todo.django_assertions import assert_equal


def test_str_category(category):
    assert_equal(str(category), category.name)


def test_str_todo(todo):
    assert_equal(str(todo), todo.name)
