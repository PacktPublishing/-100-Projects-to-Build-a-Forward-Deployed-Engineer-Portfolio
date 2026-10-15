# FDE 100-Project Code Lab

One safe, runnable Python starter per project. Each project is intentionally small enough to teach, test, and replace adapter by adapter.

## How to use this repository

1. Open a numbered project folder and read its architecture and implementation steps.
2. Run `python3 src/main.py`, then run the smoke test.
3. Replace the in-memory boundary with the suggested production stack.
4. Add credentials only through environment variables or a secrets manager.
5. Keep the contract, idempotency, authorization, telemetry, and audit patterns from the starter.

## Data Pipelines & ETL

- [001 — Ingest messy public CSVs into a clean Parquet lake with schema validation](./001-ingest-messy-public-csvs-into-a-clean-parquet-lake-with-sc/README.md)
- [002 — Build a scheduled Airflow/Dagster pipeline that dedupes and enriches CRM leads](./002-build-a-scheduled-airflow-dagster-pipeline-that-dedupes-an/README.md)
- [003 — Create a CDC pipeline from PostgreSQL to BigQuery with late-arrival handling](./003-create-a-cdc-pipeline-from-postgresql-to-bigquery-with-lat/README.md)
- [004 — Streaming ingest from Kafka to Delta Lake with watermarking and compaction](./004-streaming-ingest-from-kafka-to-delta-lake-with-watermarkin/README.md)
- [005 — Log ingestion pipeline from Fluent Bit to S3 to Athena with partition pruning](./005-log-ingestion-pipeline-from-fluent-bit-to-s3-to-athena-wit/README.md)
- [006 — Build a data quality framework with Great Expectations and auto-fail alerts](./006-build-a-data-quality-framework-with-great-expectations-and/README.md)
- [007 — Real-time anomaly detection on IoT sensor streams with Flink or Spark](./007-real-time-anomaly-detection-on-iot-sensor-streams-with-fli/README.md)
- [008 — ELT pipeline that reconciles Stripe and Shopify revenue nightly](./008-elt-pipeline-that-reconciles-stripe-and-shopify-revenue-ni/README.md)
- [009 — Build a feature store with point-in-time correctness](./009-build-a-feature-store-with-point-in-time-correctness/README.md)
- [010 — Data contract enforcement service using JSON Schema and Pydantic](./010-data-contract-enforcement-service-using-json-schema-and-py/README.md)

## APIs & Integrations

- [011 — REST API gateway that normalizes HubSpot, Salesforce, and Notion](./011-rest-api-gateway-that-normalizes-hubspot-salesforce-and-no/README.md)
- [012 — GraphQL facade over heterogeneous internal microservices](./012-graphql-facade-over-heterogeneous-internal-microservices/README.md)
- [013 — Webhook relay service with retry, dead-letter queues, and idempotency keys](./013-webhook-relay-service-with-retry-dead-letter-queues-and-id/README.md)
- [014 — OAuth2 proxy that unifies Google, Microsoft, and GitHub SSO](./014-oauth2-proxy-that-unifies-google-microsoft-and-github-sso/README.md)
- [015 — Rate-limiting and quota enforcement middleware for internal APIs](./015-rate-limiting-and-quota-enforcement-middleware-for-interna/README.md)
- [016 — API versioning with backward-compatible deprecation notices](./016-api-versioning-with-backward-compatible-deprecation-notice/README.md)
- [017 — Build a Procore or Veeva connector into your data warehouse](./017-build-a-procore-or-veeva-connector-into-your-data-warehous/README.md)
- [018 — Bi-directional sync between Airtable and Postgres with conflict resolution](./018-bi-directional-sync-between-airtable-and-postgres-with-con/README.md)
- [019 — Event-driven integration using NATS JetStream for internal services](./019-event-driven-integration-using-nats-jetstream-for-internal/README.md)
- [020 — Build and document a public API with an OpenAPI specification](./020-build-and-document-a-public-api-with-an-openapi-specificat/README.md)

## MCP Servers & Tooling

