from claim.reports import claim_elligibility, claim_percentage_referral, claims_overview, claim_history, \
    claims_primary_operational_indicators
from claim.reports.claim_history import claim_history_query
from claim.reports.claim_percentage_referral import claim_percentage_referral_query
from claim.reports.claim_elligibility import claim_elligibility_query
from claim.reports.claims_overview import claims_overview_query
from claim.reports.claims_primary_operational_indicators import claims_primary_operational_indicators_query

import logging

report_definitions = [
    {
        "name": "claim_elligibility",
        "engine": 0,
        "default_report": claim_elligibility.template,
        "description": "Claim elligibility status",
        "module": "claim",
        "python_query": claim_elligibility_query,
        "permission": ["131214"],
    },
    {
        "name": "claim_percentage_referral",
        "engine": 0,
        "default_report": claim_percentage_referral.template,
        "description": "Percentage of referrals in claims",
        "module": "claim",
        "python_query": claim_percentage_referral_query,
        "permission": ["131214"],
    },
    {
        "name": "claims_overview",
        "engine": 0,
        "default_report": claims_overview.template,
        "description": "Overview of the processing of claims",
        "module": "claim",
        "python_query": claims_overview_query,
        "permission": ["131213"],
    },
    {
        "name": "claim_history",
        "engine": 0,
        "default_report": claim_history.template,
        "description": "Claim history",
        "module": "claim",
        "python_query": claim_history_query,
        "permission": ["131223"],
    },
    {
        "name": "claims_primary_operational_indicators",
        "engine": 0,
        "default_report": claims_primary_operational_indicators.template,
        "description": "Claims Primary operational indicators",
        "module": "claim",
        "python_query": claims_primary_operational_indicators_query,
        "permission": ["131202"],
    },
]
