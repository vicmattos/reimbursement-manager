import pytest

from reimbursement_manager.presentation.protocols.controller import Controller


def test_raises_exception_if_instantiated():
    with pytest.raises(TypeError):
        Controller()
