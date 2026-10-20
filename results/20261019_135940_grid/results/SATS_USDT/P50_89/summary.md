# EMA Hourly Continuation — SATS/USDT P50_89

**Symbol:** SATS/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.5118 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.8281 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -4.7639 |
| sortino_ratio | -1.6164 |
| max_drawdown | 0.8589 |
| cagr | -0.5365 |
| net_avg_win | 34.6538 |
| net_avg_loss | -54.4646 |
| avg_hold_time_bars | 6.0103 |
| exposure | 0.1580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
