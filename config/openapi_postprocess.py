"""drf-spectacular postprocess hook: merge openapi_manual.yaml into auto-generated."""
import logging
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

MANUAL_PATH = Path(__file__).parent / 'openapi_manual.yaml'


def merge_manual(result, generator, request, public):
    """Merge manual paths/schemas into the auto-generated OpenAPI spec.

    Resolves P-S1-OpenAPI: permite a frontend mockear endpoints planificados
    para Ola 2 antes de que existan en código backend.

    Robust against missing, empty, or malformed openapi_manual.yaml: logs a
    warning and returns the auto-generated spec unmodified rather than
    breaking schema generation.
    """
    if not MANUAL_PATH.exists():
        return result

    try:
        manual = yaml.safe_load(MANUAL_PATH.read_text()) or {}
    except yaml.YAMLError as e:
        logger.warning("openapi_manual.yaml malformed, skipping overlay: %s", e)
        return result

    if not isinstance(manual, dict):
        logger.warning(
            "openapi_manual.yaml top-level must be a mapping, got %s; skipping overlay",
            type(manual).__name__,
        )
        return result

    if not manual:
        return result

    result.setdefault('paths', {})
    result['paths'].update(manual.get('paths', {}))
    result.setdefault('components', {}).setdefault('schemas', {})
    result['components']['schemas'].update(
        manual.get('components', {}).get('schemas', {})
    )
    return result
