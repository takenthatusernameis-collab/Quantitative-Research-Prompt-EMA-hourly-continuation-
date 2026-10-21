# EMA Hourly Continuation — FLOW/USDT P50_144

**Symbol:** FLOW/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.6742 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.8638 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -2.4156 |
| sortino_ratio | -0.6631 |
| max_drawdown | 0.5436 |
| cagr | -0.2629 |
| net_avg_win | 64.3846 |
| net_avg_loss | -82.1283 |
| avg_hold_time_bars | 16.8118 |
| exposure | 0.2843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
