<!--
NOTE GENERATION TEMPLATE GUIDANCE (do not include in output note)

This template is for generating technical **markdown** notes from YouTube transcripts using the notegen system. Follow these requirements:

1. Metadata (YouTube link, channel, date, and video length in frontmatter) included as markdown frontmatter.
2. Title: Use the exact video title.
3. Technical Summary
   - 2-4 sentences describing the central contribution, focusing on precise concepts, models, or algorithms.
4. Primary and Secondary Categories
   - Assign a Primary Category and a Secondary Category to the note. (see [keyword_concept.md](mdc:.cursor/rules/keyword_concept.mdc) for criteria)
5. Keyword List
   - List all relevant [[Keywords]] (see [keyword_concept.md](mdc:.cursor/rules/keyword_concept.mdc) for criteria). Place after the technical summary.
6. Core Ideas
   - Ordered list of technical concepts (not transcript order). Each: 1-3 sentences, use [[Keywords]].
7. Unique Insights and Statistics
   - Bullet points. Each must be an empirical/statistical claim, refined conceptual insight, model behavior insight, or novel interpretation. Use [[Keywords]].
-->
---
link: https://www.youtube.com/watch?v=JJ94MwfGZ-8
title: Victor Haghani - The Last of the Tactical Allocators
uploader: Flirting with Models
duration: 1:23:45
views: 1000000
---

# Victor Haghani - The Last of the Tactical Allocators

This interview explores Victor Haghani's approach to dynamic asset allocation through his firm Elm Wealth. The discussion centers on how to rationally construct portfolios based on expected returns, risk, and investor preferences, challenging traditional static allocation approaches.

Primary Category: [[Quantitative Finance]]
Secondary Category: [[Dynamic Asset Allocation]]

[[Dynamic Asset Allocation]] [[Risk-Adjusted Return]] [[Expected Return]] [[Market Portfolio]] [[Kelly Criterion]] [[Cost Matters Hypothesis]] [[Risk Matters Hypothesis]] [[Sharpe Ratio]]

## Core Ideas

- **Idea 1**: [[Dynamic Asset Allocation]] should be based on three key inputs: expected return of risky assets relative to safe assets, the riskiness of those assets, and the investor's personal risk aversion. This approach is fundamentally different from tactical allocation as it's not predicated on market inefficiencies.

- **Idea 2**: The [[Expected Return]] of equities can be estimated using cyclically adjusted earnings yield (CAPE), adjusted for payout ratios. This provides a reasonable estimate of long-term real returns, though it requires careful consideration of industry composition and accounting changes over time.

- **Idea 3**: Market risk has two main components: changes in discount rates and changes in earnings expectations. For long-term investors, changes in discount rates represent "good risk" as they don't affect the long-term consumption stream, while changes in earnings represent "bad risk" that directly impacts fundamental value.

- **Idea 4**: The [[Risk-Adjusted Return]] is the ultimate metric investors should care about, representing the certainty equivalent return of a portfolio. This is what determines the sustainable consumption stream from wealth, not the raw expected return or [[Sharpe Ratio]].

## Unique Insights and Statistics

- Approximately 50% of equity market volatility comes from changes in discount rates, while the other 50% comes from fundamental risk in earnings trajectory.

- Individual stocks have a much higher proportion of fundamental risk (80-90%) compared to market-wide discount rate risk (10-20%), making broad indices more attractive for risk-averse investors.

- The [[Risk Matters Hypothesis]] extends the [[Cost Matters Hypothesis]] to show that even in a zero-fee environment, the average actively managed portfolio must have higher risk than the market portfolio, creating an implicit cost through increased risk.

- Dynamic asset allocation strategies can allow investors to maintain higher average equity exposure than they would with a static allocation, as the ability to adjust to changing market conditions provides psychological comfort.
