# Hand-kept traces of the LocalSend evaluation

The second baseline of the ECR paper (protocol amendment 5, ECR 65f8064): for each mutant of `drift-bench/mutants/localsend/` (ECR e5425f2) on which a kept trace of `traces/localsend/` stops, the trace as an AI assistant edited it by hand so that it replays on that mutant. `hand/<mutant>/<persona>/` holds only the edited traces. The ids, steps and checks are those of the kept trace, except for the edit; no D6 mutant is edited.

Replay them on a mutant with the mutant's build command and `replay_traces=hand/<mutant>`.

Second edit (2026-11-26): malik taps Text twice (s3 and s7). On d1-send-text-button both taps get the new name, and on d4-message-dialog-before a tap on OK follows both, after the first replays on the mutants (runs 45789610884 and 45789716780) failed at s7 and s9.
