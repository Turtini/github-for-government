# How GitHub Supports Internal Controls

This section describes how GitHub can support common internal control objectives when configured and used intentionally.

This is illustrative, not prescriptive.
Organizations must assess controls within their own governance, risk, and compliance frameworks.

---

## Control Objective: Change Authorization

Goal:
Ensure changes are reviewed and approved before becoming authoritative.

How GitHub can support this:

- Changes are proposed separately from approval

- Review and approval can be required before acceptance

- Approvals are attributable to specific individuals

- Acceptance actions are explicit and logged

Result:
Unapproved changes cannot silently take effect.

---

## Control Objective: Change Documentation

Goal:
Maintain records explaining what changed and why.

How GitHub can support this:

- Each change is associated with a record (commit or pull request)

- Rationale can be documented alongside the change

- Discussion and clarification are preserved

- Historical context remains accessible

Result:
Change intent and context are retained alongside the artifact.

---

## Control Objective: Traceability

Goal:
Enable tracing from current state back to prior decisions and versions.

How GitHub can support this:

- Full version history is retained

- Changes can be compared across time

- Associated review activity is visible

- Artifacts can be referenced by version or timestamp

Result:
Teams can reconstruct how and when decisions evolved.

---

## Control Objective: Separation of Duties

Goal:
Reduce risk by distributing responsibilities across roles.

How GitHub can support this:

- Proposing changes can be separated from approving changes

- Approval authority can be restricted

- Roles can be aligned to organizational responsibilities

Result:
No single individual is required to both propose and approve changes.

---

## Control Objective: Access Management

Goal:
Ensure only authorized individuals can perform sensitive actions.

How GitHub can support this:

- Role-based access controls

- Read-only access for observers

- Elevated permissions limited to designated roles

- Access revocation when roles change

Result:
Capabilities align with assigned responsibility.

---

## Control Objective: Monitoring and Oversight

Goal:
Enable oversight without requiring direct participation.

How GitHub can support this:

- Activity is observable without modification rights

- Review history can be examined post hoc

- Changes are visible prior to acceptance

- Oversight does not require operational involvement

Result:
Oversight is enabled without introducing operational risk.

---

## Control Objective: Evidence Retention

Goal:
Retain evidence supporting decisions and changes.

How GitHub can support this:

- Historical records are preserved by default

- Prior versions remain accessible

- Review and approval artifacts are retained

Links can reference specific states in time

Result:
Evidence can be collected without recreating history.

---

## Control Objective: Error Detection and Recovery

Goal:
Detect errors and recover from unintended changes.

How GitHub can support this:

- Changes are visible before acceptance

- Prior versions can be restored

- Differences between versions are explicit

Errors can be discussed and corrected transparently

Result:
Mistakes are detectable and reversible.

---

## What GitHub Does Not Control

GitHub does not independently enforce:

- Organizational policy

- Regulatory compliance

- Records retention schedules

- Legal or statutory requirements

It provides mechanisms, not guarantees.

---

## Control Effectiveness Depends On

The effectiveness of GitHub as a control-supporting system depends on:

- Configuration choices

- Role assignment

- Review discipline

- Organizational policy alignment

- Training and expectations

Technology supports controls; it does not replace them.

---

## Summary for Internal Control Owners

When appropriately configured, GitHub can support internal controls by providing:

- Documented change authorization

- Preserved decision history

- Clear attribution of actions

- Structured review and approval

- Transparency without loss of control

Evaluating GitHub through this lens enables informed risk decisions rather than default rejection.
