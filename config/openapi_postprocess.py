"""drf-spectacular postprocess hook: merge openapi_manual.yaml into auto-generated."""
from pathlib import Path

import yaml

MANUAL_PATH = Path(__file__).parent / 'openapi_manual.yaml'


def merge_manual(result, generator, request, public):
    """Merge manual paths/schemas into the auto-generated OpenAPI spec.

    Resolves P-S1-OpenAPI: permite a frontend mockear endpoints planificados
    para Ola 2 antes de que existan en código backend.
    """
    if not MANUAL_PATH.exists():
        return result
    manual = yaml.safe_load(MANUAL_PATH.read_text())
    result.setdefault('paths', {})
    result['paths'].update(manual.get('paths', {}))
    result.setdefault('components', {}).setdefault('schemas', {})
    result['components']['schemas'].update(
        manual.get('components', {}).get('schemas', {})
    )
    return result