- [021 — MCP server connecting Slack, Gmail, and Calendar for an executive assistant](./021-mcp-server-connecting-slack-gmail-and-calendar-for-an-exec/README.md)
- [022 — MCP server exposing internal Jira and Confluence APIs to LLM tools](./022-mcp-server-exposing-internal-jira-and-confluence-apis-to-l/README.md)
- [023 — MCP server for Qdrant or Weaviate with typed tool schemas](./023-mcp-server-for-qdrant-or-weaviate-with-typed-tool-schemas/README.md)
- [024 — MCP server wrapping an internal pricing engine with audit logs](./024-mcp-server-wrapping-an-internal-pricing-engine-with-audit-/README.md)
- [025 — MCP server for Looker or Metabase natural-language queries](./025-mcp-server-for-looker-or-metabase-natural-language-queries/README.md)
- [026 — MCP server for SharePoint or Box with access control](./026-mcp-server-for-sharepoint-or-box-with-access-control/README.md)
- [027 — MCP server for Zendesk with auto-triage tools](./027-mcp-server-for-zendesk-with-auto-triage-tools/README.md)
- [028 — MCP server for 1Password or Vault with least-privilege scopes](./028-mcp-server-for-1password-or-vault-with-least-privilege-sco/README.md)
- [029 — MCP server for LaunchDarkly with rollout tools](./029-mcp-server-for-launchdarkly-with-rollout-tools/README.md)
- [030 — MCP server for Datadog or Prometheus with incident tools](./030-mcp-server-for-datadog-or-prometheus-with-incident-tools/README.md)

## RAG & LLM Systems

- [031 — Basic RAG over internal docs with chunking, embeddings, and retrieval metrics](./031-basic-rag-over-internal-docs-with-chunking-embeddings-and-/README.md)
- [032 — Multi-tenant RAG with per-tenant isolation and access control](./032-multi-tenant-rag-with-per-tenant-isolation-and-access-cont/README.md)
- [033 — RAG with hybrid BM25 and vector search plus query rewriting](./033-rag-with-hybrid-bm25-and-vector-search-plus-query-rewritin/README.md)
- [034 — Agentic RAG with search, SQL, API tools, and plan-and-execute](./034-agentic-rag-with-search-sql-api-tools-and-plan-and-execute/README.md)
- [035 — RAG with citations and grounded answers using snippet attribution](./035-rag-with-citations-and-grounded-answers-using-snippet-attr/README.md)
- [036 — Fine-tune a small LLM for domain-specific SOX controls Q&A](./036-fine-tune-a-small-llm-for-domain-specific-sox-controls-q-a/README.md)
- [037 — Build a RAG evaluation harness for recall, precision, faithfulness, and latency](./037-build-a-rag-evaluation-harness-for-recall-precision-faithf/README.md)
- [038 — Retrieval pipeline with ColBERT or cross-encoder re-ranking](./038-retrieval-pipeline-with-colbert-or-cross-encoder-re-rankin/README.md)
- [039 — LLM-powered data documentation generator from schemas and queries](./039-llm-powered-data-documentation-generator-from-schemas-and-/README.md)
- [040 — LLM agent that drafts SQL with schema grounding](./040-llm-agent-that-drafts-sql-with-schema-grounding/README.md)

## Evaluation & Observability

- [041 — End-to-end RAG evaluation framework with golden datasets](./041-end-to-end-rag-evaluation-framework-with-golden-datasets/README.md)
- [042 — LLM response quality scorer using rule-based and model-based metrics](./042-llm-response-quality-scorer-using-rule-based-and-model-bas/README.md)
- [043 — Drift detection for embeddings and retrieval Recall@K over time](./043-drift-detection-for-embeddings-and-retrieval-recall-k-over/README.md)
- [044 — Latency SLO dashboards for LLM endpoints with trace IDs](./044-latency-slo-dashboards-for-llm-endpoints-with-trace-ids/README.md)
- [045 — Cost attribution dashboard for LLM calls by user, team, and endpoint](./045-cost-attribution-dashboard-for-llm-calls-by-user-team-and-/README.md)
- [046 — Canary evaluation suite for prompt changes with an A/B harness](./046-canary-evaluation-suite-for-prompt-changes-with-an-a-b-har/README.md)
- [047 — Hallucination detector using claim extraction and source verification](./047-hallucination-detector-using-claim-extraction-and-source-v/README.md)
- [048 — Red-teaming harness for jailbreaks and prompt injection](./048-red-teaming-harness-for-jailbreaks-and-prompt-injection/README.md)
- [049 — Offline and online metric correlation for LLM system changes](./049-offline-and-online-metric-correlation-for-llm-system-chang/README.md)
- [050 — Feedback-loop UI for users to flag bad answers and retrain](./050-feedback-loop-ui-for-users-to-flag-bad-answers-and-retrain/README.md)

