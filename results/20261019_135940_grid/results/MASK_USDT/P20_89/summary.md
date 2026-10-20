# EMA Hourly Continuation — MASK/USDT P20_89

**Symbol:** MASK/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.4533 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.7749 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -6.2367 |
| sortino_ratio | -2.3779 |
| max_drawdown | 0.9484 |
| cagr | -0.6847 |
| net_avg_win | 24.8727 |
| net_avg_loss | -41.2506 |
| avg_hold_time_bars | 12.4496 |
| exposure | 0.4154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
