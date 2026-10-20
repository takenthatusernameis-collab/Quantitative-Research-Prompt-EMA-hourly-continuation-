# EMA Hourly Continuation — TNSR/USDT P12_100

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.7633 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 1.0263 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -2.8340 |
| sortino_ratio | -1.0530 |
| max_drawdown | 0.7389 |
| cagr | -0.3917 |
| net_avg_win | 67.7896 |
| net_avg_loss | -84.8142 |
| avg_hold_time_bars | 18.0991 |
| exposure | 0.5701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
