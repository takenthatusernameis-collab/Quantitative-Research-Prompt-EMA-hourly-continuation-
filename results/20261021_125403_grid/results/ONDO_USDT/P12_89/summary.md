# EMA Hourly Continuation — ONDO/USDT P12_89

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8759 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0369 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -0.9063 |
| sortino_ratio | -0.2859 |
| max_drawdown | 0.3889 |
| cagr | -0.1267 |
| net_avg_win | 82.7447 |
| net_avg_loss | -98.0571 |
| avg_hold_time_bars | 21.5300 |
| exposure | 0.4727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
