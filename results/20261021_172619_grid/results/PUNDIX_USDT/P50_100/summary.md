# EMA Hourly Continuation — PUNDIX/USDT P50_100

**Symbol:** PUNDIX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.5584 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8146 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -3.4235 |
| sortino_ratio | -0.9875 |
| max_drawdown | 0.6819 |
| cagr | -0.3638 |
| net_avg_win | 45.9064 |
| net_avg_loss | -69.5605 |
| avg_hold_time_bars | 10.9534 |
| exposure | 0.2031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
