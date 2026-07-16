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
| `openai2023functions` | OpenAI, "Function calling and other API updates," OpenAI blog, June 2023. | Mainstream introduction of structured tool/function calling (Ch. 21) |
| `anthropic2024mcp` | Anthropic, "Introducing the Model Context Protocol," Anthropic blog, November 2024. | The Model Context Protocol as a standardized tool-connection format (Ch. 21) |
| `yao2022react` | S. Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models," *arXiv:2210.03629*, 2022. | Early, influential description of interleaving reasoning with tool calls in a loop (Ch. 22) |
| `wei2022cot` | J. Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," *arXiv:2201.11903*, 2022. | Original chain-of-thought prompting result (Ch. 23) |
| `wang2022selfconsistency` | X. Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models," *arXiv:2203.11171*, 2022. | Multiple-candidate/majority-vote test-time compute (Ch. 23) |
| `deepseekai2025r1` | DeepSeek-AI, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning," *arXiv:2501.12948*, 2025. | Outcome-based reinforcement learning on reasoning trajectories, one publicly documented reasoning-model training recipe (Ch. 23) |
| `dosovitskiy2020vit` | A. Dosovitskiy et al., "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale," *arXiv:2010.11929*, 2020. | Patch-based image tokenization (Vision Transformer / ViT) (Ch. 24) |
| `radford2021clip` | A. Radford et al., "Learning Transferable Visual Models From Natural Language Supervision" (CLIP), *arXiv:2103.00020*, 2021. | Contrastive image-text alignment into a shared embedding space (Ch. 24) |
| `alayrac2022flamingo` | J. Alayrac et al., "Flamingo: a Visual Language Model for Few-Shot Learning," *NeurIPS*, 2022 (`arXiv:2204.14198`). | Cross-attention-bridge multimodal architecture (Ch. 24) |
| `liu2023llava` | H. Liu et al., "Visual Instruction Tuning" (LLaVA), *NeurIPS*, 2023 (`arXiv:2304.08485`). | Encoder-plus-projector multimodal architecture (Ch. 24) |
| `chameleon2024` | Chameleon Team, "Chameleon: Mixed-Modal Early-Fusion Foundation Models," *arXiv:2405.09818*, 2024. | Unified early-fusion-token multimodal architecture (Ch. 24) |
| `shazeer2017moe` | N. Shazeer et al., "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer," *arXiv:1701.06538*, 2017. | Original sparsely-gated Mixture-of-Experts formulation (Ch. 25) |
| `fedus2021switch` | W. Fedus, B. Zoph, N. Shazeer, "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity," *arXiv:2101.03961*, 2021. | Simplified single-expert-per-token routing at scale (Ch. 25) |
| `zheng2023judge` | L. Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," *arXiv:2306.05685*, 2023. | LLM-as-judge evaluation methodology (Ch. 26) |
| `greshake2023injection` | K. Greshake et al., "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection," *arXiv:2302.12173*, 2023. | Indirect prompt injection via retrieved/tool-fetched content (Ch. 28) |
