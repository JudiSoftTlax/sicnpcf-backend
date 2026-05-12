from unittest.mock import patch

import pytest
from rest_framework.test import APIClient

from config.openapi_postprocess import merge_manual


def test_merge_manual_missing_file_returns_result_unchanged(tmp_path):
    fake_path = tmp_path / 'does-not-exist.yaml'
    result = {'paths': {'/x': 'y'}}
    with patch('config.openapi_postprocess.MANUAL_PATH', fake_path):
        out = merge_manual(result, None, None, True)
    assert out == {'paths': {'/x': 'y'}}


def test_merge_manual_malformed_yaml_returns_result_unchanged(tmp_path, caplog):
    bad = tmp_path / 'bad.yaml'
    bad.write_text("paths: [unclosed\n")
    result = {'paths': {'/x': 'y'}}
    with patch('config.openapi_postprocess.MANUAL_PATH', bad):
        out = merge_manual(result, None, None, True)
    assert out == {'paths': {'/x': 'y'}}
    assert 'malformed' in caplog.text.lower()


def test_merge_manual_empty_yaml_returns_result_unchanged(tmp_path):
    empty = tmp_path / 'empty.yaml'
    empty.write_text('')
    result = {'paths': {'/x': 'y'}}
    with patch('config.openapi_postprocess.MANUAL_PATH', empty):
        out = merge_manual(result, None, None, True)
    assert out == {'paths': {'/x': 'y'}}


def test_merge_manual_non_dict_returns_result_unchanged(tmp_path, caplog):
    weird = tmp_path / 'weird.yaml'
    weird.write_text('- this\n- is\n- a list\n')
    result = {'paths': {'/x': 'y'}}
    with patch('config.openapi_postprocess.MANUAL_PATH', weird):
        out = merge_manual(result, None, None, True)
    assert out == {'paths': {'/x': 'y'}}
    assert 'mapping' in caplog.text.lower()


def test_schema_includes_manual_audit_endpoint():
    client = APIClient()
    resp = client.get('/api/v1/schema/')
    content = resp.content.decode()
    assert '/api/v1/audit/' in content
    assert '/api/v1/firma/sign' in content
    assert '/api/v1/documents/' in content


def test_schema_includes_auto_login_endpoint():
    client = APIClient()
    resp = client.get('/api/v1/schema/')
    content = resp.content.decode()
    assert '/api/v1/auth/login' in content
