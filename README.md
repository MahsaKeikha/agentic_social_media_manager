# F124 | Agentic Social Media Manager | L3 Gold Standard | v1.0

A governed five-agent reference architecture for social media strategy, content planning, community support, measurement, evidence discipline, risk review, and qualified human publication approval.

F124 is decision-support only. It can research, plan, draft, analyze, organize, and recommend social-media activity, but it cannot autonomously publish posts or replies, send direct messages, launch campaigns, delete public content, impersonate people, manufacture engagement, or perform external distribution.

## Social media lifecycle

```text
Context and Objectives
        -> Strategy and Audience
        -> Content Planning and Drafting
        -> Community and Risk Review
        -> Measurement and Learning
        -> Claims, Rights, Privacy, and Reputation Review
        -> Qualified Human Social Approval
        -> Human-Controlled Publication
```

The workflow fails closed when required reviews are missing or when material identity, harassment, deceptive-engagement, privacy, rights, claims, legal, reputational, or provenance risks remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Strategy Agent | Defines objectives, audiences, channels, positioning, cadence, and campaign logic | Why are we communicating, to whom, and on which channel? |
| Content Agent | Develops content concepts, formats, briefs, drafts, calendars, and adaptations | What should be communicated and how should it fit the platform? |
| Community Agent | Reviews interaction patterns, moderation needs, escalation risks, and community context | How should participation and community risk be handled? |
| Measurement Agent | Structures metrics, experiments, attribution limits, and learning loops | What evidence shows whether the strategy is working? |
| Review Agent | Reviews claims, rights, privacy, identity, safety, legal, reputation, and approval state | Is the package appropriate for qualified human review? |

Agents support social-media judgment. They do not replace authorized account owners, communications professionals, community managers, legal counsel, privacy specialists, brand leaders, safety teams, or platform policy enforcement.

## Repository structure

