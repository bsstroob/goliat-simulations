from unittest.mock import MagicMock, patch

import pytest

# Mock s4l_v1 and h5py
mocks = {
    "s4l_v1": MagicMock(),
    "s4l_v1.model": MagicMock(),
    "s4l_v1.document": MagicMock(),
    "h5py": MagicMock(),
}

with patch.dict("sys.modules", mocks):
    from src.project_manager import ProjectManager


@pytest.fixture
def mock_config():
    config = MagicMock()
    config.get_setting.return_value = "near_field"
    config.base_dir = "/tmp"
    return config


@pytest.mark.skip_on_ci
def test_project_manager_initialization(mock_config):
    pm = ProjectManager(mock_config, MagicMock(), MagicMock())
    assert pm.config == mock_config


# More tests would require a more complex setup with file system interactions
# and more detailed mocking of s4l_v1, which is out of scope.