## Enterprise Integrations

- [051 — Sync Okta identities into internal RBAC with audit logs](./051-sync-okta-identities-into-internal-rbac-with-audit-logs/README.md)
- [052 — Integrate Snowflake with Atlan or DataHub and access policies](./052-integrate-snowflake-with-atlan-or-datahub-and-access-polic/README.md)
- [053 — Build a SOX-compliant change-management workflow for data pipelines](./053-build-a-sox-compliant-change-management-workflow-for-data-/README.md)
- [054 — Integrate ServiceNow incidents with Slack alerts and auto-runbooks](./054-integrate-servicenow-incidents-with-slack-alerts-and-auto-/README.md)
- [055 — Build a PII detection and masking layer for data exports](./055-build-a-pii-detection-and-masking-layer-for-data-exports/README.md)
- [056 — Centralize DLP policies across Google Drive, S3, and Postgres](./056-centralize-dlp-policies-across-google-drive-s3-and-postgre/README.md)
- [057 — Build a GDPR and CCPA data-access request portal with approvals](./057-build-a-gdpr-and-ccpa-data-access-request-portal-with-appr/README.md)
- [058 — Integrate secrets rotation into CI/CD pipelines](./058-integrate-secrets-rotation-into-ci-cd-pipelines/README.md)
- [059 — Build an immutable audit trail for LLM prompts and outputs](./059-build-an-immutable-audit-trail-for-llm-prompts-and-outputs/README.md)
- [060 — Integrate MLflow model registry with deployment gates and sign-offs](./060-integrate-mlflow-model-registry-with-deployment-gates-and-/README.md)

## CLI & Developer Tools

- [061 — CLI that scaffolds a microservice with linting, tests, and CI](./061-cli-that-scaffolds-a-microservice-with-linting-tests-and-c/README.md)
- [062 — CLI for data-contract validation against live datasets](./062-cli-for-data-contract-validation-against-live-datasets/README.md)
- [063 — CLI to generate database migrations from ORM models with safety checks](./063-cli-to-generate-database-migrations-from-orm-models-with-s/README.md)
- [064 — CLI to run local LLM evaluation suites with diff reports](./064-cli-to-run-local-llm-evaluation-suites-with-diff-reports/README.md)
- [065 — CLI to snapshot and restore MCP server configs per environment](./065-cli-to-snapshot-and-restore-mcp-server-configs-per-environ/README.md)
- [066 — CLI to profile slow SQL and suggest indexes](./066-cli-to-profile-slow-sql-and-suggest-indexes/README.md)
- [067 — CLI to manage feature flags across environments with rollout plans](./067-cli-to-manage-feature-flags-across-environments-with-rollo/README.md)
- [068 — CLI to scrape and version API docs into a searchable knowledge base](./068-cli-to-scrape-and-version-api-docs-into-a-searchable-knowl/README.md)
- [069 — CLI to generate OpenAPI specs from captured service traffic](./069-cli-to-generate-openapi-specs-from-captured-service-traffi/README.md)
- [070 — CLI to rotate credentials across services using Vault APIs](./070-cli-to-rotate-credentials-across-services-using-vault-apis/README.md)

## Real-time & Streaming