```text
AGENTS/
├── strategy_agent.py
├── content_agent.py
├── community_agent.py
├── measurement_agent.py
└── review_agent.py

SKILLS/
├── strategy_reasoning.py
├── content_reasoning.py
├── community_reasoning.py
├── measurement_reasoning.py
└── review_reasoning.py

TOOLS/
├── content_calendar.py
├── community_log.py
├── metric_registry.py
├── risk_register.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The architecture separates generative reasoning from deterministic planning records, community logs, metric registries, risk registers, governance, observability, and evaluation.

## Strategy and objectives

The policy requires `strategy_reviewed`.

Social strategy should begin with an explicit objective such as awareness, education, community participation, thought leadership, customer support, event communication, recruiting, product communication, or another legitimate goal.

F124 should not optimize engagement without regard to the actual communication objective, audience welfare, brand integrity, or downstream consequences.

## Audience architecture

Audience analysis can include needs, context, platform behavior, knowledge level, geography, language, professional role, customer stage, and accessibility needs.

Audience assumptions should remain distinguishable from verified audience evidence. Sensitive traits should not be inferred or exploited without a legitimate basis.

## Platform strategy

Different platforms have different norms, formats, recommendation systems, audience expectations, moderation rules, and disclosure requirements.

F124 can adapt a strategy across channels while preserving the underlying message and avoiding mechanical cross-posting when context materially differs.

## Content pillars

Content planning can organize recurring themes such as education, research, product knowledge, community stories, events, culture, customer questions, leadership perspectives, or industry analysis.

Content pillars are planning devices, not permission to repeat unsupported claims or flood channels with low-value material.

## Content calendar

`TOOLS/content_calendar.py` provides a deterministic planning surface.

A governed calendar can preserve:

```text
content_id
channel
objective
audience
pillar
format
draft_owner
review_owner
planned_date
claim_state
rights_state
approval_state
publication_state
```

Scheduling does not create autonomous publishing authority.

## Content formats

F124 can support planning for text posts, threads, carousels, images, short video, long video, live sessions, polls, stories, community questions, links, event posts, and other platform-supported formats.

Format recommendations should consider accessibility, message complexity, platform context, production cost, and audience value rather than engagement alone.

## Brand voice

Content should preserve reviewed brand voice, terminology, values, and identity while allowing channel-appropriate variation.

The system should flag material voice drift rather than inventing a new public persona without authorization.

## Authenticity and identity

The system must not impersonate individuals, employees, customers, experts, journalists, public officials, creators, or organizations.

`impersonation_risk` blocks release.

Drafting in an authorized person's established voice can be supported only as drafting assistance with human control over attribution and publication.

## AI-generated content

AI assistance should not be used to create false evidence, fabricated experiences, fake endorsements, nonexistent events, synthetic customer stories represented as real, or deceptive representations of human participation.

Where disclosure is required by platform policy, law, contract, or organizational policy, that requirement should be surfaced for review.

## Claims and evidence

The policy requires `claims_reviewed` and `evidence_provenance_reviewed`.

Claims about products, performance, science, customers, competitors, safety, health, finance, sustainability, employment, awards, partnerships, or other verifiable matters should be supported by reviewed evidence.

`unsupported_claim` and `evidence_provenance_gap` block release.

F124 must never fabricate citations, metrics, testimonials, customer outcomes, endorsements, partnerships, research findings, press coverage, awards, or platform analytics.

## Comparative claims

Comparisons with competitors or alternatives require a defined basis, current evidence, fair framing, and appropriate legal or brand review.

Selective comparisons should not be framed as universal superiority.

## Testimonials and endorsements

Testimonials should reflect authentic experiences and appropriate permissions. Material relationships, sponsorships, incentives, or other required disclosures should remain visible.

The system should not invent testimonials or convert an ordinary comment into an endorsement without authorization.

## Copyright and media rights

The workflow should track rights for images, video, music, graphics, text excerpts, logos, screenshots, user-generated content, and other media.

`copyright_rights_gap` blocks release when material rights or licensing questions remain unresolved.

Public availability does not imply unrestricted reuse rights.

## User-generated content

Reposting or featuring user-generated content can require permission, attribution, contextual review, and privacy consideration.

F124 should preserve the original context and avoid transforming a person's content into an implied endorsement without consent.

## Privacy and consent

The policy requires `privacy_consent_reviewed`.

Social content can expose names, faces, locations, health information, contact details, private conversations, employee information, customer information, children, or other personal data.

`privacy_consent_gap` blocks release.

The system should minimize unnecessary personal information and escalate sensitive cases for qualified review.

## Children and vulnerable audiences

Content involving minors or vulnerable people requires heightened consent, privacy, safeguarding, targeting, and reputational review.

Engagement goals should never override safeguarding requirements.

## Community management

`SKILLS/community_reasoning.py` and `TOOLS/community_log.py` support structured community review.

Community activity can be categorized by question, feedback, praise, complaint, misinformation, support need, abuse, threat, crisis signal, legal issue, or escalation need.

The system can recommend response approaches but does not autonomously publish replies.

## Reply governance

`publish_reply` is a protected action.

A reply can carry the same legal, reputational, privacy, and factual risk as an original post. High-speed interaction should not bypass review when the subject is sensitive.

## Direct messages

`send_direct_message` is protected.

F124 can draft proposed direct messages but cannot autonomously initiate private outreach, solicit sensitive information, or represent that a human has personally contacted someone.

## Harassment and abuse

`harassment_risk` blocks release.

The system should not generate targeted abuse, humiliation, threats, dogpiling instructions, or retaliatory engagement. Community safety should take precedence over maximizing interaction.

## Moderation

Moderation support can distinguish disagreement from abuse, spam, threats, impersonation, privacy violations, and platform-policy violations.

F124 should preserve escalation paths and avoid silently deleting legitimate criticism merely because it is negative.

## Deceptive engagement

`deceptive_engagement` blocks release.

Prohibited patterns include fabricated comments, fake likes, fake followers, coordinated inauthentic engagement, undisclosed bot personas, engagement rings designed to mislead, manufactured testimonials, and false claims of virality.

F124 should optimize for authentic audience value rather than manipulated metrics.

## Platform manipulation

The system should not recommend spam, mass unsolicited outreach, evasion of platform enforcement, account farms, fake identities, artificial amplification, or other deceptive platform manipulation.

Platform-specific growth tactics should remain within applicable rules and legitimate audience practices.

## Social listening

Social listening can identify themes, questions, sentiment signals, emerging topics, complaints, and community needs.

The system should distinguish sampled public conversation from representative population evidence and avoid overgeneralizing from viral or highly visible posts.

## Sentiment analysis

Automated sentiment is uncertain, especially with irony, slang, multilingual content, cultural context, and mixed emotions.

Sentiment scores should not be treated as definitive statements about individual people or entire communities.

## Trend analysis

Trends can change quickly and can be driven by news, algorithms, coordinated behavior, cultural moments, or platform-specific dynamics.

F124 can identify a trend opportunity while requiring contextual and reputational review before participation.

## Newsjacking and real-time content

Rapid participation in breaking events can create factual, safety, legal, and reputational risk.

The system should prioritize verification and appropriateness over speed when facts are incomplete or people may be harmed.

## Crisis communication

Potential crises require escalation rather than ordinary engagement optimization.

Examples include safety incidents, data breaches, litigation, executive misconduct allegations, product recalls, public emergencies, misinformation waves, threats, or rapidly escalating reputational events.

F124 can organize facts and draft options, but authorized crisis leaders retain publication authority.

## Misinformation

The system should not amplify an unverified claim merely because it is trending.

Corrective content should preserve source quality, uncertainty, timing, and context. High-impact factual disputes should be escalated to appropriate experts.

## Political and civic content

Political, election, public-policy, and civic content can require specialized legal, platform, organizational, and factual review.

F124 should not infer political beliefs from unrelated user behavior or use manipulative targeting strategies based on sensitive traits.

## Regulated domains

Health, financial, legal, employment, housing, education, public safety, and other regulated or high-impact content can require specialized claims and compliance review.

Social brevity does not remove the obligation to preserve important qualifications.

## Accessibility

Social content should consider alt text, captions, transcripts, readable contrast, clear language, keyboard-accessible destinations, descriptive links, and avoidance of unnecessary visual or sensory barriers.

Accessibility should be incorporated during content planning rather than added only after publication.

## Localization

Localization should preserve meaning, cultural context, claims, required disclosures, and brand identity rather than performing literal translation only.

Sensitive humor, idioms, symbols, dates, units, and cultural references should be reviewed locally when material.

## Hashtags and metadata

Hashtags, mentions, tags, geotags, keywords, and metadata can improve discovery but can also create misleading affiliation, privacy, spam, or context problems.

F124 should not tag people or organizations in ways that falsely imply endorsement or partnership.

## Influencer and creator relationships

Creator partnerships should preserve authorization, sponsorship disclosure, usage rights, deliverables, claim boundaries, and brand-safety requirements.

The system should not represent an unpaid or nonexistent relationship as a partnership.

## Employee advocacy

Employee social participation should remain voluntary and consistent with applicable organizational policy, disclosure requirements, confidentiality, and employment rules.

F124 should not fabricate employee voices or create undisclosed coordinated advocacy presented as spontaneous public opinion.

## Confidential information

Drafts should be checked for unreleased product information, customer data, internal metrics, private communications, credentials, security details, contractual information, or other confidential material.

Confidentiality concerns should be escalated before publication.

## Security and account safety

Social workflows should preserve account access controls, credential security, role separation, recovery procedures, and logging.

F124 should never request or expose passwords, authentication tokens, recovery codes, or other credentials in content artifacts.

## Measurement

`SKILLS/measurement_reasoning.py` and `TOOLS/metric_registry.py` support measurement discipline.

Potential metrics include reach, impressions, watch time, completion, saves, shares, comments, qualified engagement, clicks, conversions, response time, community growth, and downstream outcomes.

Metrics should be tied to objectives rather than optimized indiscriminately.

## Vanity metrics

Follower counts, likes, views, and impressions can be useful but may not represent trust, comprehension, qualified demand, customer value, or business impact.

F124 should avoid equating high visibility with successful strategy.

## Attribution

Social attribution is affected by cross-device behavior, dark social, organic discovery, delayed conversion, platform reporting, privacy controls, and multi-touch journeys.

The system should distinguish observed platform metrics from causal business impact.

## Experiments

Experiments can compare formats, hooks, timing, creative, calls to action, or audience approaches when ethical and operationally appropriate.

Experiments should define hypotheses and success criteria before results are interpreted.

## Algorithm changes

Platform recommendation systems and measurement definitions change over time.

F124 should preserve dates and avoid treating historical benchmarks as permanently stable.

## Content fatigue

Repeated messages can reduce audience value and increase unfollows, hiding, or negative sentiment.

The system should consider frequency, novelty, audience saturation, and channel context rather than maximizing posting volume.

## Community feedback loops

Questions, objections, complaints, and recurring discussion can inform future content, product education, support materials, and strategy.

Feedback should be summarized without exposing unnecessary personal information or treating vocal minorities as representative without evidence.

## Brand safety

Brand-safety review can include adjacent content, cultural context, current events, creator relationships, comments, hashtags, and platform placement.

`legal_reputation_risk` blocks release when material risk remains unresolved.

## Corrections

When published information is materially wrong, correction strategy should consider accuracy, visibility, timing, affected audiences, legal requirements, and preservation of trust.

F124 can recommend a correction but cannot autonomously delete or replace public content.

## Deletion boundary

`delete_public_content` is protected.

Deletion can destroy evidence, worsen a crisis, conflict with records obligations, or hide legitimate criticism. Authorized humans retain deletion authority.

## Campaign launch boundary

`launch_campaign` is protected.

A completed strategy, calendar, creative package, and measurement plan do not authorize autonomous campaign activation.

## External distribution boundary

`external_distribution` is protected.

The system can prepare approved-ready assets, but posting, syndication, account actions, paid amplification, direct outreach, and other external distribution remain under authorized human control.

## Evidence provenance

Material facts should preserve source, date, owner, version, context, limitations, and reviewer where relevant.

Evidence provenance supports corrections, audits, claims review, and reproducibility.

## Memory and state

The `memory/` layer can preserve structured workflow state across agents.

State should distinguish research evidence, audience assumptions, drafts, proposed replies, metrics, risks, human decisions, and published outcomes.

Private community information should not be retained beyond legitimate operational needs.

## Observability

The `observability/` layer supports traceability across the workflow.

Useful telemetry includes strategy state, content status, claim status, rights status, privacy review, community risks, approval state, measurement definitions, governance blockers, and attempts to invoke protected actions.

Observability does not create publication authority.

## Required reviews

The implemented safety policy requires all eight conditions:

```text
strategy_reviewed
content_reviewed
community_reviewed
claims_reviewed
privacy_consent_reviewed
legal_reputation_reviewed
evidence_provenance_reviewed
qualified_social_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- a claim exceeds reviewed evidence
- identity or impersonation risk remains unresolved
- harassment or abusive-engagement risk remains unresolved
- deceptive or manipulated engagement is detected
- privacy, consent, or personal-data review is incomplete
- copyright, licensing, or media-rights review is incomplete
- legal or reputational risk remains unresolved
- evidence provenance is incomplete
- any required review is missing
- qualified social-media approval is missing

