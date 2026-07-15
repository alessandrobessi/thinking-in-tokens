# Bibliography

Master source list. Per-chapter files in this directory (`chapter-01.md`,
etc.) cite specific entries here against specific claims — this file just
collects the sources once, in one place, so they aren't retyped per chapter.

This is a lightweight system, not an academic reference manager: entries
are added as chapters make claims that need a traceable source, not
pre-emptively. See `ROADMAP.md` (Milestone 3) for the planned citation pass
over Part I's more contestable framing claims (e.g. "scale as the dominant
driver," "emergent abilities").

| Key | Citation | Used for |
|---|---|---|
| `shannon1948` | C. E. Shannon, "A Mathematical Theory of Communication," *Bell System Technical Journal*, 1948. | Formal definition of information/entropy (Ch. 2) |
| `vaswani2017` | A. Vaswani et al., "Attention Is All You Need," *NeurIPS*, 2017. | The transformer architecture (Ch. 1 preview, formally Ch. 11–12) |
| `sennrich2016bpe` | R. Sennrich, B. Haddow, A. Birch, "Neural Machine Translation of Rare Words with Subword Units," *ACL*, 2016. | Byte-Pair Encoding for tokenization (Ch. 3) |
| `mikolov2013word2vec` | T. Mikolov et al., "Efficient Estimation of Word Representations in Vector Space," *arXiv:1301.3781*, 2013. | Word embeddings, including the country/capital direction example (Ch. 5) |
| `kaplan2020scaling` | J. Kaplan et al., "Scaling Laws for Neural Language Models," *arXiv:2001.08361*, 2020. | Original characterization of scaling laws (Ch. 10) |
| `hoffmann2022chinchilla` | J. Hoffmann et al., "Training Compute-Optimal Large Language Models" (the "Chinchilla" paper), *arXiv:2203.15556*, 2022. | Data/parameter balance and undertraining (Ch. 10) |
| `rumelhart1986backprop` | D. Rumelhart, G. Hinton, R. Williams, "Learning Representations by Back-Propagating Errors," *Nature*, 1986. | Gradient descent / backpropagation, the parameter-adjustment procedure described conceptually in Ch. 9 |
| `ouyang2022instructgpt` | L. Ouyang et al., "Training Language Models to Follow Instructions with Human Feedback" (the "InstructGPT" paper), *arXiv:2203.02155*, 2022. | Fine-tuning and RLHF (Ch. 13 preview, formally Ch. 19) |
| `lewis2020rag` | P. Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," *arXiv:2005.11401*, 2020. | The RAG technique and name (Ch. 18) |
| `levesque2012winograd` | H. Levesque, E. Davis, L. Morgenstern, "The Winograd Schema Challenge," *KR*, 2012. | The trophy/suitcase sentence pair used as Ch. 11's real-world story |
| `holtzman2019degeneration` | A. Holtzman et al., "The Curious Case of Neural Text Degeneration," *arXiv:1904.09751*, 2019. | Nucleus (top-p) sampling (Ch. 14) |
| `rafailov2023dpo` | R. Rafailov et al., "Direct Preference Optimization: Your Language Model is Secretly a Reward Model," *arXiv:2305.18290*, 2023. | Direct preference optimization as an alternative to RLHF (Ch. 19) |
| `frantar2022gptq` | E. Frantar et al., "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers," *arXiv:2210.17323*, 2022. | Calibrated post-training quantization (Ch. 20) |
| `mata2023avianca` | *Mata v. Avianca, Inc.*, No. 22-cv-1461 (S.D.N.Y. June 22, 2023), Order on Sanctions. | The fabricated legal citations incident used as Ch. 15's real-world story |
| `ji2023hallucination` | Z. Ji et al., "Survey of Hallucination in Natural Language Generation," *ACM Computing Surveys*, 2023 (`arXiv:2202.03629`). | General hallucination-rate and mitigation claims (Ch. 15) |
