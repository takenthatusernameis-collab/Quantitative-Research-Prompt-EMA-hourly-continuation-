# EMA Hourly Continuation — TFUEL/USDT P21_50

**Symbol:** TFUEL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1114 |
| net_profit_factor | 0.4148 |
| net_win_rate | 0.3833 |
| gross_profit_factor | 0.7654 |
| gross_win_rate | 0.4093 |
| sharpe_ratio | -10.9581 |
| sortino_ratio | -5.1588 |
| max_drawdown | 0.9986 |
| cagr | -0.9255 |
| net_avg_win | 16.5768 |
| net_avg_loss | -24.8384 |
| avg_hold_time_bars | 4.5215 |
| exposure | 0.2279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