The system exposes the blocker rather than manufacturing approval.

## Protected actions

The safety policy permanently protects:

```text
publish_post
publish_reply
send_direct_message
launch_campaign
delete_public_content
external_distribution
```

These actions remain outside autonomous authority even after all review conditions are satisfied.

## Human authority boundaries

F124 must not autonomously:

- publish posts
- publish comments or replies
- send direct messages
- launch social campaigns
- delete public content
- distribute content externally
- impersonate people or organizations
- create fake accounts or engagement
- approve legal, privacy, copyright, or reputational risk
- represent unverified claims as facts

Authorized humans retain control over accounts, publication, moderation decisions, crisis communications, campaigns, external messaging, and binding public representations.

## Explicit failure states

Useful explicit states include:

```text
STRATEGY REVIEW REQUIRED
CONTENT REVIEW REQUIRED
COMMUNITY REVIEW REQUIRED
CLAIM UNSUPPORTED
IMPERSONATION RISK
HARASSMENT RISK
DECEPTIVE ENGAGEMENT DETECTED
PRIVACY OR CONSENT GAP
COPYRIGHT OR RIGHTS GAP
LEGAL OR REPUTATION RISK
EVIDENCE PROVENANCE GAP
QUALIFIED SOCIAL APPROVAL REQUIRED
POST PUBLICATION PROHIBITED
REPLY PUBLICATION PROHIBITED
DIRECT MESSAGE PROHIBITED
CAMPAIGN LAUNCH PROHIBITED
PUBLIC CONTENT DELETION PROHIBITED
EXTERNAL DISTRIBUTION PROHIBITED
```

