# EMA Hourly Continuation — CYBER/USDT P8_20

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.7764 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0983 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -2.4462 |
| sortino_ratio | -0.9422 |
| max_drawdown | 0.6755 |
| cagr | -0.3503 |
| net_avg_win | 61.7285 |
| net_avg_loss | -86.2306 |
| avg_hold_time_bars | 5.4643 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
