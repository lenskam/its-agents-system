from __future__ import annotations

import pytest

from common.llm import DataSensitivity, classify_sensitivity


class TestClassifySensitivity:
    def test_public_text_returns_public(self) -> None:
        assert classify_sensitivity("Quel est le statut du monitoring?") == DataSensitivity.PUBLIC

    def test_email_detected_as_confidential(self) -> None:
        assert (
            classify_sensitivity("L'utilisateur jean.dupont@example.com a un problème")
            == DataSensitivity.CONFIDENTIAL
        )

    def test_password_keyword_detected_as_confidential(self) -> None:
        assert (
            classify_sensitivity("Le mot de passe de l'admin est...")
            == DataSensitivity.CONFIDENTIAL
        )

    def test_api_key_keyword_detected_as_confidential(self) -> None:
        assert (
            classify_sensitivity("Changing the api_key for production")
            == DataSensitivity.CONFIDENTIAL
        )

    def test_ip_address_detected_as_confidential(self) -> None:
        assert (
            classify_sensitivity("Le serveur 192.168.1.100 est en panne")
            == DataSensitivity.CONFIDENTIAL
        )

    def test_financial_amount_detected_as_confidential(self) -> None:
        assert (
            classify_sensitivity("Facture de FCFA 1,500,000 pour Client Alpha")
            == DataSensitivity.CONFIDENTIAL
        )

    def test_generic_question_returns_public(self) -> None:
        assert (
            classify_sensitivity("Comment créer un devis dans Odoo?") == DataSensitivity.PUBLIC
        )

    def test_credential_keyword_detected(self) -> None:
        assert (
            classify_sensitivity("Update the database credential")
            == DataSensitivity.CONFIDENTIAL
        )