F124 must never fabricate engagement, audience evidence, testimonials, metrics, endorsements, public reactions, partnerships, permissions, or human approvals.

## End-to-end reference workflow

1. Define the communication objective and authorized accounts.
2. Identify audiences, channels, constraints, and brand context.
3. Develop platform-specific strategy and content pillars.
4. Build content briefs and calendar entries.
5. Draft content without fabricating facts, experiences, or endorsements.
6. Review claims and evidence provenance.
7. Review identity, privacy, consent, copyright, and media rights.
8. Review community, harassment, moderation, and crisis risks.
9. Review legal, reputational, platform, and regulated-domain concerns.
10. Define objective-linked metrics and attribution limits.
11. Record unresolved risks in the deterministic risk register.
12. Apply fail-closed governance.
13. Require explicit qualified-human social approval.
14. Keep publication, replies, DMs, campaign launches, deletion, and external distribution outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test strategy quality, content relevance, platform adaptation, evidence discipline, community-risk detection, measurement quality, and governance behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, successful reviewed release, unsupported claims, impersonation, harassment, deceptive engagement, privacy, copyright, legal or reputation risk, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed reference workflow.

## Reproducibility

Run:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

Reproducibility also depends on preserving source evidence, content versions, platform context, measurement definitions, risk decisions, and approval state.

