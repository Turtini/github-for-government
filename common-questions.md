# Questions Auditors Commonly Ask (and How to Answer Them)

This section addresses common questions raised during audit, compliance, security, and risk reviews when GitHub is introduced as part of an operating model.

The responses are intentionally conservative and factual.

---

## “Is GitHub a production system?”

Short answer: No.

Explanation:

GitHub is a collaboration and documentation platform. It does not execute workloads, process transactions, or operate live systems. It is typically used to manage artifacts about systems, not the systems themselves.

---

## “Can someone accidentally change something critical?”

Short answer: No.

Explanation:

Changes require intentional, logged actions. Reading content is non-destructive. Proposed changes are reviewed before acceptance, and permissions restrict who can approve changes.

---

## “Is there an audit trail?”

Short answer: Yes.

Explanation:

GitHub preserves a complete record of changes, including who made them, when they occurred, and what was modified. Historical versions remain accessible by default.

---

## “Can changes be made without approval?”

Short answer: Not when configured appropriately.

Explanation:

GitHub supports review and approval requirements before changes are accepted. Control effectiveness depends on configuration and governance, not the tool alone.

---

## “Can someone delete or alter history?”

Short answer: History is preserved in practice.

Explanation:

While content can evolve, prior versions and activity records remain accessible. Changes to history are visible and leave evidence, supporting post-hoc review.

---

## “Who controls access?”

Short answer: The repository owner.

Explanation:

Access is role-based and explicitly granted. Permissions can be limited to read-only, comment-only, proposal, or approval roles and revoked when necessary.

---

## “Is GitHub secure?”

Short answer: Security depends on use and configuration.

Explanation:

GitHub provides access controls, authentication, and activity logging. Organizations must determine appropriate usage based on data sensitivity and policy requirements.

---

## “Does using GitHub violate records management requirements?”

Short answer: Not inherently.

Explanation:

GitHub does not replace formal records systems. It can coexist alongside them as a working collaboration space, with authoritative records managed elsewhere as required.

---

## “Is this compliant with our regulatory framework?”

Short answer: That requires assessment.

Explanation:

GitHub provides capabilities that can support control objectives. Organizations must evaluate alignment with applicable frameworks (e.g., NIST, ISO, COSO) and internal policy.

---

## “Can GitHub be used with sensitive data?”

Short answer: That is a policy decision.

Explanation:

Organizations should determine what data types are appropriate for GitHub. Many teams restrict usage to public, draft, or non-sensitive materials.

---

## “What happens if something goes wrong?”

Short answer: Changes are reversible.

Explanation:

Prior versions are retained, differences are visible, and corrective changes can be proposed and reviewed transparently.

---

## “Who is accountable for decisions?”

Short answer: Individuals are identifiable.

Explanation:

Actions in GitHub are attributable to specific accounts, providing clarity on authorship, review, and approval.

---

## “Why not just use shared drives or email?”

Short answer: Those tools lack structured traceability.

Explanation:

Email and shared drives do not preserve decision history, review context, or structured approvals as effectively as GitHub.

---

## “Does transparency increase risk?”

Short answer: Transparency enables oversight.

Explanation:

Visibility into changes and decisions supports accountability and early detection. Risk arises from lack of controls, not from visibility itself.

---

## “What is the risk of not using something like GitHub?”

Short answer: Loss of traceability.

Explanation:

Without structured change tracking, organizations rely on informal processes that are harder to audit, reconstruct, or defend.

---

## Summary for Meetings

If asked to summarize:

GitHub is a documentation and collaboration platform that, when properly configured, supports traceability, review, and accountability. It does not replace policy or records systems, but it can strengthen internal controls around how work evolves.
