# EMA Hourly Continuation — STRAX/USDT P26_100

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.6448 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.8646 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -3.5836 |
| sortino_ratio | -1.1878 |
| max_drawdown | 0.7589 |
| cagr | -0.4220 |
| net_avg_win | 55.0106 |
| net_avg_loss | -70.9055 |
| avg_hold_time_bars | 13.0240 |
| exposure | 0.3227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