## Extension points

Organization-specific implementations can add governed integrations for content management, social listening, analytics, asset libraries, customer support, brand systems, approval workflows, scheduling tools, and platform APIs.

Any integration that can perform an external account action should remain behind explicit authorization, least privilege, audit logging, and human-controlled execution.

## Example applications

Potential governed uses include social strategy development, content-calendar planning, thought-leadership support, community-response drafting, social listening synthesis, campaign planning, creator-program review, accessibility review, content-risk assessment, and social measurement analysis.

F124 is not an autonomous social account operator, bot network, crisis spokesperson, moderation authority, legal reviewer, or substitute for qualified communications judgment.

## Design principles

1. Optimize for legitimate communication objectives, not engagement at any cost.
2. Preserve human identity and never fabricate participation.
3. Substantiate material claims and preserve evidence provenance.
4. Protect privacy, consent, copyright, licensing, and confidential information.
5. Reject harassment, manipulation, fake engagement, and deceptive amplification.
6. Treat community and crisis risks as first-class workflow inputs.
7. Measure outcomes with explicit attribution limits.
8. Fail closed when material evidence or review is incomplete.
9. Keep publication and external account actions under authorized human control.

## Scope statement

F124 demonstrates a governed multi-agent architecture for social-media management support. It combines specialized strategy, content, community, measurement, and review agents with deterministic planning and risk tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over publication and external account actions.

Author: Mahsa Keikha