- [071 — Real-time order-funnel dashboard with WebSocket updates](./071-real-time-order-funnel-dashboard-with-websocket-updates/README.md)
- [072 — Streaming ETL enriching clickstream with user profiles in under one second](./072-streaming-etl-enriching-clickstream-with-user-profiles-in-/README.md)
- [073 — Real-time fraud-scoring microservice with model inference](./073-real-time-fraud-scoring-microservice-with-model-inference/README.md)
- [074 — Live chat analytics with topic clustering and sentiment over time](./074-live-chat-analytics-with-topic-clustering-and-sentiment-ov/README.md)
- [075 — Real-time log anomaly detector with automatic incident tickets](./075-real-time-log-anomaly-detector-with-automatic-incident-tic/README.md)
- [076 — Streaming joins between IoT telemetry and reference data](./076-streaming-joins-between-iot-telemetry-and-reference-data/README.md)
- [077 — Real-time personalization engine updating recommendations per session](./077-real-time-personalization-engine-updating-recommendations-/README.md)
- [078 — Live leaderboards with Redis sorted-set rank updates](./078-live-leaderboards-with-redis-sorted-set-rank-updates/README.md)
- [079 — Real-time capacity forecasting for API endpoints](./079-real-time-capacity-forecasting-for-api-endpoints/README.md)
- [080 — Real-time data-quality monitors with schema-drift alerts](./080-real-time-data-quality-monitors-with-schema-drift-alerts/README.md)

## Security & Governance

- [081 — Build a policy-as-code engine with OPA and Rego for data access](./081-build-a-policy-as-code-engine-with-opa-and-rego-for-data-a/README.md)
- [082 — Implement attribute-based access control for internal APIs](./082-implement-attribute-based-access-control-for-internal-apis/README.md)
- [083 — Build a data-lineage tracker from ingestion to ML features](./083-build-a-data-lineage-tracker-from-ingestion-to-ml-features/README.md)
- [084 — Create a secrets-scanning pre-commit hook with vault rotation](./084-create-a-secrets-scanning-pre-commit-hook-with-vault-rotat/README.md)
- [085 — Build a PII inventory service scanning databases and buckets](./085-build-a-pii-inventory-service-scanning-databases-and-bucke/README.md)
- [086 — Implement encryption at rest with KMS-backed key rotation](./086-implement-encryption-at-rest-with-kms-backed-key-rotation/README.md)
- [087 — Build a threat-model generator from architecture diagrams](./087-build-a-threat-model-generator-from-architecture-diagrams/README.md)
- [088 — Create a compliant data-retention and deletion scheduler](./088-create-a-compliant-data-retention-and-deletion-scheduler/README.md)
- [089 — Build an audit-log viewer with immutable storage and tamper evidence](./089-build-an-audit-log-viewer-with-immutable-storage-and-tampe/README.md)
- [090 — Implement fine-grained LLM output filtering for sensitive topics](./090-implement-fine-grained-llm-output-filtering-for-sensitive-/README.md)

## End-to-End Apps & Demos

- [091 — Internal support bot that triages tickets with an LLM and tools](./091-internal-support-bot-that-triages-tickets-with-an-llm-and-/README.md)
- [092 — Sales copilot that enriches leads from three APIs and drafts outreach](./092-sales-copilot-that-enriches-leads-from-three-apis-and-draf/README.md)
- [093 — Finance copilot that reconciles invoices and flags anomalies](./093-finance-copilot-that-reconciles-invoices-and-flags-anomali/README.md)
- [094 — HR onboarding bot that provisions accounts and tracks a checklist](./094-hr-onboarding-bot-that-provisions-accounts-and-tracks-a-ch/README.md)
- [095 — Ops runbook executor that responds to alerts with approved actions](./095-ops-runbook-executor-that-responds-to-alerts-with-approved/README.md)
- [096 — Compliance copilot that maps controls to evidence and gaps](./096-compliance-copilot-that-maps-controls-to-evidence-and-gaps/README.md)
- [097 — Data-catalog explorer with natural-language search and lineage](./097-data-catalog-explorer-with-natural-language-search-and-lin/README.md)
- [098 — Incident-response assistant aggregating logs, metrics, and traces](./098-incident-response-assistant-aggregating-logs-metrics-and-t/README.md)
- [099 — Customer-health scoring app with churn explanations](./099-customer-health-scoring-app-with-churn-explanations/README.md)
- [100 — Executive dashboard answering KPI questions with citations](./100-executive-dashboard-answering-kpi-questions-with-citations/README.md)
