# EMA Hourly Continuation — ORCA/USDT P20_89

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7371 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -1.9519 |
| sortino_ratio | -0.6085 |
| max_drawdown | 0.5517 |
| cagr | -0.2459 |
| net_avg_win | 60.3132 |
| net_avg_loss | -79.4713 |
| avg_hold_time_bars | 18.4823 |
| exposure | 0.4024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
