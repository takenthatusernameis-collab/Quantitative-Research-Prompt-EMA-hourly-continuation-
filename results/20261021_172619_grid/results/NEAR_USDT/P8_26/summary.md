# EMA Hourly Continuation — NEAR/USDT P8_26

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.7858 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 1.0187 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -2.2009 |
| sortino_ratio | -0.7948 |
| max_drawdown | 0.6456 |
| cagr | -0.3061 |
| net_avg_win | 69.9340 |
| net_avg_loss | -87.6074 |
| avg_hold_time_bars | 6.4819 |
| exposure | 0.1871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
