# EMA Hourly Continuation — DEGEN/USDT P100_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 1.0515 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -3.2690 |
| sortino_ratio | -0.9697 |
| max_drawdown | 0.6995 |
| cagr | -0.3745 |
| net_avg_win | 62.6132 |
| net_avg_loss | -91.8121 |
| avg_hold_time_bars | 4.9140 |
| exposure | 0.0989 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
