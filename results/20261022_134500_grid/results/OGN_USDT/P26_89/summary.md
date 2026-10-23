# EMA Hourly Continuation — OGN/USDT P26_89

**Symbol:** OGN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.5240 |
| net_win_rate | 0.4284 |
| gross_profit_factor | 0.8699 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -6.1580 |
| sortino_ratio | -2.3638 |
| max_drawdown | 0.9489 |
| cagr | -0.6809 |
| net_avg_win | 32.4736 |
| net_avg_loss | -46.4422 |
| avg_hold_time_bars | 9.6198 |
| exposure | 0.3252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
